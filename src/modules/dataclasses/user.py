from dataclasses import dataclass, field
from modules.functions import getTimeFromString

@dataclass
class User:
    id: int
    name: str
    displayName: str
    passwordHash: str
    addedOnStr: str
    isOwner: bool

    def __post_init__(self):
        self.addedOn = getTimeFromString(self.addedOnStr)