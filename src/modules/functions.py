from datetime import datetime
from modules.consts import DATE_FORMAT

def getFormattedTime(time: datetime):
    return time.strftime(DATE_FORMAT)


def getTimeFromString(time: str):
    return datetime.strptime(time, DATE_FORMAT)


class Debug:

    @classmethod
    def debugPrint(cls, *args, **kwargs):
        print(*args, **kwargs)

    @classmethod
    def warningPrint(cls, *args, **kwargs):
        print("[WARNING]:", *args, **kwargs)

    @classmethod
    def errorPrint(cls, *args, **kwargs):
        print("[ERROR]:", *args, **kwargs)

