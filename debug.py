import os
import logging
from datetime import datetime


def get_timestamp():
    now = datetime.now()
    year = now.year
    month = f"{now.month:02}"
    day = f"{now.day:02}"
    hours = f"{now.hour:02}"
    minutes = f"{now.minute:02}"
    seconds = f"{now.second:02}"
    milliseconds = f"{now.microsecond // 1000:03}"
    return f"{year}{month}{day}_{hours}{minutes}{seconds}_{milliseconds}"


class Debug:

    def __init__(self):

        # global enable
        self.enabled = False

        # file path
        self.path = ''

        # FLAGS options
        self.terminal_output_enable = False
        self.terminal_timestamp_enable = False
        self.file_output_enable = False
        self.file_timestamp_enable = False
        self.file_history_enable = False

    def enable(self):

        # globally enable logging
        self.enabled = True

        # set things up for file logging
        if self.file_output_enable and self.path != '':

            # calculate path directory
            script_path = os.path.abspath(self.path)
            script_dir = os.path.dirname(script_path)
            log_dir = os.path.join(script_dir, 'debug')
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # calculate path filename
            script_name = ''
            if self.file_history_enable:
                script_name = get_timestamp() + '_'
            script_name += os.path.basename(script_path)

            # set path = directory + filename
            self.path = os.path.join(log_dir, script_name + '.log')

            # create file and enable file logging
            logging.basicConfig(
                level=logging.DEBUG,
                filename=self.path,
                filemode="w",
                format="%(message)s"
            )

    def log(self, description, obj=''):

        # check if disabled
        if not self.enabled:
            return

        # log to file if enabled
        if self.file_output_enable:
            if self.file_timestamp_enable:
                logging.debug("%s %s %r", get_timestamp(), description, obj)
            else:
                logging.debug("%s %r", description, obj)

        # log to terminal if enabled
        if self.terminal_output_enable:
            if self.terminal_timestamp_enable:
                print(get_timestamp(), description, obj)
            else:
                print(description, obj)
