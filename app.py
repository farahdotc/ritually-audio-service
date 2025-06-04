from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
import boto3
import uuid
import io

app = FastAPI()

# AWS Polly configuration
polly = boto3.client("polly", region_name="us-east-1")

class RitualRequest(BaseModel):
    text: str

@app.post("/get-ritual-audio")
async def get_ritual_audio(data: RitualRequest):
    try:
        # Wrap text in SSML to slow the speed slightly
        ssml_text = f"<speak><prosody rate='90%'>{data.text}</prosody></speak>"
        # ssml_text = f"<speak>{data.text}</speak>"

        response = polly.synthesize_speech(
            OutputFormat="mp3",
            Text=ssml_text,
            VoiceId="Emma",
            Engine="neural",
            SampleRate="24000", 
            TextType="ssml"
        )

        # Polly returns a streaming object
        audio_stream = response.get("AudioStream")
        if audio_stream is None:
            return JSONResponse(content={"error": "No audio stream returned"}, status_code=500)

        return StreamingResponse(audio_stream, media_type="audio/mpeg")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
