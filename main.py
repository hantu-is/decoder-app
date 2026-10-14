from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class DecoderApp(App):

  def build(self):
    self.title = 'Decoder'

    # Главный контейнер (расположение элементов друг под другом)
    layout = BoxLayout(
        orientation='vertical', padding=20, spacing=15, size_hint=(1, 1)
    )

    # Заголовок
    self.label_info = Label(
        text='Введите текст для декодирования:',
        size_hint=(1, 0.1),
        font_size=18,
    )
    layout.add_widget(self.label_info)

    # Поле ввода текста
    self.text_input = TextInput(
        text='',
        hint_text='Сюда введи зашифрованный текст...',
        size_hint=(1, 0.3),
        multiline=True,
    )
    layout.add_widget(self.text_input)

    # Кнопка действия
    self.btn_decode = Button(
        text='Декодировать', size_hint=(1, 0.15), background_color=(0.1, 0.6, 1, 1)
    )
    self.btn_decode.bind(on_press=self.on_decode_click)
    layout.add_widget(self.btn_decode)

    # Поле вывода результата
    self.label_result = Label(
        text='Результат появится здесь', size_hint=(1, 0.3), font_size=16
    )
    layout.add_widget(self.label_result)

    return layout

  def on_decode_click(self, instance):
    # Получаем текст из поля ввода
    user_text = self.text_input.text

    # Твоя логика декодирования (пока что просто пример)
    # Здесь ты можешь написать свой алгоритм расшифровки
    decoded_text = (
        f'Расшифровано: {user_text[::-1]}'  # Пример: переворачиваем текст задом наперед
    )

    # Выводим результат на экран
    self.label_result.text = decoded_text


if __name__ == '__main__':
  DecoderApp().run()
