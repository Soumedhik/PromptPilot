import os
import wave
import time
import pyaudio
import audioop
import PyPDF2
from groq import Groq

class GenerateResponse:
    def __init__(self, api_key, model="llama-3.3-70b-versatile", temperature=1, max_tokens=1024, top_p=1):
        self.client = Groq(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p

    @staticmethod
    def extract_text_from_pdf(pdf_path):
        """Extracts text content from a PDF file."""
        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                return "".join(page.extract_text() for page in reader.pages)
        except Exception as e:
            return f"Error reading PDF: {e}"

    @staticmethod
    def chunk_text(text, chunk_size=500):
        """Chunks text into smaller pieces for processing."""
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def generate_response(self, user_query, cv_chunks, conversation_history):
        """Generates a response based on the user's query, CV chunks, and conversation history."""
        system_message = {
            "role": "system",
            "content": 

"You are an advanced interview assistant AI that simulates a knowledgeable "
                "and professional candidate in a job interview. Your goal is to provide "
                "detailed, accurate, and well-articulated answers to the interviewer’s questions. "
                "You are representing a candidate with the following CV details."
                "\n\n"
                "You have access to the CV text provided below. Use this information to craft "
                "personalized answers for all questions related to the candidate's background, "
                "education, technical skills, projects, achievements, and experiences. You may also "
                "generate relevant examples or expand on the provided details when required."
                "\n\n"
                "In addition to CV details, use your general knowledge about common interview questions, "
                "industry practices, and professional etiquette to formulate responses that demonstrate "
                "competence, confidence, and expertise. Tailor your answers for each query and provide "
                "insights as if you were the candidate."
                "\n\n"
                "The questions may range from personal introductions, technical challenges, behavioral "
                "questions, and situational problems to industry-specific topics. Always ensure your "
                "answers are clear, concise, and relevant to the question asked."
                "\n\n"
                "When the interviewer asks non-CV-related questions (e.g., hypothetical scenarios, general knowledge, "
                "or domain-specific topics), answer based on your understanding of industry best practices and professional principles."
        }

        # Create the messages array with system message and CV chunks
        messages = [system_message]
        messages.extend({"role": "user", "content": chunk} for chunk in cv_chunks)
        
        # Add conversation history
        messages.extend(conversation_history[-10:])  # Keep last 10 exchanges to stay within context window
        
        # Add current query
        messages.append({"role": "user", "content": user_query})

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stream=True,
            )
            return "".join(chunk.choices[0].delta.content or "" for chunk in completion).strip()
        except Exception as e:
            return f"Error during response generation: {e}"

