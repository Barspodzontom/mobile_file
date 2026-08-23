# -*- coding: utf-8 -*-
import secrets
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown_opened = False

    def toggle_dropdown(self, button):
        dropdown = self.ids.dropdown_menu
        if self.dropdown_opened:
            dropdown.dismiss()
            self.dropdown_opened = False
        else:
            dropdown.open(button)
            self.dropdown_opened = True

    def dismiss_dropdown(self):
        self.ids.dropdown_menu.dismiss()
        self.dropdown_opened = False


    def show_help(self):
        self.ids.password_display.text = "Справка: генерируйте надёжные пароли!"
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.restore_display_text(), 2)

    def restore_display_text(self):
        if self.ids.password_display.text == "Справка: генерируйте надёжные пароли!":
            self.ids.password_display.text = "Ваш пароль появится тут"

    def generate_password(self, length, lower, upper, digit, punct):
        lowercase = 'abcdefghkmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHKMNOPQRSTUVWXYZ'
        digits = '23456789'
        punctuation = '}#$%&*+/<=>?@{~'
        chars = ''

        if lower:
            chars += lowercase
        if upper:
            chars += uppercase
        if digit:
            chars += digits
        if punct:
            chars += punctuation

        if not chars:
            self.ids.password_display.text = "Выберите типы символов!"
            return

        # Генерация пароля
        while True:
            password = ''.join(secrets.choice(chars) for _ in range(length))
            has_letter = any(c in lowercase for c in password) if lower else True
            has_upper = any(c in uppercase for c in password) if upper else True
            has_digit = any(c in digits for c in password) if digit else True
            has_special = any(c in punctuation for c in password) if punct else True

            if has_letter and has_upper and has_digit and has_special:
                break

        self.ids.password_display.text = password

    def copy_to_clipboard(self):
        password = self.ids.password_display.text
        if password and not password.startswith("Выберите") and \
           not password.startswith("Справка:") and password != "Скопировано!":
            Clipboard.copy(password)
            self.ids.password_display.text = "Скопировано!"
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.restore_password(password), 1)

    def restore_password(self, pwd):
        if self.ids.password_display.text == "Скопировано!":
            self.ids.password_display.text = pwd


class LblApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    LblApp().run()
