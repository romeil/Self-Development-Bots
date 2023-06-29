import requests
import json

def get_quote():
   response = requests.get("https://zenquotes.io/api/random")
   json_data = json.loads(response.text)
   quote = json_data[0]["q"] + " - {0}".format(json_data[0]["a"])
   return quote

