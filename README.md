# PythonFTP
A wrapper and CLI engine for interacting with an FTP server with Unix/Linux style commands

This library consists of three main parts: PythonFTP.py, FTP_Engine.py, and FTP.py


## PythonFTP
This script serves as a simple demonstration of how to run the FTP Engine, which drives the CLI (see next section).

Running the engine consists of the following three lines:

> `from FTP_Engine import Engine` <br>
> `e = Engine(ADDRESS, USERNAME, PWD)` <br>
> `e.run()`

All you need is the IP Address or Hostname of the FTP server, the username, and password. Instantiate an Engine object with these parameters and tell it to `run()`.


## FTP Engine
This script drives the command-line interface (CLI) for the FTP processes. It retains an instance of the FTP object (see next section) and reads user input to determine the FTP operations to perform. 

The available operations include:
* connect - Open an active connection to the FTP server
* disconnect - Close the connection to the FTP server
* ls - List the contents of the current directory
* pwd - Print the name of the working directory
* cd - Change directories
* send - Send a file _to_ the FTP server
* get - Get a file _from_ the FTP server
* mkdir - Make a directory, in the current working directory, on the FTP server
* rmdir - Delete a directory on the FTP server
* rm - Delete a file on the FTP server
* exit - Exit the engine (and close the connection to the FTP server)


## FTP
This object is the heart of the library and serves as a wrapper around the `ftplib` Python library. It makes performing the operations on a CLI simpler, adds basic error handling, and uses familiar Unix/Linux command names instead of the default names used in the `ftplib` library.
