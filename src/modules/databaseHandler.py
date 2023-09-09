import sqlite3
from typing import Self
from enum import Enum
from datetime import datetime
import bcrypt
from modules.functions import getFormattedTime, debugPrint
from modules.dataclasses.user import User
from modules.dataclasses.movie import Movie
import json
from typing import Callable



def SQLExecFunction(emptyReturn = None):

    def inner(method: Callable):

        def wrapper(self, *args, **kwargs):

            if not (self.connection and self.cursor):
                return (False, DatabaseHandlerMessages.CONNECTION_NOT_ESTABLISHED, emptyReturn) \
                    if emptyReturn is not None \
                        else (False, DatabaseHandlerMessages.CONNECTION_NOT_ESTABLISHED)

            try:
                if(emptyReturn is not None):
                    return (True, DatabaseHandlerMessages.SUCCESS, method(self, *args, **kwargs))
                
                method(self, *args, **kwargs)
                return (True, DatabaseHandlerMessages.SUCCESS)
            
            except sqlite3.Error as error:
                debugPrint(f"Error: {error}")
                return (False, DatabaseHandlerMessages.SQLITE_ERROR, []) \
                    if emptyReturn is not None \
                        else (False, DatabaseHandlerMessages.SQLITE_ERROR)
         
        return wrapper
    
    return inner


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
    

    @SQLExecFunction()
    def addUser(self, name: str, displayName: str, password: str, isOwner: bool = False):
        self.cursor.execute(f'INSERT INTO users VALUES (NULL, "{name}", "{displayName}", "{password}", "{getFormattedTime(datetime.now())}", {isOwner})')
        self.connection.commit()
        

    @SQLExecFunction(emptyReturn=[])
    def getUsers(self) -> list[User]:
        return [User(*userData) for userData in self.cursor.execute("SELECT * FROM users").fetchall()]
    

    @SQLExecFunction(emptyReturn=[])
    def getMovies(self) -> list[Movie]:
        return [Movie(*movieData) for movieData in self.cursor.execute("SELECT * FROM movies").fetchall()]
        

    @SQLExecFunction()
    def addMovie(self, title: str, path: str, thumbnailPath: str, duration: int):
        self.cursor.execute(f'INSERT INTO movies VALUES (NULL, "{title}", "{path}", "{thumbnailPath}", {duration})')
        self.connection.commit()



    