# Andy Horn - October, 2019
# PythonFTP.py
#
# A working demonstration of the FTP Engine python library
# and the FTP python library, a linux-style CLI interface
# wrapped around the ftplib Python library.

from FTP_Engine import Engine

ADDRESS = "192.168.0.229"
USERNAME = "Home"
PWD = ""

# Instantiate the Engine object
e = Engine(ADDRESS, USERNAME, PWD)

# Run the engine
e.run()
