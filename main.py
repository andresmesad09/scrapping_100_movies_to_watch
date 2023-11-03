from pathlib import Path

import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                            "/best-movies-2/")
web_page_content = response.text

soup = BeautifulSoup(web_page_content, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

target_file = Path().cwd() / "100_top_movies.txt"
movie_names = []
for movie in all_movies:
    if ":" in movie.getText():
        movie_name = movie.getText().split(":")[1].strip()
    else:
        movie_name = movie.getText().split(")")[1].strip()
    movie_names.append(movie_name)

with open(target_file, mode="w") as f:
    for index, movie in enumerate(movie_names, start=1):
        f.write(f"{index}) {movie}\n")
