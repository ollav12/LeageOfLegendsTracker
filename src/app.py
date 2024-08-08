import os
from dotenv import load_dotenv
from flask import Flask, Request, render_template, jsonify
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
def front_page():
    """Render the front page for this application"""
    return render_template("index.html")

@app.route("/summoners/<region>/<username>-<tag>")
def get_summoners_region_username_tag(region, username, tag):

    new_region = get_region(region)

    # Get account id
    api_url1 = f"https://{new_region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tag}?api_key={api_key}"
    response1 = requests.get(api_url1)
    data1 = response1.json()

    puuid = data1.get("puuid")

    # Get summoner account
    api_url2 = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}"
    response2 = requests.get(api_url2)
    data2 = response2.json()

    id = data2.get("id")

    # Get summoner ranked data
    api_url3 = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={api_key}"
    response3 = requests.get(api_url3)
    data3 = response3.json()

    # Get list of match ids
    api_url4 = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={api_key}"
    response4 = requests.get(api_url4)
    data4 = response4.json()

    match_id = data4[0]

    # Get specific match data
    api_url5 = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    response5 = requests.get(api_url5)
    data5 = response5.json()

    combined_data = {
        "account data": data1,
        "summoner account data": data2,
        "summoner ranked data": data3,
        "summoner match ids": data4,
        "summoner specific match": data5
    }

    return jsonify(combined_data)

@app.route("/summoners/<region>/<username>-<tag>/champions")
def get_summoners_region_username_tag_champions():
    return 0

@app.route("/summoners/<region>/<username>-<tag>/mastery")
def get_summoners_region_username_tag_mastery():
    return 0

@app.route("/summoners/<region>/<username>-<tag>/ingame")
def get_summoners_region_username_tag_ingame():
    return 0



def get_region(region):
    if(region == "euw"):
        return "europe"
    elif(region == "na"):
        return "america"
    else:
        print("region does not exist: " + region)