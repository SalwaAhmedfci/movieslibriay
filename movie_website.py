import media
import fresh_tomatoes

toystory = media.Movie("Toy Story","Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("avatar","On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
angrybirds = media.Movie("angry birds","Flightless birds lead a mostly happy existence, except for Red (Jason Sudeikis), who just can't get past the daily annoyances of life. His temperament leads him to anger management class, where he meets fellow misfits Chuck (Josh Gad) and Bomb. Red becomes even more agitated when his feathered brethren welcome green pigs to their island paradise. As the swine begin to get under his skin, Red joins forces with Chuck and Bomb to investigate the real reason behind their mysterious arrival.","https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=QRmKa7vvct4")
Tangled = media.Movie("Tangled","FWhen the kingdom's most-wanted bandit, Flynn Rider (Zachary Levi), hides in a convenient tower, he immediately becomes a captive of Rapunzel (Mandy Moore), the spire's longtime resident. Crowned with 70 feet of magical golden hair, she has been locked away for years and desperately wants freedom. The feisty teenager strikes a deal with Flynn, and together they begin a whirlwind adventure.","https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Tangled_poster.jpg/220px-Tangled_poster.jpg","https://www.youtube.com/watch?v=ip_0CFKTO9E")
#print(angrybirds.poster_image_url)
#print(avatar.poster_image_url)
#print(toystory.poster_image_url)
#angrybirds.show_trailer()
#toystory.show_trailer()
#avatar.show_trailer()
#angrybirds.show_trailer()
#Tangled.show_trailer()
#movies = [toystory , avatar , angrybirds , Tangled]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__name__)
print (media.Movie.__module__)
