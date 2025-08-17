[app]
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
log_level = 2
warn_on_root = 1

[buildozer]
# Storage directories
build_dir = ./.buildozer
bin_dir = ./bin
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk wget python3-pip python3-setuptools build-essential

# Install buildozer and cython
python3 -m pip install --upgrade pip
python3 -m pip install buildozer cython

# Initialize buildozer
buildozer init

# Optional: If AIDL error shows, install extra dependencies
sudo apt install -y libc6:i386 libncurses5 libstdc++6 lib32z1 libbz2-1.0:i386
# Clean previous build (optional)
buildozer android clean

# Build debug APK
buildozer android debug
