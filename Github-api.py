import requests
url = "https://api.github.com/users/user" # замените user на свой
response = requests.get(url)
data = response.json
print(data["name"])
print(data["public_repos"])
