from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Пример словаря шифрования (двузначные коды -> кириллица)
# Можешь настроить пары под свои значения.ю
CIPHER_DICT = {
    '10': 'А', '11': 'Б', '12': 'В', '13': 'Г', '14': 'Д',
    '15': 'Е', '16': 'Ж', '17': 'З', '18': 'И', '19': 'К',
    '20': 'Л', '21': 'М', '22': 'Н', '23': 'О', '24': 'П',
    '25': 'Р', '26': 'С', '27': 'Т', '28': 'У', '29': 'Ф',
    '30': 'Х', '31': 'Ц', '32': 'Ч', '33': 'Ш', '34': 'Щ',
    '35': 'Ъ', '36': 'Ы', '37': 'Ь', '38': 'Э', '39': 'Ю', '40': 'Я',
    ' ': ' '
}

# Обратный словарь для шифрования. (буква -> код)
DECIPHER_DICT = {v: k for k, v in CIPHER_DICT.items()}

class DecoderApp(App):
    def build(self):
        self.title = "Дешифратор"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.input_text = TextInput(
            hint_text='Введите текст или коды...',
            size_hint=(1, 0.3),
            font_size=18
        )
        layout.add_widget(self.input_text)
        
        btn_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)
        
        decode_btn = Button(text='Расшифровать', background_color=(0.1, 0.6, 0.3, 1))
        decode_btn.bind(on_press=self.decode_action)
        btn_layout.add_widget(decode_btn)
        
        encode_btn = Button(text='Зашифровать', background_color=(0.3, 0.4, 0.8, 1))
        encode_btn.bind(on_press=self.encode_action)
        btn_layout.add_widget(encode_btn)
        
        layout.add_widget(btn_layout)
        
        self.result_label = Label(
            text='Результат появится здесь',
            size_hint=(1, 0.4),
            font_size=20,
            halign='center',
            valign='middle'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        layout.add_widget(self.result_label)
        
        return layout

    def decode_action(self, instance):
        text = self.input_text.text.strip()
        # Простая логика расшифровки по парам символов или через пробелы
        words = text.split()
        decoded_result = []
        for word in words:
            # Если код разбит по 2 символа
            decoded_word = ""
            i = 0
            while i < len(word):
                code = word[i:i+2]
                decoded_word += CIPHER_DICT.get(code, code)
                i += 2
            decoded_result.append(decoded_word)
        self.result_label.text = " ".join(decoded_result)

    def encode_action(self, instance):
        text = self.input_text.text.upper()
        encoded_result = []
        for char in text:
            encoded_result.append(DECIPHER_DICT.get(char, char))
        self.result_label.text = " ".join(encoded_result)

if __name__ == '__main__':
    DecoderApp().run()
