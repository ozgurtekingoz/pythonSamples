import requests

url = "http://data.fixer.io/api/latest?access_key=387f9c18535609a7375d8483255583bd"

# birinciDovizCinsi = input("Birinci Doviz Cinsi ")
# ikinciDoviz = input("İkinci Döviz Cinsi")
# miktar = float(input("Miktar: "))

response = requests.get(url)

print(response.json()["rates"]["TRY"])
