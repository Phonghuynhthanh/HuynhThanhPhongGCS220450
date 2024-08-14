from library_item import LibraryItem

library = {}
library["01"] = LibraryItem("Shape of You", "Ed Sheeran", "Song", 2017, "ShapeOfYou.mp3", 4)
library["02"] = LibraryItem("Despacito", "Luis Fonsi", "Song", 2017, "Despacito.mp3", 5)
library["03"] = LibraryItem("Uptown Funk", "Mark Ronson", "Song", 2014, "UptownFunk.mp3", 2)
library["04"] = LibraryItem("Blank Space", "Taylor Swift", "Song", 2014, "BlankSpace.mp3", 1)
library["05"] = LibraryItem("Gangnam Style", "Psy", "Song", 2012, "GangnamStyle.mp3", 3)



def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

def get_type(key):
    try:
        item = library[key]
        return item.type
    except KeyError:
        return None

def get_year(key):
    try:
        item = library[key]
        return item.year
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def get_mp3_file(key):
    try:
        item = library[key]
        return item.mp3_file
    except KeyError:
        return None
