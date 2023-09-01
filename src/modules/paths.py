import os

MAIN = "/".join(os.path.dirname(__file__).split("/")[:-1])

DATABASE = f"{MAIN}/database/web_player.sqlite"
print(DATABASE)