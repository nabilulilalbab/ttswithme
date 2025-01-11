import os
from gtts import gTTS
import pygame

def text_to_speech(text, lang='en', slow=False, output_file='output.mp3'):
    """
    Convert text to speech using Google Text-to-Speech (gTTS)
    
    Args:
        text (str): Text to be converted to speech
        lang (str, optional): Language code. Defaults to 'en' (English).
        slow (bool, optional): Speak slowly if True. Defaults to False.
        output_file (str, optional): Output audio file name. Defaults to 'output.mp3'.
    
    Returns:
        str: Path to the generated audio file
    """
    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=lang, slow=slow)
        
        # Save the audio file
        tts.save(output_file)
        print(f"Audio saved as {output_file}")
        
        return output_file
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def play_audio(audio_file):
    """
    Play the generated audio file
    
    Args:
        audio_file (str): Path to the audio file
    """
    try:
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load and play the audio
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except Exception as e:
        print(f"Error playing audio: {e}")
    
    finally:
        # Clean up pygame mixer
        pygame.mixer.quit()

def main():
    # Example usage
    text = "Hello, this is a text-to-speech demonstration using Google Text-to-Speech library."
    
    # Convert text to speech
    audio_file = text_to_speech(text)
    
    # Play the audio if successfully generated
    if audio_file:
        play_audio(audio_file)

if __name__ == "__main__":
    main()

