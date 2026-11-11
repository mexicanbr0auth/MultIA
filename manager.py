import requests
import json

with open("endpoints.json", "r") as file:
    api = json.load(file)

select = input("Selecione O Provedor: ")

if select in api:
    print(f"API SELECIONADA: {api[select]}")

    credentials = True

    if credentials:
        api_key = input("API KEY: ")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": "Olá! Responda em português."
                }
            ],
            "temperature": 0.7
        }

        response = requests.post(
            api[select],
            headers=headers,
            json=payload
        )

        print("STATUS:", response.status_code)
        print(response.text)

else:
    print("Provedor Não Encontrado")
