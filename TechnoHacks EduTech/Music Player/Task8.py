import pygame
import os

# Initialize pygame
pygame.init()

# Create a function to load and play an MP3 file
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Create a function to add songs to a playlist
def create_playlist():
    playlist = []
    while True:
        song = input("Enter the path to an MP3 file or type 'done' to finish: ")
        if song == 'done':
            break
        if os.path.isfile(song) and song.endswith('.mp3'):
            playlist.append(song)
        else:
            print("Invalid file. Please enter a valid MP3 file.")
    return playlist

# Create a function to display the playlist
def display_playlist(playlist):
    print("Current Playlist:")
    for i, song in enumerate(playlist):
        print(f"{i+1}. {os.path.basename(song)}")

# Main music player loop
playlist = []
while True:
    print("\nMusic Player Menu:")
    print("1. Play a song")
    print("2. Create a playlist")
    print("3. View playlist")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        song_path = input("Enter the path to the MP3 file you want to play: ")
        if os.path.isfile(song_path) and song_path.endswith('.mp3'):
            play_music(song_path)
        else:
            print("Invalid file. Please enter a valid MP3 file.")
    
    elif choice == '2':
        new_playlist = create_playlist()
        if new_playlist:
            playlist.extend(new_playlist)
    
    elif choice == '3':
        display_playlist(playlist)
    
    elif choice == '4':
        pygame.mixer.music.stop()
        pygame.quit()
        break
