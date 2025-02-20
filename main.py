from linkedin_api import Linkedin

api = Linkedin("email", "password")

profile = api.get_profile(public_id="jhonnatan-carvalho")


headline = profile.get('headline')

experience = profile.get('experience')

languages = profile.get('languages')

experience = profile.get('experience')
