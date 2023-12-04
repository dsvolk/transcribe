FROM python:3.10-slim

LABEL maintainer="Denis Volk <the.denis.volk@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# Copy the rest of the application code into the container at /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app
COPY . /app

# Install requirements
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m unidic download

EXPOSE 8501

# Copy the value from STREAMLIT_PASSWORD environment variable into the container at /.streamlit/secrets.toml
ARG STREAMLIT_PASSWORD
ENV STREAMLIT_PASSWORD=$STREAMLIT_PASSWORD
RUN echo "password = \"${STREAMLIT_PASSWORD}\"" > /app/.streamlit/secrets.toml

# Run the command to start the bot
CMD "streamlit run app.py"