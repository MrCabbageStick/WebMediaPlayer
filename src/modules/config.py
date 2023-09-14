from pathlib import Path
import json
from dataclasses import dataclass


@dataclass
class MovieDirectory:
    comment: str
    path: Path


class Config:

    def __init__(self, configFilePath: Path | str) -> None:
        
        self.path = Path(configFilePath)

        if not self.path.exists or self.path.is_dir():
            raise FileNotFoundError(str(self.path))
        
        
        with open(self.path) as configFile:
            config: dict = json.load(configFile)

        
        self.movieDirectories = [
            MovieDirectory(movieDir.get("comment"), Path(movieDir.get("path")))
            for movieDir in config.get("movie_directories")
        ]

        self.allowedExtensions = list(map(
            lambda extension: extension if extension[0] == "." else "." + extension,
            config.get("allowed_extensions", [])
        ))