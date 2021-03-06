import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "1995", "John Lasseter", "http://www.eggplante.com/wp-content/uploads/2013/09/11-Toy-Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine collides with aliens", "2009", "James Cameron", "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")
odyssey = media.Movie("2001: A Space Odyssey", "A trip in space", "1968", "Stanley Kubrick", "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg","https://www.youtube.com/watch?v=N6ywMnbef6Y")
gunday = media.Movie ("Gunday", "A new Love story", "2014", "Ali Abbas Zafar", "http://upload.wikimedia.org/wikipedia/en/4/46/Gunday_%282013_film%29.jpg", "https://www.youtube.com/watch?v=lFI09rbuHQ8")
xmen = media.Movie ("X-Men: Days of future past", "To save the future they must save the past", "2014", "Bryan Singer", "http://cdn.collider.com/wp-content/uploads/x-men-days-of-future-past-international-poster.jpeg", "https://www.youtube.com/watch?v=pK2zYHWDZKo")
crimson = media.Movie ("Crimson Peak", "50 shades of Crimson", "2015 (upcoming)", "Guillermo del Toro", "http://upload.wikimedia.org/wikipedia/en/c/cf/Crimson_Peak_film_poster.png", "https://www.youtube.com/watch?v=4zBlG8Lv01k")
#print(toy_story.storyline)     
#print(avatar.storyline)
#avatar.show_trailer()
movies = [avatar, odyssey, gunday, toy_story, xmen, crimson]
fresh_tomatoes.open_movies_page(movies)
