from google.colab import files
import os

def upload_and_rename(filename="im1.png"):
    uploaded = files.upload()
    original_name = list(uploaded.keys())[0]
    os.rename(original_name, filename)
    return filename
