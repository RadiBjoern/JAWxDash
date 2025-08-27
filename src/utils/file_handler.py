import base64
import os
import uuid

from src.templates.settings_template import UPLOAD_DIRECTORY
    


def save_upload(content, filename) -> str:
    _, content_string = content.split(",")
    decoded = base64.b64decode(content_string)

    _, ext = os.path.splitext(filename)
    unique_name = "%s_%s" % (uuid.uuid4().hex, filename)

    file_path = os.path.join(UPLOAD_DIRECTORY, unique_name)

    with open(file_path, "wb") as f:
        f.write(decoded)
    
    return file_path
