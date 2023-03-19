import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Song:
    def __init__(self, name, duration_in_seconds, artist, genre, album):
        self.name = name
        self.duration_in_seconds = duration_in_seconds
        self.artist = artist
        self.genre = genre 
        self.album = album

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"| {self.name} | {self.duration_in_seconds} | {self.artist} | {self.genre} | {self.album} |"
song1 = Song("38 special", 198, 'juice wrld', 'unkown', 'unreleased')
song2 = Song("FTL", 220, 'juice wrld', 'unknown', 'unreleased')
song3 = Song("Bad Habit", 233, 'Steve Lacy', 'R&B/Soul', 'single')

print(song1)


#task 4 ('supercharge your classes')
#MyWidget class inherits from the super() class