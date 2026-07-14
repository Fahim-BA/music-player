# MP3 Player

Simple command-line MP3 player built with Python and Pygame.

## What it does

- Scans the `mp3/` folder for `.mp3` files.
- Lists the available songs in the terminal.
- Lets you pick a song by number.
- Supports playback commands while a song is playing:
  - `p` pause
  - `r` resume
  - `s` stop
  - `q` quit

## Requirements

- Python 3
- `pygame`
- An `mp3/` folder in the same directory as `main.py`

## Folder Structure

```text
main.py
mp3/
```

## How to Run

1. Open a terminal in the project folder.
2. Install pygame if needed:

   ```bash
   pip install pygame
   ```

3. Run the player:

   ```bash
   python main.py
   ```

## Usage

1. Start the program.
2. Enter the number of the song you want to play.
3. Use the playback commands shown on screen.

## Notes

- The script ignores non-MP3 files.
- If no MP3 files are found, the program exits with a message.
