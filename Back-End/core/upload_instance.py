from core import Base64ToFile


class UpLoadBase64:
    @classmethod
    def upload_image_base64(cls, data):
        if data and (len(data) > 40):
            return Base64ToFile(data).filename
        return data


upload_base64 = UpLoadBase64()