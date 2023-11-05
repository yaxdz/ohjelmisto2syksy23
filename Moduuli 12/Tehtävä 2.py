import requests



hakussa = input("Anna kaupungin nimi: ")

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakussa}&units=metric&lang=fi&appid=d5617b002ed2b89c33043122a30586b8"
print(pyyntö)

try:
    vastaus = requests.get(pyyntö)

    if vastaus.status_code==200:


        json_vastaus = vastaus.json()

        print(f"Lämpötila: {json_vastaus ['main'] ['temp']}")
        print(f"Säätila: {json_vastaus ['weather'][0] ['main']}")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")

print("Hakutapahtuma on ohi.")


