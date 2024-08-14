import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import pygame
from video_library import get_name, get_mp3_file, increment_play_count  # Importing functions to retrieve video info and increment play count

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, content)

class CreateVideoList:
    def __init__(self, window):
        self.sound_player = pygame.mixer
        self.sound_player.init()
        window.geometry("800x400")
        window.title("Create Video Playlist")

        self.playlist = []
        self.mp3_files = []
        self.current_index = 0

        # Top row: Add video and input field
        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Key")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Second row: Playlist text area
        self.playlist_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Third row: Control buttons (Play, Stop, Reset)
        play_btn = tk.Button(window, text="Play", command=self.play_selected_song)
        play_btn.grid(row=2, column=0, padx=10, pady=10)

        stop_btn = tk.Button(window, text="Stop", command=self.stop_sound)
        stop_btn.grid(row=2, column=1, padx=10, pady=10)

        reset_playlist_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_playlist_btn.grid(row=2, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.is_playing = False

    def add_video_clicked(self):
        key = self.input_txt.get()
        name = get_name(key)  # Get the video name using the key
        mp3_file = get_mp3_file(key)  # Get the MP3 file path using the key

        if name is not None and mp3_file is not None:
            self.playlist.append((key, name))
            self.mp3_files.append(mp3_file)
            playlist_str = "\n".join([name for _, name in self.playlist])
            set_text(self.playlist_txt, playlist_str)
            self.status_lbl.configure(text=f"Added {name} to the playlist.")
        else:
            self.status_lbl.configure(text=f"Video with key {key} not found.")

    def play_selected_song(self):
        selected_text = self.playlist_txt.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
        for index, (_, name) in enumerate(self.playlist):
            if name == selected_text:
                self.current_index = index
                self.play_sound()
                self.status_lbl.configure(text=f"Playing {name}...")
                self.is_playing = True
                break
        else:
            self.status_lbl.configure(text="Please select a song from the playlist.")

    def play_sound(self):
        if self.mp3_files and self.current_index < len(self.mp3_files):
            current_key, current_name = self.playlist[self.current_index]
            current_song = self.mp3_files[self.current_index]  # Get the MP3 file path

            # Increment the play count for the current video
            increment_play_count(current_key)

            self.sound_player.music.load(current_song)
            self.sound_player.music.play()

            # Use pygame's event system to trigger the next song after the current one finishes
            self.sound_player.music.set_endevent(pygame.USEREVENT)
            window.bind("<USEREVENT>", lambda event: self.play_next_song())
        else:
            self.status_lbl.configure(text="No songs in the playlist or invalid selection.")

    def play_next_song(self):
        self.current_index += 1
        if self.current_index < len(self.mp3_files):
            self.play_sound()
        else:
            self.status_lbl.configure(text="Finished playing the playlist.")
            self.is_playing = False

    def stop_sound(self):
        self.sound_player.music.stop()
        self.is_playing = False
        self.status_lbl.configure(text="Stopped the playback.")

    def reset_playlist_clicked(self):
        self.playlist = []
        self.mp3_files = []
        set_text(self.playlist_txt, "")
        self.status_lbl.configure(text="Playlist has been reset.")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()
