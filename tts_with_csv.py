from gtts import gTTS
import os
import sys
import csv

def convert_text_to_speech(text, output_filename='output.mp3', language='en'):
    """
    Convert English text to speech using gTTS.
    
    Args:
        text (str): Input text in English to convert to speech
        output_filename (str, optional): Name of output MP3 file. Defaults to 'output.mp3'
        language (str, optional): Language code. Defaults to 'en' for English
    
    Raises:
        ValueError: If input text is empty
        Exception: For any other errors during conversion
    """
    try:
        # Validate input text
        if not text or text.isspace():
            raise ValueError("Input text cannot be empty")
        
        # Create gTTS object
        tts = gTTS(text=text, lang=language)
        
        # Save the audio file
        tts.save(output_filename)
        
        print(f"✅ Audio successfully saved as {output_filename}")
        return output_filename
    
    except ValueError as ve:
        print(f"❌ Error: {ve}")
        sys.exit(1)
    
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)

def process_csv_input(csv_filename, language='en'):
    """
    Read English sentences from a CSV file and convert them to speech.
    
    Args:
        csv_filename (str): Path to the CSV file containing the text
        language (str): Language code for the speech conversion
    
    """
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.reader(file)
            for idx, row in enumerate(reader, start=1):
                if row:  # Ensure there's text in the row
                    text = row[0].strip()  # Assume text is in the first column
                    output_filename = f"output_{idx}.mp3"
                    print(f"Converting: {text}")
                    convert_text_to_speech(text, output_filename, language)
    
    except FileNotFoundError:
        print(f"❌ Error: The file {csv_filename} was not found.")
        sys.exit(1)
    
    except Exception as e:
        print(f"❌ An unexpected error occurred while processing the CSV file: {e}")
        sys.exit(1)

def main():
    """
    Main function to handle user interaction and TTS conversion from CSV
    """
    print("\U0001F1EC\U0001F1E7 English Text-to-Speech Converter from CSV \U0001F50A")
    
    try:
        # Get the CSV filename from user
        csv_filename = input("Enter the CSV filename (including .csv extension): ").strip()
        
        # Process the CSV file and convert each sentence to speech
        process_csv_input(csv_filename)
    
    except KeyboardInterrupt:
        print("\n\n\U0001F44B Operation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()

