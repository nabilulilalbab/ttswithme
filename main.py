import re

import requests
import os
import shutil
from gradio_client import Client

# Pastikan folder "output" sudah ada
os.makedirs("output", exist_ok=True)

# Inisialisasi Client
client = Client("Deddy/TTS-Indonesiaku-Gratis")
text = "We see that we have 1 API endpoint in this space, and shows us how to use the API endpoint to make a prediction: we should call the .predict() method (which we will explore below), providing a parameter input_audio of type str, which is a filepath or URL."
# Melakukan inferensi TTS
result = client.predict(
    text= text,
    speaker_label="ardi",
    speed=0.4,
    language="Indonesian",
    api_name="/gen_voice"
)
print(result)

# Tentukan path file output
text = re.sub(r"[.,]", "", text).replace(" ", "-")
output_path = f"output/{text}.wav"

# Salin file dari path lokal yang dikembalikan oleh API ke folder output
# Check if the result is a URL or a file path
if os.path.isfile(result):
    with open(result, 'rb') as src_file:
        with open(output_path, 'wb') as dest_file:
            shutil.copyfileobj(src_file, dest_file)
else:
    # Assume result is a URL and download the content
    if not result.startswith(('http://', 'https://')):
        result = 'http://' + result
    response = requests.get(result)
    with open(output_path, 'wb') as dest_file:
        dest_file.write(response.content)

print(f"Audio berhasil disimpan di {output_path}")

