import webbrowser

class Movie():
    """This Class provides a way to store  movie related documentation"""
    VALID_RATINGS = ["G", "PG-13", "M", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline= movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # TODO: write code...
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
