import argparse
import json
from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.youtube import download_audio_from_url, is_youtube_link

app = FastAPI()


# Define a Pydantic model for request body validation
class InputModel(BaseModel):
    source: Union[str, None] = None


# Dummy function to simulate processing and generate a large JSON output
def process_input(source: str) -> dict:
    # In a real application, you would have logic here to process the URL or file
    # For demonstration, we'll just return a large JSON object
    large_json = {"data": [{"id": i, "value": f"Item {i}"} for i in range(1000)]}
    return large_json


# FastAPI endpoint
@app.post("/transcribe/")
async def transcribe_endpoint(input_model: InputModel):
    if input_model.source:
        result = process_input(input_model.source)
        return result
    else:
        raise HTTPException(status_code=400, detail="No source provided")


# CLI functionality
def cli():
    parser = argparse.ArgumentParser(description="Transcribe a URL or file and output JSON.")
    parser.add_argument("source", type=str, help="The URL or filename to transcribe")
    args = parser.parse_args()

    source = args.source
    if is_youtube_link(args.source):
        print("Downloading audio from YouTube...")
        source, _ = download_audio_from_url(args.source)

    result = process_input(source)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # If arguments are provided, use CLI mode
        cli()
    else:
        # Otherwise, start the FastAPI server
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=8000)
