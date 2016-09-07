from urllib2 import urlopen
from json import load

from MovieInfo import MovieInfo


apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

response = urlopen(apiUrl)

json_obj = load(response)

#print json_obj[1]

film = []


for film in json_obj:
	director = film["director"]
	release_year = film["release_year"]
	title = film["title"]
	actor_1 = film["actor_1"]
	actor_2 = film["actor_2"]
	location = location["location"]

	movie = MovieInfo(director, release_year, title, actor_1, actor_2, location)
	
	if film['release_year'] == "2002":
		if film['title'] not in film_2002:

			film_2002.append(film['title'])

		#print film['title']

film = sorted(film)
print film