import requests
url = "https://api.github.com/users/octocat" # замените octotat на свой
response = requests.get(url)
data = response.json()
print(data["name"])
print(data["public_repos"])
print(data["bio"])
print(data["email"])
print(data["id"])