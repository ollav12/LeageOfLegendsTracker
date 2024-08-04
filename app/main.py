import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")
##database_url = os.getenv("DATABASE_URL")

app = FastAPI()

# Mount the static directory to serve CSS, JS, and images
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup for templating
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)