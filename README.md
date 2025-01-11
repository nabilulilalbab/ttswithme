# Indonesian Text-to-Speech Converter (TTS) using gTTS

This project provides a simple tool to convert Indonesian text into speech using the **gTTS (Google Text-to-Speech)** library. The tool reads sentences from a CSV file and generates corresponding audio files in MP3 format.

---

## 📝 Features
- Converts Indonesian text to speech using **gTTS**.
- Reads text input from a **CSV file**.
- Automatically generates separate **MP3 files** for each sentence.
- Supports **batch processing** of multiple sentences.

---

## 📂 Project Structure
```
|-- tts_converter.py   # Main script for text-to-speech conversion
|-- sentences.csv      # Sample CSV file containing sentences in Indonesian
|-- output_files/      # Folder to store generated MP3 files
```

---

## 🛠️ Requirements
Make sure you have the following installed:
- Python 3.6+
- gTTS library

To install **gTTS**, run the following command:
```bash
pip install gTTS
```

---

## 📥 Input CSV File Format
The input CSV file should have one sentence per row. For example:
```csv
"Saya akan pergi ke toko hari ini."
"Dia sedang membaca buku di perpustakaan."
"Apakah kamu ingin pergi jalan-jalan?"
"Hari ini sangat dingin."
"Saya suka mendengarkan musik."
```
Save this file as **sentences.csv**.

---

## 🚀 How to Run
### 1. Clone the Repository
```bash
git clone git@github.com:nabilulilalbab/ttswithme.git
cd ttswithme
```

### 2. Run the Script
To run the text-to-speech conversion, execute the following command:
```bash
python tts_converter.py
```

### 3. Enter the CSV Filename
When prompted, enter the name of the CSV file (e.g., `sentences.csv`):
```
Enter the CSV filename (including .csv extension): sentences.csv
```
The script will process each sentence in the CSV file and generate corresponding MP3 files.

---

## 🎧 Output Files
The output MP3 files will be saved in the current directory with the following format:
```
output_1.mp3
output_2.mp3
output_3.mp3
...
```
Each file corresponds to a sentence from the input CSV.

---

## 🛠️ Customization
You can modify the following parameters in the script:
- **Language**: The default language is set to `id` (Indonesian). You can change it to another language if needed by modifying the `language` parameter in the `convert_text_to_speech` function.
- **Output Filename**: The script automatically generates filenames like `output_1.mp3`, `output_2.mp3`, etc. You can customize the naming convention if desired.

---

## 🐛 Error Handling
The script includes error handling for the following scenarios:
- **Empty text input**: Raises a `ValueError` if the input text is empty or contains only whitespace.
- **File not found**: Displays an error if the specified CSV file is not found.
- **Unexpected errors**: Catches any unexpected errors and displays an appropriate message.

---

## 🤖 Example Usage
Sample interaction:
```
🇮🇩 Indonesian Text-to-Speech Converter from CSV 🔊
Enter the CSV filename (including .csv extension): sentences.csv
🔄 Converting: Saya akan pergi ke toko hari ini.
✅ Audio successfully saved as output_1.mp3
🔄 Converting: Dia sedang membaca buku di perpustakaan.
✅ Audio successfully saved as output_2.mp3
...
```

---

## 📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## 🧑‍💻 Author
- **Nabil Ulil Albab**
- [https://github.com/nabilulilalbab](https://github.com/nabilulilalbab)

---

## 💡 Future Enhancements
- Add support for multiple languages.
- Implement a GUI for easier usage.
- Allow user-defined output directories.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

Happy coding! 🎉


