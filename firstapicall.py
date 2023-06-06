import requests

# Set up the necessary variables
access_token = 'EAAHWIeUsTdABAHK6teMwAY7A04u5nc7L2xhReJbXidQ5ZA0wvSUGkaI2ltzk7LX3R5IyzSE4gFEJ2VwcLiQYoaKW7QIBy9kTiI1FZAZCwMLFLYihYB5opp13ZABYKs5MCZCZBDihJrjqedQj2AmU8ZCodHkIE4LrDYw4Xpwizjq61AsuZBsplZChp0WCWpQPKyT7vYfSGlTBqjtZCVhOP0BnU3Ar0ZC1gUWZBJuRFrkI63Ce67ZAYzAkaFbYr'
endpoint = 'https://graph.instagram.com/v17.0/me'

# Set the parameters for the API request
params = {
    'fields': 'id,username',
    'access_token': access_token
}

url = endpoint + '?fields=id%2Cname&access_token='+access_token

# Make the API request
response = requests.get(url)

# Check the response status and print the retrieved data
if response.status_code == 200:
    data = response.json()
    print('User ID:', data['id'])
    print('Username:', data['name'])
else:
    print('Error occurred:')