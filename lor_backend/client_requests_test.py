import requests
import sys

base_url = "http://localhost:8000"
endpoint_url = "/champion/"
champion_id = sys.argv[1] if len(sys.argv) > 1 else 1

ban_list = [i for i in range(1, 500)]
params = {"ids": ban_list}

response = requests.get(
    f"{base_url}{endpoint_url}{champion_id}", params=params)

if response.status_code == 200:
    print("Champion data:")
    print(response.json())
elif response.status_code == 201:
    print("New champion data created:")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
