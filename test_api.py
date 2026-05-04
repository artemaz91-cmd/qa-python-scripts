import requests

url = "https://httpbin.org/get"
response = requests.get(url, verify=False)

print("Статус:", response.status_code)

if response.status_code == 200:
    print("✅ Тест пройден")
else:
    print("❌ Ошибка:", response.status_code)
