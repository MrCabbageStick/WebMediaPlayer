import sqlite3
from typing import Self
from enum import Enum
from datetime import datetime
import bcrypt
from modules.functions import getFormattedTime, debugPrint
from modules.dataclasses.user import User
from modules.dataclasses.movie import Movie
import json


class DatabaseHandlerMessages:
    SUCCESS = "Success"
    CONNECTION_NOT_ESTABLISHED = "Connection not established"
    USER_ALREADY_EXISTS = "User already exists"
    SQLITE_ERROR = "Internal error occured"


class DatabaseHandler:

    connection: sqlite3.Connection = None
    cursor: sqlite3.Cursor = None

    def __init__(self, path: str) -> None:
        
        self.path = path
        print(f"{self.path=}")

    
    def connect(self) -> Self:

        self.connection = sqlite3.connect(self.path, check_same_thread=False)
        self.cursor = self.connection.cursor()

        return self
    
    
    def close(self) -> Self:

        self.connection.close()
        self.connection = None
        self.cursor = None

        return self
    

    def addUser(self, name: str, displayName: str, password: str, isOwner: bool = False) -> tuple[bool, DatabaseHandlerMessages]:
        """Returns a tuple: (success, message)"""

        if not (self.connection and self.cursor):
            return (False, DatabaseHandlerMessages.CONNECTION_NOT_ESTABLISHED)

        if self.cursor.execute(f"SELECT name FROM users WHERE name='{name}'").rowcount > 0:
            return (False, DatabaseHandlerMessages.USER_ALREADY_EXISTS)
        
        password = password.encode()
        password = bcrypt.hashpw(password, bcrypt.gensalt())
        
        try:
            self.cursor.execute(f'INSERT INTO users VALUES (NULL, "{name}", "{displayName}", "{password}", "{getFormattedTime(datetime.now())}", {isOwner})')
            self.connection.commit()

            return (True, "User added succesfully")
        
        except sqlite3.Error as error:
            debugPrint(f"Error: {error}")
            return (False, DatabaseHandlerMessages.SQLITE_ERROR)
        
    
    def getUsers(self) -> tuple[bool, str, list[User]]:
        """Returns a tuple: (success, message, list of users)"""

        if not (self.connection and self.cursor):
            return (False, DatabaseHandlerMessages.CONNECTION_NOT_ESTABLISHED, [])
        
        try:
            return (True, DatabaseHandlerMessages.SUCCESS, [
                User(*userData) for userData in self.cursor.execute("SELECT * FROM users").fetchall()
            ])
        
        except sqlite3.Error as error:
            debugPrint(f"Error: {error}")
            return (False, DatabaseHandlerMessages.SQLITE_ERROR, [])
    
        
    def getMovies(self) -> tuple[bool, str, list[Movie]]:
        """Returns a tuple: (success, message, list of movies)"""

        if not (self.connection and self.cursor):
            return (False, DatabaseHandlerMessages.CONNECTION_NOT_ESTABLISHED, [])
        
        try:
            return (True, DatabaseHandlerMessages.SUCCESS, [
                Movie(*movieData) for movieData in self.cursor.execute("SELECT * FROM movies").fetchall()
            ])
        
        except sqlite3.Error as error:
            debugPrint(f"Error: {error}")
            return (False, DatabaseHandlerMessages.SQLITE_ERROR, [])