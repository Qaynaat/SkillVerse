"""
==========================================
SkillVerse Database Manager
Version : 0.2
==========================================
"""

import sqlite3
from datetime import datetime
from config import DATABASE_PATH


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.create_default_user()

    def create_tables(self):

        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    dream TEXT,

    deadline INTEGER,

    reward TEXT,

    study_days TEXT,

    roadmap TEXT,

    xp INTEGER DEFAULT 0,

    lifetime_xp INTEGER DEFAULT 0,

    coins INTEGER DEFAULT 0,

    streak INTEGER DEFAULT 0,

    portal_keys INTEGER DEFAULT 0,

    certificates INTEGER DEFAULT 0

)
""")
        self.connection.commit()

    # -----------------------------
    # Create User
    # -----------------------------

    def create_user(self, username):

        self.cursor.execute("""

        INSERT INTO users
        (username, created_at)

        VALUES (?,?)

        """, (username, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        self.connection.commit()

    # -----------------------------
    # Get User
    # -----------------------------

    def get_user(self):

        self.cursor.execute("""

        SELECT * FROM users LIMIT 1

        """)

        return self.cursor.fetchone()
    def update_user(self,
                username,
                dream,
                deadline,
                reward,
                study_days,
                roadmap):

        self.cursor.execute("""

    UPDATE users

    SET

    username=?,
    dream=?,
    deadline=?,
    reward=?,
    study_days=?,
    roadmap=?

    WHERE id=1

    """,

    (

    username,
    dream,
    deadline,
    reward,
    study_days,
    roadmap

    ))

        self.connection.commit()
    def create_default_user(self):

        self.cursor.execute("""

    INSERT OR IGNORE INTO users

    (

    id,
    username

    )

    VALUES

    (

    1,

    ''

    )

    """)

        self.connection.commit()

    def close(self):
        self.connection.close()