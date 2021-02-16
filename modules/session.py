from enum import Enum
import json
from datetime import datetime

class SessionStage(Enum):
    STARTED = 0
    COMBINATIONS_DONE = 1
    TRANSFORMS_DONE = 2
    LYRICS_DONE = 3


class Session:
    def __init__(self, session_name, args):
        self.SESSION_NAME = session_name
        self.ARGS = args

        try:
            f = open("session_{}.json".format(self.SESSION_NAME), "r")
            session_data = json.loads(f.read())
            print("session file loaded")
            self.ARGS = session_data["args"]
            self.STAGE = session_data["stage"]
            self.START_TIME = session_data["start_time"]
            f.close()
        except (IOError, FileNotFoundError):
            print("session file is not accessible. creating new...")
            self.STAGE = SessionStage.STARTED
            data = {
                "args": self.ARGS.toJSON(),
                "stage":  self.STAGE.value,
                "start_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
            with open("session_{}.json".format(self.SESSION_NAME), 'w') as outfile:
                json.dump(data, outfile)
            print("session file stored")
