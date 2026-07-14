import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

def play_music(folder, song):

    file_path = os.path.join(folder, song)

    if not os.path.exists(file_path):
        print(f"The file '{song}' does not exist in the folder .")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song}")
    print("Commands: 'p' to pause, 'r' to resume, 's' to stop, 'q' to quit")

    while True:
        command = input(">").lower()

        if command == 'p':
            pygame.mixer.music.pause()
            print("Music paused.")
        elif command == 'r':
            pygame.mixer.music.unpause()
            print("Music resumed.")
        elif command == 's':
            pygame.mixer.music.stop()
            print("Music stopped.")
            return
        elif command == 'q':
            pygame.mixer.music.stop()
            print("Exiting the MP3 player.")
            exit()
        else:
            print("Invalid command. Please use 'p', 'r', 's', or 'q'.")

def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Error initializing the mixer:", e)
        return
    
    folder = "mp3"  

    if not os.path.isdir(folder):
        print(f"The folder '{folder}' does not exist.")
        return
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith('.mp3')]

    if not mp3_files:
        print(f"No MP3 files found in the folder '{folder}'.")
        
    while True:
        print("====>MP3 Player<====")
        print("My songs:")

        for index, song in enumerate(mp3_files,start=1):
            print(f"{index}. {song}")
        
        choice_input = input("\nEnter the number of the song you want to play (or 'q' to quit):")

        if choice_input.lower() == 'q':
            print("Exiting the MP3 player.")
            break

        if not choice_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        
        choice = int(choice_input)-1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice. Please select a valid song number.")
            
if __name__ == "__main__":
    main()