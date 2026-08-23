[app]

title = Password Generator
package.name = passgen
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# ВАЖНО: 
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Указываем, какой именно файл запускать, если он НЕ называется main.py
# Это заставит Buildozer взять в сборку именно Ran_pass.py
source.include_patterns = Ran_pass.py

# Android-специфичные настройки (можно оставить как есть, это хороший базовый набор)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.debug_artifact = apk
android.accept_sdk_license = True
