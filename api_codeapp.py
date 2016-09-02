from urllib2 import urlopen
from json import load

apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

response = urlopen(apiUrl)

json_obj = load(response)

#print json_obj[1]

film_2002 = []

for film in json_obj:
	if film['release_year'] == "2002":
		if film['title'] not in film_2002:

			film_2002.append(film['title'])

		#print film['title']

film_2002 = sorted(film_2002)
print film_2002
