import base64

class Converter():
    def __init__(self):
        self.encoding = 'utf-8'

    def converting_text(self, from_text, to_text, from_box_text):
        to_text_return = ''
        if to_text == 'Base64':
            if from_text == 'UTF-8':
                to_text_return = self.__convert_utf8_base64(from_box_text)
            elif from_text == '%Char':
                pass
        elif to_text == 'UTF-8':
            if from_text == 'Base64':
                to_text_return = self.__convert_base64_utf8(from_box_text)
            elif from_text == '%Char':
                to_text_return = self.__convert_percent_utf8(from_box_text)
        elif to_text == '%Char':
            if from_text == 'UTF-8':
                to_text_return = self.__convert_utf8_percent(from_box_text)



        return to_text_return

    def __convert_utf8_base64(self, from_text):
        """converting string to ascii then to Base64
        after removing newlines making it urlsafe"""

        return base64.b64encode(from_text.encode(self.encoding))

    def __convert_base64_utf8(self, from_text):
        """convert base64 to utf-8 string"""
        return base64.urlsafe_b64decode(from_text)

    def __convert_utf8_percent(self, from_text):
        return ''.join('%' + str(ord(character)) for character in from_text)

    def __convert_percent_utf8(self, from_text):
        percent_chars = from_text.split('%')
        if percent_chars[0] == '':
            percent_chars.pop(0)
        encoded = ''.join(chr(int(character)) for character in percent_chars)
        return encoded
