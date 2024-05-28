# ------------------------------------------------------------------------------
# copy this inside the file you want to debug

import os
import logging

def debug_enable():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    log_dir = os.path.join(script_dir, 'debug')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    script_name = os.path.basename(script_path)
    log_path = os.path.join(log_dir, script_name + '.debug.log')
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_path,
        filemode="w",
        format="%(asctime)s %(message)s"
    )


def debug_log(description, obj=''):
    logging.debug("%s %r", description, obj)



# ------------------------------------------------------------------------------
# example usage

import sys

def main():
    simple_object = {
        "string_property": "Hello, World!",
        "number_property": 42,
        "bool_property": True
    }
    debug_log('simple_object', simple_object)
    sys.exit(0)


if __name__ == "__main__":
    debug_enable() # comment this to disable debugging
    try:
        debug_log('starting main()')
        main()
    except SystemExit as e:
        # Reraise the exception to terminate the program with the exit code.
        debug_log('SystemExit:', e)
        raise
    except BaseException as e:
        # catch SIGTERM, KeyboardInterrupt and other exceptions
        debug_log('BaseException:', e)
        sys.exit()


# ------------------------------------------------------------------------------
