import requests
from bs4 import BeautifulSoup

imdbUrl = "https://www.imdb.com/chart/top/"
r = requests.get(imdbUrl)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("table", {"class": "chart full-width"})

body = data[0].find_all_next("tbody", {"class": "lister-list"})

films = body[0].find_all("tr")

for film in films:
    filmBasliklari = film.find_all("td", {"class": ["titleColumn", "ratingColumn imdbRating"]})
    filmIsmi = filmBasliklari[0].text
    filmIsmi = filmIsmi.replace("\n", "")
    filmRating = filmBasliklari[1].text
    filmRating = filmRating.replace("\n", "")
    print(filmIsmi + " " + filmRating)
