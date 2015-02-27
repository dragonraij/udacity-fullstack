#Udacity Full Stack Assessment 1
#Raj Prasad 27/2/14
# Class model for Movies. Stores movie attributes
# has a method to open movie trailer in browser

import webbrowser

class Movie():
    """This Class provides a way to store  movie related documentation"""
    VALID_RATINGS = ["G", "PG-13", "M", "R"]
    def __init__(self, movie_title, movie_storyline, release_year, movie_director, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline= movie_storyline
        self.release_year=release_year
        self.movie_director=movie_director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
