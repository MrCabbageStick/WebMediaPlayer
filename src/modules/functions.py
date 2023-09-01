from datetime import datetime
from modules.consts import DATE_FORMAT

def getFormattedTime(time: datetime):
    return time.strftime(DATE_FORMAT)


def debugPrint(*args, **kwargs):
    print(*args, **kwargs)