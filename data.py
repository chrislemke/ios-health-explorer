import pandas as pd
import xml.etree.ElementTree as et


class DataProvider():

    @classmethod
    def __get_xroot(self, path):
        xtree = et.parse(path)
        return xtree.getroot()

    @classmethod
    def rows_and_columns_xml(self, path):
        xroot = self.__get_xroot(path)

        types = set([])
        rows = []

        for node in xroot[0:]:

            types.add(node.attrib.get('type'))

            if node.attrib.get('type') == 'HKQuantityTypeIdentifierHeartRate' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierActiveEnergyBurned' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierBasalEnergyBurned' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierDistanceWalkingRunning' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierAppleExerciseTime' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierAppleStandTime' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierFlightsClimbed' or \
                    node.attrib.get('type') == 'HKQuantityTypeIdentifierStepCount':

                s_type = node.attrib.get('type')
                s_unit = node.get('unit')
                s_dateTime = node.get('startDate')
                s_value = float(node.get('value'))
                s_source = node.get('sourceName')

                columns = ['type', 'source', 'unit', 'dateTime', 'value']

                rows.append({'type': s_type,
                             'unit': s_unit,
                             'dateTime': s_dateTime,
                             'source': s_source,
                             'value': s_value})

        print('Available data types:')
        for data_type in types:
            print(data_type)
        return (rows, columns)


class DataManager():

    @classmethod
    def grouped_by_date_df(self, df, data_type, column_name, grouped_strategy):
        grouped_df = df[df['type'].isin([data_type])]
        if grouped_strategy == 'mean':
            grouped_df = round(grouped_df.groupby('dateTime').mean(), 0)
        elif grouped_strategy == 'sum':
            grouped_df = round(grouped_df.groupby('dateTime').sum(), 4)
        else:
            raise ValueError(
                "Invalid value for 'grouped_strategy'! Should be either 'mean' or 'sum'.")
        return grouped_df.rename(columns={'value': column_name})

    @classmethod
    def merge(self, dataframes_list):
        if len(dataframes_list) < 2:
            raise ValueError(
                "'dataframes_array' should contain at least two dataframes!")

        merged = pd.merge(dataframes_list[0], dataframes_list[1], how='inner',
                          left_index=True, right_index=True)

        if len(dataframes_list) > 2:
            for df in dataframes_list[2:]:
                merged = pd.merge(merged, df, how='inner',
                                  left_index=True, right_index=True)
        return merged

    @classmethod
    def handle_nan(self, df):
        df['standTime(min)'] = df['standTime(min)'].fillna(0.0)
        df['stepCount'] = df['stepCount'].fillna(0)
        df['activeEnergyBurned(kal)'] = df['activeEnergyBurned(kal)'].fillna(
            0.0)
        df['walkingRunningDistance(km)'] = df['walkingRunningDistance(km)'].fillna(
            0.0)
        return df.dropna()


class DataFormatter():

    @classmethod
    def format_time_df(self, df):
        date = pd.to_datetime(df['dateTime'])
        date = date.dt.tz_localize(None)
        date = date.dt.floor('Min')
        df['date'] = date.dt.floor('d')
        df['weekday'] = date.dt.weekday.astype('category')
        df['startTime'] = date.dt.time
        return df

    @classmethod
    def date_df(self, merged_df):
        avg_hr_date = pd.DataFrame(merged_df.groupby(['date'])[
            'heartRate(BPM)'].mean())
        total_sc_date = pd.DataFrame(
            merged_df.groupby(['date'])['stepCount'].sum())
        total_aeb_date = pd.DataFrame(merged_df.groupby(
            ['date'])['activeEnergyBurned(kal)'].sum())
        total_wd_date = pd.DataFrame(merged_df.groupby(
            ['date'])['walkingRunningDistance(km)'].sum())
        total_st_date = pd.DataFrame(merged_df.groupby(['date'])[
            'standTime(min)'].sum())

        df_list = [avg_hr_date, total_sc_date,
                   total_aeb_date, total_wd_date, total_st_date]

        date_df = DataManager.merge(df_list).reset_index()
        return date_df.rename(columns={
            'heartRate(BPM)': 'heartRateAvg(BPM)',
            'stepCount': 'stepCountSum',
            'activeEnergyBurned(kal)': 'activeEnergyBurnedSum(kal)',
            'walkingRunningDistance(km)': 'walkingRunningDistanceSum(km)',
            'standTime(min)': 'standTimeSum(min)'
        })
