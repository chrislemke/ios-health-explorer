# Explore iOS health
### Explore and visualize data from the iOS health app

<img src="https://github.com/stoffy/ios_health_analysing/blob/master/images/health-app-icon.png" alt="iOS health app">

This project can be used to explore, visualize and investigate the data provided by the iOS health app. The data can be exported to a XML file by tapping on the profile icon in the right corner in the health app.

### Collect data from XML
Apple stores the health data in XML format. From each record the following attributes are processed: `type`, `unit`, `startDate`, `value` and `sourceName`.
Only certain types are taken, but this list can be customized:

* `HKQuantityTypeIdentifierHeartRate` 
* `HKQuantityTypeIdentifierActiveEnergyBurned`
* `HKQuantityTypeIdentifierDistanceWalkingRunning`
* `HKQuantityTypeIdentifierAppleExerciseTime`
* `HKQuantityTypeIdentifierAppleStandTime`
* `HKQuantityTypeIdentifierStepCount`

The complete list may vary between iOS versions:

`HKQuantityTypeIdentifierBodyMassIndex`,
`HKQuantityTypeIdentifierStairDescentSpeed`,
`HKQuantityTypeIdentifierBasalEnergyBurned`,
`HKQuantityTypeIdentifierVO2Max`,
`HKQuantityTypeIdentifierWalkingStepLength`,
`HKQuantityTypeIdentifierStepCount`,
`HKQuantityTypeIdentifierActiveEnergyBurned`,
`HKQuantityTypeIdentifierHeadphoneAudioExposure`,
`HKQuantityTypeIdentifierHeartRateVariabilitySDNN`,
`HKQuantityTypeIdentifierHeight`,
`HKQuantityTypeIdentifierBodyFatPercentage`,
`HKCategoryTypeIdentifierHighHeartRateEvent`,
`HKQuantityTypeIdentifierEnvironmentalAudioExposure`,
`HKQuantityTypeIdentifierWalkingHeartRateAverage`,
`HKQuantityTypeIdentifierRestingHeartRate`,
`HKCategoryTypeIdentifierMindfulSession`,
`HKQuantityTypeIdentifierSixMinuteWalkTestDistance`,
`HKQuantityTypeIdentifierDietaryWater`,
`HKQuantityTypeIdentifierFlightsClimbed`,
`HKQuantityTypeIdentifierLeanBodyMass`,
`HKQuantityTypeIdentifierDistanceWalkingRunning`,
`HKCategoryTypeIdentifierAppleStandHour`,
`HKQuantityTypeIdentifierBodyMass`,
`HKCorrelationTypeIdentifierBloodPressure`,
`HKDataTypeSleepDurationGoal`,
`HKQuantityTypeIdentifierWalkingDoubleSupportPercentage`,
`HKQuantityTypeIdentifierBloodPressureSystolic`,
`HKQuantityTypeIdentifierAppleStandTime`,
`HKQuantityTypeIdentifierWalkingAsymmetryPercentage`,
`HKQuantityTypeIdentifierBloodPressureDiastolic`,
`HKQuantityTypeIdentifierWalkingSpeed`,
`HKQuantityTypeIdentifierDistanceCycling`,
`HKCategoryTypeIdentifierAudioExposureEvent`,
`HKQuantityTypeIdentifierStairAscentSpeed`,
`HKQuantityTypeIdentifierAppleExerciseTime`,
`HKCategoryTypeIdentifierSleepAnalysis`,
`HKQuantityTypeIdentifierHeartRate`

### Visiualize your data to understand it better
<img src="https://github.com/stoffy/ios-health-explorer/blob/master/images/heart-walk-graphs.png" alt="Heart rate, walking and steps chart">

<img src="https://github.com/stoffy/ios-health-explorer/blob/master/images/steps-headmap.png" alt="Steps heatmap">


For more information on the Apple health app visit: [https://www.apple.com/ios/health/](https://www.apple.com/ios/health/)
