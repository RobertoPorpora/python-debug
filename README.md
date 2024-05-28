# python-debug

This project contains a simple utility to facilitate logging and debugging in your Python scripts.

## Usage

To use this debug utility, follow the steps below:

1. Copy the first part of the `debug.py` script.

2. Paste it into the script you want to debug.

3. Enable debugging by calling `debug_enable()`:

    Call this at the beginning of your script's execution to set up the logging configuration. This will create a `debug` directory in the same location as your script if it doesn't already exist and set up a log file for debugging information.

4. Log debug information using `debug_log()`:

    Use this function to log messages and objects for debugging purposes.

### Example

Here is a simple example demonstrating how to use the debug utility in your script:

```python
# enable debugging
debug_enable() # comment this line to disable debugging

# create a simple object with various properties
simple_object = {
    "string_property": "Hello, World!",
    "number_property": 42,
    "bool_property": True
}

# log the object
debug_log('simple_object', simple_object)
```

### Customization

- **Enable/Disable Debugging:** You can disable debugging by commenting out the `debug_enable()` call in the main execution block.
- **Log Directory:** Logs are saved in a `debug` directory by default. Modify the `debug_enable` function if you need to change the log directory path.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
