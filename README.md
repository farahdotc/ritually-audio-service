Ritually Audio Service

The Ritually Audio Service is a FastAPI-based backend that powers the audio generation feature of the Ritually iOS app. It uses Amazon Polly to convert customized wellness ritual text into high-quality spoken audio.
Overview

Ritually helps users practice emotional well-being through personalized, guided rituals. The audio service takes in user-generated text and responds with an audio file that the app plays for the user. This backend is a core part of the Ritually experience, enabling a seamless voice-guided flow.
How It Works

Accepts a POST request containing ritual text in JSON format.
Uses AWS Polly to synthesize the text into speech (MP3).
Returns the generated audio file as a downloadable response.
Deployed using Render at:
https://ritually-audio-service.onrender.com/get-ritual-audio
Technologies Used

Python 3
FastAPI
Uvicorn
Boto3 (Amazon Polly)
Render for deployment
Example Request

POST /get-ritual-audio
Content-Type: application/json

{
  "text": "Welcome to your ritual. Take a deep breath and begin."
}
Setup Instructions

Clone this repository.
Create a virtual environment and activate it.
Install dependencies:
pip install -r requirements.txt
Create a .env file and add your AWS credentials:
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
Run the server:
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
Support

This repository serves as the support and documentation site for the backend service. If you are experiencing issues with audio in the Ritually app, please contact the developer via GitHub or raise an issue on this repository.
