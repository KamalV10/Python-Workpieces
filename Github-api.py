import requests
url = "https://api.github.com/users/KamalV10" # замените KamalV10 на свой
response = requests.get(url)
data = response.json()
print(data["name"])
print(data["public_repos"])