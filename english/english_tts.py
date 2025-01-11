from gtts import gTTS
import os
import sys

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

def main():
    """
    Main function to handle user interaction and TTS conversion
    """
    print("\U0001F1EC\U0001F1E7 English Text-to-Speech Converter \U0001F50A")
    
    try:
        # Get input text from user
        text = input("Enter English text to convert to speech: ").strip()
        
        # Optional: Let user specify output filename
        output_filename = input("Enter output filename (press Enter for default 'output.mp3'): ").strip()
        output_filename = output_filename if output_filename else 'output.mp3'
        
        # Ensure filename ends with .mp3
        if not output_filename.lower().endswith('.mp3'):
            output_filename += '.mp3'
        
        # Convert text to speech
        convert_text_to_speech(text, output_filename)
    
    except KeyboardInterrupt:
        print("\n\n\U0001F44B Operation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
