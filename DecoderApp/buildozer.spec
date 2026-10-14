[app]

# (str) Title of your application
title = Decoder

# (str) Package name
package.name = decoder

# (str) Package domain (needed for android packaging)
package.domain = org.hantu

# (str) Source files where the *.py files exist
source.dir = .

# (list) Source files to include (let empty to include all files)
source.exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Зафиксирован стабильный python3==3.11 для избежания ошибок компиляции тестов
requirements = python3==3.11,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Permissions
android.permissions = INTERNET

# (str) Orientation of the application
orientation = portrait

# (list) List of services to declare
#services = 

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
#android.sdk = 20

# (str) ANT version to use
#android.ant_version = 1.9.4

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) The format used to package the app for store/testing ('apk' or 'aab')
android.format = apk

# (int) Logger level (0 = debug, 1 = info, 2 = warning, 3 = error)
log_level = 2

# (str) Path to a custom __init__.py before the application starts
#android.manifest.intent_filters =
