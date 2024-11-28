import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
movies = []

response = requests.get(URL)

if response.status_code == 200:

    yc_web_page = response.text
    soup = BeautifulSoup(yc_web_page, 'html.parser')
    all_movies = soup.find_all("h3", class_="title")

    for movie in all_movies:
        film = movie.getText()
        movies.append(film)

    with open("100 movies.txt", "w") as file:
        for i in range(len(movies) - 1, -1, -1):
            file.write(movies[i] + "\n")
