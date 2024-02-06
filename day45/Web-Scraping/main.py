import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")[::-1]
# print(movies)
movie_names = [name.getText() for name in movies]
# for name in movies:
#     names = name.getText()
#     movie_names.append(names)

print(movie_names[0])
print(len(movie_names))

with open("movies.txt", "w") as file:
    for movie in movie_names:
        file.write(movie + "\n")