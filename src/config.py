import os

from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

load_dotenv()


class GlobalConfig:
    ENV: str = os.getenv("ENV", "default")
    DEBUG: bool = os.getenv("DEBUG", "false") == "true"
    assert isinstance(DEBUG, bool)

    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    TRANSLATE_MODEL = "gpt-4-1106-preview"
