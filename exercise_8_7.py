# Exercise 8-7 (Album)
# Write a function called make_album() that builds a dictionary describing music album
# The function should take an artist name and an album title and should return a dictionary
def make_album(artist_name, album_title, tracks = None):
    album= {
        'Artist': artist_name,
        "Album title": album_title
        }
    
    if tracks is not None:
        album['Tracks Number'] = tracks
    return album
    
print(make_album("Rose", "Rosie", 13))
print(make_album("Jennie", "Ruby", 15))
print(make_album("Lisa", "Alter Ego"))