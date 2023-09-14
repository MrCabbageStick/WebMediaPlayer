from pathlib import Path

from modules.functions import Debug

class MovieRegistry:

    paths: list[Path] = []
    allowedExtensions: list[str] = []
    foundFiles: list[Path] = []

    def __init__(self, *paths: Path, allowedExtensions: list[str]) -> None:
        
        paths = [Path(path) for path in paths]

        self.paths = paths
        self.allowedExtensions = allowedExtensions


    def findMovies(self):
        
        for path in self.paths:
            
            if not path.exists():
                Debug.warningPrint(f"Path does not exist: '{path}'")
                continue

            if not path.is_dir():
                Debug.warningPrint(f"Path is not a directory: '{path}'")
                continue

            for file in path.iterdir():

                if not file.exists() or file.is_dir():
                    continue

                if not file in self.foundFiles \
                    and file.suffix in self.allowedExtensions:
                    self.foundFiles.append(file)

