import base64
import datetime
import shutil
from decouple import config


class Base64ToFile:
    def __init__(self, data):
        self.data = data
        self.file_name = ''
        self.base64_img_bytes = self.data.encode('utf-8')
        self.__convert()

    def __convert(self):
        self.file_name = self.__generate_name()
        with open(f"{self.file_name}.png", 'wb') as file_to_save:
            decoded_image_data = base64.decodebytes(self.base64_img_bytes)
            file_to_save.write(decoded_image_data)
            shutil.move(f"{self.file_name}.png", f'static/images/{self.file_name}.png')
            file_to_save.close()

    @property
    def filename(self):
        if self.file_name:
            return f"{self.file_name}.png"
        return ''

    @classmethod
    def __generate_name(cls):
        return int(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
