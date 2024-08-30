# playlist.py

# Step 2: Define the playlist dictionary
playlist = {}

# Step 3: Adding Songs to the Playlist
def add_song(title, artist, genre):
    if title in playlist:
        print(f"The song '{title}' already exists in the playlist.")
    else:
        playlist[title] = {'artist': artist, 'genre': genre}
        print(f"Added '{title}' by {artist} to the playlist.")

# Step 4: Viewing the Playlist
def view_playlist():
    if not playlist:
        print("The playlist is empty.")
    else:
        print("\nCurrent Playlist:")
        for title, details in playlist.items():
            print(f"Title: {title}, Artist: {details['artist']}, Genre: {details['genre']}")
        print()

# Step 5: Updating Song Information
def update_song(title, new_artist=None, new_genre=None):
    if title in playlist:
        if new_artist:
            playlist[title]['artist'] = new_artist
        if new_genre:
            playlist[title]['genre'] = new_genre
        print(f"Updated '{title}' in the playlist.")
    else:
        print(f"The song '{title}' does not exist in the playlist.")

# Step 6: Deleting a Song from the Playlist
def delete_song(title):
    if title in playlist:
        del playlist[title]
        print(f"Deleted '{title}' from the playlist.")
    else:
        print(f"The song '{title}' does not exist in the playlist.")

# Step 7: Testing Your Functions
# Adding songs to the playlist
add_song("Blinded by Your Grace", "Stormzy", "Pop")
add_song("Thank You", "Taiwo Emmanuel", "Gospel")
add_song("Holy Forever", "Cece Winans", "Christian")

# Viewing the playlist
view_playlist()

# Updating a song's artist and genre
update_song("Holy Forever", new_artist="Cece Winans", new_genre="Christian")

# Viewing the updated playlist
view_playlist()

# Deleting a song from the playlist
delete_song("Blinded by Your Grace")

# Viewing the playlist after deletion
view_playlist()

# Attempting to update a non-existent song
update_song("Blinded by Your Grace", new_artist="Stormzy")

# Attempting to delete a non-existent song
delete_song("Blinded by Your Grace")

# Viewing the final playlist
view_playlist()
