# PromptPilot

## Overview

**PromptPilot** is a transformative application designed to help individuals articulate their thoughts during interviews or professional conversations. Powered by advanced Generative AI, PromptPilot combines real-time voice transcription and response generation to assist users in confidently handling interviews and overcoming nervousness or communication barriers.

---

⚠️ **Disclaimer** ⚠️
This application is designed as a supportive tool for practicing and improving communication skills. **PromptPilot** is not intended to promote cheating, deceive, or mislead during professional interactions. Users are encouraged to use this tool ethically and responsibly, ensuring they rely on their own abilities during interviews and presentations.

---

## Features

1. **Real-Time Audio Processing**: Seamlessly records and transcribes audio for immediate analysis.  
2. **Accurate Voice Recognition**: Leverages **Whisper distil-large-v3 model** for highly precise and efficient audio transcription.  
3. **Personalized Response Generation**: Uses **LLaMA 3.3** to craft thoughtful, relevant answers tailored to the user's context.  
4. **Retrieval-Augmented Generation (RAG) Framework**:  
   - Utilizes **contextual retrieval from CV text chunks** to enrich the generative process.  
   - Ensures accurate and contextually relevant responses by combining user input with preloaded CV information.  
5. **History-Based Conversation Management**: Maintains a dynamic conversation history for **context retention** and coherent multi-turn dialogue. Limits the memory scope to the last 10 exchanges, optimizing for relevance and computational efficiency.  
6. **Transparent and Intuitive Interface**: Semi-transparent interface ensures **uninterrupted interaction** with primary tasks during transcription and response review. Designed for **real-time usability**, minimizing disruptions while maximizing output clarity.  
7. **Streamlined Personalization via CV Integration**:  
   - Users can load their **CV as a PDF** into the application folder (`cv.pdf`) or specify a custom path.  
   - Automatically parses and **chunks CV data into manageable pieces** for efficient contextual reference during response generation.  
8. **Real-Time Audio Control**: Integrated **keyboard shortcuts** for seamless operation:  
   - **Ctrl+R** to toggle recording.  
   - **Q** to terminate the session.  
   - Audio is recorded as `recorded_audio.wav` and transcribed instantly for interaction.  
9. **Ethics-Oriented Design**: Explicitly avoids misuse by promoting the tool as a **practice companion** for enhancing communication skills. Encourages ethical application in interview preparation and professional growth.  
10. **Streamlined Installation and Setup**: Minimalistic dependency requirements managed via `requirements.txt`. Users need only provide their **Groq API Key** and ensure Python 3.10+ compatibility.  
11. **Robust Error Handling**: Comprehensive error-checking mechanisms for CV parsing, audio transcription, and response generation. Provides detailed feedback for troubleshooting and seamless user experience.  
12. **Modular and Extensible Architecture**: Core functionalities split into reusable classes for **audio transcription**, **CV management**, and **response generation**. Easily extensible for future enhancements like multi-language support or custom prompt engineering.

---

## Requirements

- **Python 3.10+**: Ensure Python is installed on your system.  
- **Groq API Key**: Necessary for transcription and response generation features.  
- **Microphone Access**: For recording audio inputs during interviews or practice sessions.  

---

## Installation

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/Soumedhik/PromptPilot.git 
   cd prompt-pilot  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Environment Setup**:  
   - Add your **Groq API Key** to the `.env` file in the project directory.  

4. **Load Your CV**:  
   - Place your **resume or CV** as a PDF in the same folder as the application (`cv.pdf`). The application will automatically parse and use it for context during response generation.

---

## Usage

1. **Launch the Application**:  
   Run the following command to start:  
   ```bash  
   python app.py  
   ```  

2. **Recording**:  
   - Press **Ctrl+R** to toggle recording on/off.  
   - Audio will be saved temporarily as `recorded_audio.wav` for transcription.  

3. **Transcription and Response Generation**:  
   - Recorded audio is automatically transcribed using **distil-whisper-large-v3-en**, and a response is generated by **LLaMA 3.3**.  
   - Review transcriptions and responses in the transparent window for seamless interaction.  

4. **Ending a Session**:  
   - Press **Q** to exit the application.  

---

## Contributions
Contributions are welcome! If you have suggestions or would like to enhance the application, feel free to submit a pull request or create an issue.

