import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

app = FastAPI()

@app.get("/")
def read_root():
    return {"API_KEY": api_key, "DATABASE_URL": database_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)