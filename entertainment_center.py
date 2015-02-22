import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://www.eggplante.com/wp-content/uploads/2013/09/11-Toy-Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine collides with aliens", "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")
odyssey = media.Movie("2001: A Space Odyssey", "A trip in space", "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg","https://www.youtube.com/watch?v=N6ywMnbef6Y")
#print(toy_story.storyline)     
#print(avatar.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
