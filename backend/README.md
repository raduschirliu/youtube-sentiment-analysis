Backend REST API for the youtube-sentiment-analysis project, built using Python, Flask, TextBlob/NLTK, Redis, and Google's YouTube Data APAI.

## Building and Running
To build and run the backend, first clone the repo and change into the backend folder
```bash
git clone git@github.com:raduschirliu/youtube-sentiment-analysis.git
cd youtube-sentiment-analysis/backend
```

set the neccesary environment variables (either globally or in a `.env` file in the `backend/` folder)
```bash
# YouTube API key
API_KEY=api-key-here
REDIS_URL=redis://url-here
```

create a virtual environment and install dependencies through pip
```bash
python -m venv .venv
pip install -r requirements.txt
```

Then, it can be started in development mode by running the `start.sh` script
```bash
./start.sh
```