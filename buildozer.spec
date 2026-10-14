[app]

# (str) Title of your application
title = Decoder

# (str) Package name
package.name = decoder

# (str) Package domain (needed for android packaging)
package.domain = org.hantu

# (str) Version of the application
version = 1.0

# (str) Source files where the *.py files exist
source.dir = .

# (list) Source files to include (let empty to include all files)
source.exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Зафиксирован стабильный python3==3.11 для избежания ошибок компиляции тестов
requirements = python3==3.11,kivy

# (list) Permissions
android.permissions = INTERNET

# (str) Orientation of the application
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) The format used to package the app for store/testing ('apk' or 'aab')
android.format = apk

# (int) Logger level (0 = debug, 1 = info, 2 = warning, 3 = error)
log_level = 2
