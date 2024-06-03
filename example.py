import sys
from debug import Debug


def main():
    global debug
    simple_object = {
        "string_property": "Hello, World!",
        "number_property": 42,
        "bool_property": True
    }
    debug.log('simple_object', simple_object)
    sys.exit(0)


# setup debugging
debug = Debug()
debug.path = __file__
debug.file_output_enable = True
debug.file_timestamp_enable = True
# debug.file_history_enable = True
# debug.terminal_output_enable = True
# debug.terminal_timestamp_enable = True
debug.enable()

try:
    debug.log('starting main()')
    main()
except SystemExit as e:
    # Reraise the exception to terminate the program with the exit code.
    debug.log('SystemExit:', e)
    raise
except BaseException as e:
    # catch SIGTERM, KeyboardInterrupt and other exceptions
    debug.log('BaseException:', e)
    sys.exit()
