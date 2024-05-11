import os
import uuid


def generate_path(image):
    image_name = os.path.splitext(image.filename)[0]
    extension = os.path.splitext(image.filename)[1].lower()
    uid = (str(uuid.uuid4()).replace('-', ''))[:16]
    filename = image_name + "_" + uid + extension
    return f"media/images/{filename}"