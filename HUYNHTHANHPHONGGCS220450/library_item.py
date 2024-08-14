class LibraryItem:
    def __init__(self, name, director, type, year, mp3_file, rating=0):
        self.name = name
        self.director = director
        self.type = type
        self.year = year
        self.rating = rating
        self.play_count = 0
        self.mp3_file = mp3_file  # New attribute for the MP3 file

    def info(self):
        return f"{self.name} ({self.type}, {self.year}) - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
