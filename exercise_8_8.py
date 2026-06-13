# Exercise 8-8 (User albums)
# Add while loop to Exercise 8-7 to allow users to enter an album's artist and title
def make_album(artist_name, album_title, tracks):
    album = {
            "Artist name": artist_name,
            "Album title": album_title,
            "Tracks number": tracks
        }
    return album

while True:
    print("\nEnter artist name and his/her album title")
    print("Enter 'q' to quit")

    ar_name = input("Enter artist name: ")
    if ar_name.lower() == 'q':
        break
        
    al_title = input("Enter album title: ")
    if al_title.lower() == 'q':
        break
        
    al_tracks = input("Enter tracks number (or press Enter to skip): ")
    if al_tracks == "q":
        break
    
    print(make_album(ar_name, al_title, al_tracks))
    