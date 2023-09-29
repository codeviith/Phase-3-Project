#!/usr/bin/env python3
# lib/debug.py

# import ipdb
from models.__init__ import CONN, CURSOR
from models.models import Player, Score


# Player.drop_table()
# Score.drop_table()
# Player.create_table()
# Score.create_table()

# player1 = Player.create("Sy")
# player2 = Player.create("Ken")
# score1 = Score.create(1, 1000)
# score2 = Score.create(1, 500)
# score3 = Score.create(2, 750)

###  This score will not save to the database due to the player property in the Score model (class)
# Player # 3 does not exist
# score4 = Score.create(3, 100000)


# ipdb.set_trace()