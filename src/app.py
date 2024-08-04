import os
from dotenv import load_dotenv
from flask import Flask, Request, render_template
import requests

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")
##database_url = os.getenv("DATABASE_URL")

################################
# Set up app
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,   
    template_folder=os.path.join(APP_PATH, "src/templates"),
    static_folder=os.path.join(APP_PATH, "src/static"),
)


@app.get("/")
@app.get("/index.html")
def index_html():
    """Render the home page"""
    return render_template("index.html")