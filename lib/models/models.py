from models.__init__ import CONN, CURSOR

### PLAYER MODEL ###
class Player:

    all = []

    def __init__(self, username):
        self.id = None
        self.username = username
        self.scores_list = []

    def __repr__(self):
        return f'Player {self.id}: {self.username}'

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                username TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS players
        """

        CURSOR.execute(sql)
        
        cls.all = []

    @classmethod
    def new_data_from_db(cls, row):
        player = cls(row[1])
        player.id = row[0]
        return player
    

### CRUD
# Read
    # Get player usernames
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM players
        """

        all = CURSOR.execute(sql).fetchall()
        
        cls.all = [cls.new_data_from_db(row) for row in all]

        return cls.all


    # Find players by ID
    @classmethod
    def find_by_id(cls, id):
        players = [player for player in Player.all if player.id == id]

        if len(players) > 0:
            return players[0]
        else:
            return None


# Create
    # Create new player
    @classmethod
    def create(cls, username):
        player = Player(username)
        player.save()
        return player
    
    def save(self):
        sql = """
            INSERT INTO players (username)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.username,))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM players").fetchone()[0]
        CONN.commit()
        Player.all.append(self)


# Update
    # Update a player
    def update(self):
        sql = """
            UPDATE players
            SET username = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.id))
        CONN.commit()


# Delete
    # Delete a player
    def delete(self):
        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        # Remove the player instance from Player.all
        Player.all = [player for player in Player.all if player.id != self.id]

        # Delete the associated reviews from the database and remove the associated review instances from Review.all
        # The idea here is that there should not exist reviews for a player that no longer exists
        for score in self.scores_list:
            score.delete()



### SCORE MODEL ###
class Score:

    all = []

    def __init__(self, player_id, value):
        self.player_id = player_id
        self.player = Player.find_by_id(player_id)
        self.player.scores_list.append(self)
        self.value = value

    def __repr__(self):
        return f'{self.player}, has a score of: {self.value}'
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception("Error: Player not found!")        

### CRUD
# Create
    # Create new score
    @classmethod
    def create(cls, player_id, value):
        score = cls(player_id, value)
        score.save()
        cls.all.append(score)
        return score
    
    def save(self):
        sql = """
            INSERT INTO scores (player_id, value)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.player_id, self.value))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM scores").fetchone()[0]
        CONN.commit()

    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                player_id INTEGER,
                value FLOAT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS scores
        """

        CURSOR.execute(sql)
        
        cls.all = []


# Read
    # Get score values
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM scores
        """

        all = CURSOR.execute(sql).fetchall()
        
        cls.all = [cls.new_data_from_db(row) for row in all]

        return cls.all

# Update
    # Update a score
    def update(self):
        sql = """
            UPDATE scores
            SET value = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.value, self.id) )
        CONN.commit()

# Delete
    # Delete a score
    def delete(self):
        sql = """
            DELETE from scores
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Score.all = [score for score in Score.all if score.id != self.id]
        
    
    @classmethod
    def new_data_from_db(cls, row):
        score = cls(row[1], row[2])
        score.id = row[0]
        return score

