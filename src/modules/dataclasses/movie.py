from dataclasses import dataclass

@dataclass
class Movie:
    id: int
    title: str
    path: str
    thumbnailPath: str
    duration: int