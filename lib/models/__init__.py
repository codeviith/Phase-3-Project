import sqlite3

CONN = sqlite3.connect('trivia_game.db')
CURSOR = CONN.cursor()
