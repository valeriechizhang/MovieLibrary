import webbrowser
import fresh_tomatoes
import requests


API_KEY = "api_key=771dea820715b51ce9fc3fe99886d731"
REQUEST_ADDR = "/3/movie/"

class Movie(): 

	def __init__(self, movie_title, image, trailer, movie_id):
		self.title = movie_title
		self.poster_image_url = image;
		self.trailer_youtube_url = trailer;
		self.movie_id = movie_id;

	# request more information of the movie from themoviedb API
	def getDetail(self, request_addr, api_key):
		request = "https://api.themoviedb.org/3/movie/" + self.movie_id + "?" + api_key
		r = requests.get(request)
		res = r.json()
		self.genre = res["genres"][0]["name"]
		self.release_year = res["release_date"][0:4]
		self.tagline = res["tagline"]


# movie entries
goodWillHunting = Movie("Good Will Hunting", 
						"https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",
						"https://youtu.be/PaZVjZEFkRs",
						"tt0119217")

blackSwan = Movie("Black Swan",
				  "https://images-na.ssl-images-amazon.com/images/M/MV5BNzY2NzI4OTE5MF5BMl5BanBnXkFtZTcwMjMyNDY4Mw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
				  "https://youtu.be/5jaI1XOB-bs",
				  "tt0947798")

fightClub = Movie("Fight Club",
				  "https://images-na.ssl-images-amazon.com/images/M/MV5BMzc1YmU2ZjEtYWIwMC00ZjM3LWI0NTctMDVlNGQ3YmYwMzE5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY999_CR0,0,704,999_AL_.jpg",
				  "https://youtu.be/BdJKm16Co6M",
				  "tt0137523")

walle = Movie("WALL·E",
			  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
			  "https://youtu.be/alIq_wG9FNk",
			  "tt0910970")

theLionKing = Movie("The Lion King",
					"https://images-na.ssl-images-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
					"https://youtu.be/4sj1MT05lAA",
					"tt0110357")


movies = [theLionKing, walle, fightClub, goodWillHunting, blackSwan]

# get the details from each movie
for movie in movies:
	movie.getDetail(REQUEST_ADDR, API_KEY);


# generate the webpage
fresh_tomatoes.open_movies_page(movies)

