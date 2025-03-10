from linkedin_api import Linkedin
import json 
from pprint import pprint

with open('cred.json', 'r') as f:
    cred = json.load(f)

api = Linkedin(cred["email"], cred["password"])

# TARGET SPECIFIC PROFILES
# print(help(api.get_profile)) for more info on usage

# profile = api.get_profile(public_id="jhonnatan-carvalho")

# headline = profile.get('headline')

# experience = profile.get('experience')

# languages = profile.get('languages')

# experience = profile.get('experience')

# USE SEARCH METHOD
# print(help(api.search_people)) for more info on usage

search_results = api.search_people(keywords='python', limit=10) # cap at 10 profiles

pprint(search_results)