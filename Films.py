import imdb
from imdb import Cinemagoer
import random
from collections import defaultdict
ia = imdb.Cinemagoer()

dict = defaultdict()



def Movie_Search():
    movie_choice = input("Please search for a movie: ")
    movies = ia.search_movie(movie_choice)
    
    
            
    print(f"Searching for {movie_choice}")
    movie_nr = 1
    random.shuffle(movies)
    x=0
    
    for movie in movies[x:4]:
            if movie['kind'] == "movie":
                try:
                    id = movies[movie_nr].movieID
                    movie = ia.get_movie(id)
                    title = movie['title']
                    year = movie['year']
                    rating = movie['rating']
                    genres = movie['genres'][0:2]
                    
                    genres = '/'.join(genres)    
                    for person in movie['directors']:
                        director = person['name']
                    url = movie['full-size cover url']
                    starring = str(movie['cast'][0])+ " & " + str(movie['cast'][1])
                
                
                    dict['string{0}'.format(movie_nr)] = title + " - " + str(year) + " - " + str(genres) + " - " + str(rating) + " - " + url + " - " + str(director) + " - " + str(starring)
                    movie_nr += 1
                    x += 1
                    
                except KeyError: 
                   pass
            else:
                movie_nr -= 0
            
    if 'string1' in dict:
        print(dict['string1'])
    if 'string2' in dict:
        print(dict['string2'])
    if 'string3' in dict:
        print(dict['string3']) 
    if 'string4' in dict:
        print(dict['string4'])
   

    
    
    
    

Movie_Search()