import uuid
from uuid import UUID
import os

def upload_image(image):
    extension = os.path.splitext(image)[1].lower()
    print(extension)
    name = (str(uuid.uuid4()).replace('-', ''))[:16]
    filename = name + extension
    return filename


def main() -> None:
    print(upload_image("file.png"))
    
if __name__ == '__main__':
    main()