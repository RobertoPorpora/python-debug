# python-debug

Simple log-to-file library for debugging Python scripts.


## Why Use This?

Regardless of the fact that logging to a file with precise timestamps can generally be more practical and useful than printing to the screen...

There are times when you need to debug issues:
- that only manifest during runtime.
- when access to a debugger isn't available.
- when halting the process isn't feasible.
- when the stdout/stderr isn't visible.
- when dealing with a plug-in or a child process.

In such scenarios, logging to a file can be invaluable.

This repository offers a straightforward logger, complete with detailed timestamps, enabling quick setup for file logging.

This library can also be used for simple terminal printing.  
It adds the following features:
- a global switch to disable all debug_log() calls.
- timestamp to the output (can be easily disabled).

<div style="text-align: right;">
    <a href="#python-debug">Back to top</a>
</div>


## Usage

1. Copy `debug.py` into your project.
2. Insert `from debug import Debug` in the `.py` file where you want to use the logging functions.
3. At the start of your script, Create a new debug object, set the path, set some flags and call debug.enable() like so:
```python
# create debug object
from debug import Debug
debug = Debug()
# set the path to be the same as your script's path
debug.path = __file__
# set some flags, See "FLAGS options" below.
debug.file_output_enable = True
debug.file_timestamp_enable = True
# call enable()
debug.enable()
```
4. Every time you need to log something, call `debug.log(DESCRIPTION, SOME_OBJECT)` just like you would call `print(DESCRIPTION, SOME_OBJECT)`.
5. When you have finished debugging, comment or delete call to enable() like this `# debug.enable();` to disable logging.
    - No need to comment or delete any `debug.log()` line. Without `debug.enable()`, they will do nothing.

<div style="text-align: right;">
    <a href="#python-debug">Back to top</a>
</div>


## FLAGS options

There are some flags you can use to customize how debug.log() works.


### debug.terminal_output_enable

Why forgo terminal output while logging to file?  
Set this to True in order to see everything you log to file also on the process stdout.
Do you want to disable this at some point?  
Simply set it back to False before calling `debug.enable()`.


### debug.terminal_timestamp_enable

If you don't want timestamps for every line in your terminal, set this to False.


### debug.file_output_enable

Need to disable logging to file?  
Use this switch to enable (True) or disable (False) file logging.


### debug.file_timestamp_enable

If you don't want timestamps for every line in your file, set this to False.


### debug.file_history_enable

**debug.file_history_enable = False**: only one file is written and it is overwritten over and over everytime the executable executes.
```
root
├── debug.py
├── main.py  <-- your script
└── debug
    └── main.py.log
```

**debug.file_history_enable = True**: it generates a new timestamped file each time the executable is executed. 
```
root
├── debug.py
├── main.py  <-- your script
└── debug
    ├── 20240531_1234_000_main.py.log
    ├── 20240531_1234_123_main.py.log
    ├── 20240531_1256_012_main.py.log
    └── 20240531_1345_987_main.py.log
```

<div style="text-align: right;">
    <a href="#python-debug">Back to top</a>
</div>


## Testing and compiling the example.

- Check `example.py`.
- Execute it with command `python example.py`.
- Check the log file that has been written in `debug/` folder.
- Experiment with the `example.py` file (disable debugging, change FLAGS, log other types of data, etc.).

<div style="text-align: right;">
    <a href="#python-debug">Back to top</a>
</div>


## Links.

- [Debug logger for Python.](https://github.com/RobertoPorpora/python-debug)
- [Debug logger for C/C++.](https://github.com/RobertoPorpora/c-debug)
- [Debug logger for Node.js.](https://github.com/RobertoPorpora/node-debug)
- [Debug logger for Rust.](https://github.com/RobertoPorpora/rust-debug)


<div style="text-align: right;">
    <a href="#python-debug">Back to top</a>
</div>