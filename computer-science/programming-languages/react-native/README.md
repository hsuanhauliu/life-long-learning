# Installation
```
brew install node
brew install watchman
npm install -g react-native-cli
```

## iOS
Also install Xcode command line tool. Go to Xcode Preference -> Locations and enable Command Line Tools.

## Android
1. Download Android Studio.
2. Install Java JDK (or OpenJDK). Follow this guide to properly install OpenJDK: https://www.youtube.com/watch?v=ru1itnqrRqU.

Follow the guide [here](https://facebook.github.io/react-native/docs/getting-started) under the Android section to properly set up the development environment.

# Run Your Project
To start a new project, enter
```
react-native init my-app
```

To run your app, type
```
cd my-app
react-native run-ios # replace run-ios with run-android to run the Android simulator
```

The above command will automatically run your app on the iOS Simulator by default.

To run a React Native app downloaded from Github, type the following command inside of the project folder.
```
npm install
react-native run-ios
```