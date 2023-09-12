from dataclasses import dataclass, field

@dataclass
class Movie:
    id: int
    title: str
    path: str
    thumbnailPath: str
    duration: int
    genres: list[tuple[int, str]] = field(default_factory=lambda: [])