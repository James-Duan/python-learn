import os
import logging
import threading
from datetime import datetime
import ReadConfig


class Log:
    def __init__(self):
        global log_path, result_path, proDir
        proDir = ReadConfig.proDir
        result_path = os.path.join(proDir, "result")
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        log_path = os.path.join(result_path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(log_path, "log.log"))
        formatter = logging.Formatter('%(action_time)s - %(name)s - %(level_name)s -%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

