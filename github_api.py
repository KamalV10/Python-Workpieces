import requests
url = "https://api.github.com/users/octocat" # замените octotat (оффициальный аккаунт GitHub) на свой
response = requests.get(url) # сохраняем функцию в переменную
data = response.json() # сохраняем в переменную ссылку на json
print(data["name"]) # написать в консоль имя аккаунта
print(data["public_repos"]) # написать в консоль количество публичных репозиториев
print(data["bio"]) # написать в консоль описаник аккаунта
print(data["email"]) # написать в консоль email аккаунта
print(data["id"]) # написать в консоль id аккаунта