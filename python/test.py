from pymongo import MongoClient
import json 
from connectDb import connectDb
from selectCollection import selectCollection
from exercices.filmsFrom1999 import filmsFrom1999
from exercices.comedy import comedy
from exercices.matrix import matrix
from exercices.longMovie import longMovie
from exercices.titleYear import titleYear
from exercices.goodMovie import goodMovie
from exercices.movies90s import movies90s
from exercices.actionSciFi import actionSciFi
from exercices.tomHanks import tomHanks
from exercices.space import space

from exercices2.bestMovies import bestMovies
from exercices2.recentMovies import recentMovies
from exercices2.longComedies import longComedies
from exercices2.moviesByGender import moviesByGender
from exercices2.averageRatingByGender import averageRatingByGender
from exercices2.moreApparitions import moreApparitions
from exercices2.numberImdbVotes import numberImdbVotes
from exercices2.listMovieComents import listMovieComents
from exercices2.comentsByUsers import comentsByUsers

def test_requests():
    db = connectDb('sample_mflix')
    movies_collection = selectCollection(db, 'movies')
    comments_collection = selectCollection(db, 'comments')
    print(movies_collection.count_documents({}))
    print(comments_collection.count_documents({}))

    moviesFrom1999 = filmsFrom1999(movies_collection)
    print('Films from 1999 :',len(moviesFrom1999))

    comedies = comedy(movies_collection)
    print('Comedies :',len(comedies))

    matrix_movies = matrix(movies_collection)
    print('The Matrix movies :',len(matrix_movies))

    long_movies = longMovie(movies_collection)
    print('Movies longer than 2 hours :',len(long_movies))

    titles_years = titleYear(movies_collection)
    #print(titles_years)

    good_movies = goodMovie(movies_collection)
    print('Movies with an IMDB rating greater than 8 :',len(good_movies))

    movies_90s = movies90s(movies_collection) 
    print('Movies from the 90s :',len(movies_90s))

    action_sci_fi_movies = actionSciFi(movies_collection)
    print('Action and Sci-Fi movies :',len(action_sci_fi_movies))

    tom_hanks_movies = tomHanks(movies_collection)
    print('Movies with Tom Hanks :',len(tom_hanks_movies))

    space_movies = space(movies_collection)
    print('Movies with "space" in the plot :',len(space_movies))

    # Exercices 2

    best_movies = bestMovies(movies_collection)
    x = 0
    print("Les 10 meilleurs films: ")
    for movie in best_movies:
        x += 1
        print(x,": ",f"Title: {movie['title']}", f"Rating: {movie['imdb']['rating']}")
    print("\n")
    
    recent_movies = recentMovies(movies_collection)
    y = 0
    print("Les 5 films les plus récents: ")
    for movie in recent_movies:
        y += 1
        print(y,": ",f"Title: {movie['title']}", f"Year: {movie['released']}")
    print("\n")

    long_comedies = longComedies(movies_collection)
    z = 0
    print("Les 5 comédies les plus longues: ")
    for movie in long_comedies:
        z += 1
        print(z,": ",f"Title: {movie['title']}", f"Runtime: {movie['runtime']}")
    print("\n")

    byGender = moviesByGender(movies_collection)
    print("Nombre de films par genre: ")
    for genre in byGender:
        print(f"Genre: {genre['_id']}, Nombre de films: {genre['count']}")
    print("\n")

    avgRatingByGender = averageRatingByGender(movies_collection)
    print("Note moyenne par genre: ")
    for genre in avgRatingByGender:
        print(f"Genre: {genre['_id']}, Note moyenne: {genre['averageRating']}")
    print("\n")

    apparitions = moreApparitions(movies_collection)
    print("Acteurs avec le plus d'apparitions: ")
    for actor in apparitions:
        print(f"Acteur: {actor['_id']}, Nombre d'apparitions: {actor['count']}")
    print("\n")

    votes = numberImdbVotes(movies_collection)
    for movie in votes:
        print(f"{movie['title']} - Votes: {movie['imdb']['votes']}")
    print("\n")

    """movie_comments = listMovieComents(movies_collection, comments_collection)
    for movie in movie_comments:
        print(f"Title: {movie['title']}")
        for comment in movie['comments']:
            print(f" - Comment: {comment['text']}")
    print("\n")"""

    comments_by_users = comentsByUsers(comments_collection)
    for user in comments_by_users:
        print(f"User: {user['name']}, Number of comments: {user['count']}")
        for comment in user['comments']:
            print(f" - Comment: {comment}")
    print("\n")



if __name__ == "__main__":
    test_requests()