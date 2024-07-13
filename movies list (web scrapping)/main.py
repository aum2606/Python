import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html,"html.parser")
movies = soup.find_all(name="h3", class_="title")

print(movies)
movie_titles = [movie.getText() for movie in movies]
movies_list = movie_titles[::-1]

with open("movies.txt",mode="w", encoding="utf8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")