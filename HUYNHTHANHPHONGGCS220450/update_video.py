import tkinter as tk
import tkinter.scrolledtext as tkst
from video_library import get_name, get_rating, set_rating, get_play_count

class UpdateVideos:
    def __init__(self, window):
        window.geometry("600x250")
        window.title("Update Video Rating")

        # Label and Entry for Video Number
        video_number_lbl = tk.Label(window, text="Enter Video Number:")
        video_number_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.video_number_entry = tk.Entry(window, width=10)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for New Rating
        new_rating_lbl = tk.Label(window, text="Enter New Rating (1-5):")
        new_rating_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.new_rating_entry = tk.Entry(window, width=10)
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to Update Rating
        update_btn = tk.Button(window, text="Update Rating", command=self.update_rating_clicked)
        update_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # ScrolledText widget to display the update information
        self.text_area = tkst.ScrolledText(window, width=40, height=10)
        self.text_area.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

        # Label to Display the Status (optional)
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def update_rating_clicked(self):
        video_number = self.video_number_entry.get()
        try:
            new_rating = int(self.new_rating_entry.get())
        except ValueError:
            self.status_lbl.configure(text="Please enter a valid rating (1-5).")
            return

        if new_rating < 1 or new_rating > 5:
            self.status_lbl.configure(text="Please enter a valid rating (1-5).")
            return

        # Get the video name and current rating
        video_name = get_name(video_number)
        if video_name is not None:
            # Update the rating
            set_rating(video_number, new_rating)

            # Get the updated rating and play count
            updated_rating = get_rating(video_number)
            play_count = get_play_count(video_number)

            # Display the video name, new rating, and play count in the ScrolledText widget
            self.text_area.insert(tk.END, f"{video_name}: Rating = {updated_rating}, Play Count = {play_count}\n")
            self.status_lbl.configure(text=f"Updated {video_name} successfully.")
        else:
            # Display an error message if the video number is not valid
            self.status_lbl.configure(text=f"Video with number {video_number} not found.")

if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideos(window)
    window.mainloop()