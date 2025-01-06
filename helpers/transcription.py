import os
import wave
import time
import pyaudio
import audioop
import PyPDF2
from groq import Groq
import keyboard

class InterviewAssistant:
    def __init__(self, stt_api_key, cv_chunks, response_generator, model="distil-whisper-large-v3-en", output_format="verbose_json"):
        self.client = Groq(api_key=stt_api_key)
        self.model = model
        self.output_format = output_format
        self.response_generator = response_generator
        self.cv_chunks = cv_chunks
        self.history = []
        self.should_exit = False  # Add flag to control program exit

    def transcribe_audio(self, audio_path):
        """Transcribes the given audio file using the STT API."""
        try:
            with open(audio_path, "rb") as file:
                transcription = self.client.audio.transcriptions.create(
                    file=(os.path.basename(audio_path), file.read()),
                    model=self.model,
                    response_format=self.output_format,
                )
            if hasattr(transcription, 'text'):
                return transcription.text
            elif isinstance(transcription, dict):
                return transcription.get('text', "Error: Transcription failed.")
            else:
                return str(transcription)
        except Exception as e:
            return f"Error: {e}"

    def record_audio(self, output_filename="recorded_audio.wav"):
        """Starts and stops audio recording manually using Ctrl+R."""
        chunk = 1024
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 44100

        p = pyaudio.PyAudio()
        is_recording = False
        stream = None

        try:
            print("Press 'Ctrl+R' to start recording. Release 'Ctrl+R' to stop recording.")
            print("Press 'q' to exit the program.")
            
            while not self.should_exit:
                if keyboard.is_pressed('q'):
                    print("\nExiting the program...")
                    self.should_exit = True
                    break
                
                if keyboard.is_pressed('ctrl+r') and not is_recording:
                    print("Recording started...")
                    frames = []
                    is_recording = True
                    stream = p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

                    while keyboard.is_pressed('ctrl+r') and not self.should_exit:
                        if keyboard.is_pressed('q'):
                            print("\nExiting the program...")
                            self.should_exit = True
                            break
                        data = stream.read(chunk, exception_on_overflow=False)
                        frames.append(data)

                    if not self.should_exit and frames:  # Only process if we have recorded something
                        print("Recording stopped.")
                        self.save_audio(frames, output_filename, channels, p.get_sample_size(audio_format), rate)
                        if stream:
                            stream.stop_stream()
                            stream.close()

                        # Add error handling for transcription
                        transcription = self.transcribe_audio(output_filename)
                        if transcription and not transcription.startswith("Error"):
                            print(f"Transcription: {transcription}")
                            response = self.response_generator.generate_response(transcription, self.cv_chunks, self.history)
                            self.history.append({
                                "role": "user",
                                "content": transcription
                            })
                            self.history.append({
                                "role": "assistant",
                                "content": response
                            })
                            print(f"Response: {response}")
                        else:
                            print(f"Transcription failed: {transcription}")
                        
                        try:
                            os.remove(output_filename)
                        except Exception as e:
                            print(f"Warning: Could not remove temporary audio file: {e}")
                    
                    is_recording = False
                time.sleep(0.1)  # Prevent CPU overuse

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if stream:
                stream.stop_stream()
                stream.close()
            p.terminate()

    @staticmethod
    def save_audio(frames, filename, channels, sample_width, rate):
        """Saves the recorded audio to a file."""
        try:
            with wave.open(filename, "wb") as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(sample_width)
                wf.setframerate(rate)
                wf.writeframes(b''.join(frames))
            print(f"Audio saved to {filename}.")
        except Exception as e:
            print(f"Error saving audio: {e}")

    def clear_history(self):
        """Clear the history at the end of the session."""
        self.history = []
        print("History cleared.")

    def clear_temp_files(self):
        """Clear the temporary files used during the session."""
        try:
            os.remove("recorded_audio.wav")
        except Exception as e:
            print(f"Warning: Could not remove temporary audio file: {e}")

