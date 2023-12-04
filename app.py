import asyncio

import openai
import streamlit as st

from src.config import GlobalConfig

openai.api_key = GlobalConfig.OPENAI_API_KEY

DEBUG = False


async def main():
    st.set_page_config(layout="wide")
    st.title("Template Project App")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(main())
