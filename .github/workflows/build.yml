name: Build APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    name: Build Android APK
    runs-on: ubuntu-latest
    env:
      ANDROIDAPI: 33
      ANDROIDMINAPI: 21
      ANDROIDNDK: 25b

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y python3-pip openjdk-11-jdk zip unzip git wget curl build-essential
          pip install --upgrade pip buildozer cython

      - name: Setup Android SDK & NDK
        run: |
          mkdir -p $HOME/android-sdk/cmdline-tools
          cd $HOME/android-sdk/cmdline-tools
          wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O cmdline-tools.zip
          unzip cmdline-tools.zip
          mv cmdline-tools latest
          export ANDROID_HOME=$HOME/android-sdk
          export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH
          yes | sdkmanager --sdk_root=$ANDROID_HOME "platform-tools" "platforms;android-33" "build-tools;34.0.0" "ndk;25.2.9519653" "cmake;3.22.1"

      - name: Build APK with Buildozer
        run: |
          buildozer android debug

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: MyApp-APK
          path: bin/*.apk
