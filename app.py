from helpers.transcription import InterviewAssistant
from helpers.response import GenerateResponse
import keyboard
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API key not found. Ensure it's set in the .env file.")
    cv_path = "cv.pdf"

    try:
        response_generator = GenerateResponse(api_key=api_key)
        print(f"Loading CV from: {cv_path}")
        
        cv_text = response_generator.extract_text_from_pdf(cv_path)
        if "Error" in cv_text:
            print(f"Error extracting CV text: {cv_text}")
            return
        
        cv_chunks = response_generator.chunk_text(cv_text)
        if not cv_chunks:
            print("Error: CV text could not be chunked correctly.")
            return

        assistant = InterviewAssistant(api_key, cv_chunks, response_generator)
        
        print("Starting the Interview Assistant...")
        while not assistant.should_exit:
            assistant.record_audio(output_filename="recorded_audio.wav")
            if assistant.should_exit:
                print("Interview session ended.")
                break

        assistant.clear_history()
        assistant.clear_temp_files()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Interview Assistant process completed.")


if __name__ == "__main__":
    main()