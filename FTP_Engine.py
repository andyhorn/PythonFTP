# Andy Horn - October, 2019
# FTP_Engine.py
#
# The Engine class drives a CLI for performing activities
# on an FTP server. It relies on the FTP library to perform
# the underlying operations.


from FTP import Ftp, Usage
from sys import version_info


class Engine:
    def __init__(self, address, username, pwd):
        self.address = address
        self.username = username
        self.pwd = pwd
        self.ftp = Ftp(self.address, self.username, self.pwd)


    def _invalid_arg(self):
        print("Error - Invalid argument(s)")


    def _filter_empty(self, item):
        if item.strip() is "":
            return False
        else:
            return True


    def input(self, display):
        if version_info >= (3,0):
            return input(">> ")
        else:
            return raw_input(">> ")


    # The core of the engine, a while loop with a list
    # of if/elif statements to determine which FTP
    # operation the user is trying to perform
    def run(self):
        RUN = True
        while RUN:
            cmd = self.input(">> ")
            c = cmd.lower()

            try:
                if c == "connect":
                    self.ftp.connect()

                elif c == "disconnect":
                    self.ftp.disconnect()

                elif c == "ls":
                    self.ftp.ls()

                elif c == "pwd":
                    self.ftp.pwd()

                elif "cd" in c:
                    params = self.get_params(cmd, 1, 1)
                    if len(params) is not 1:
                        self.invalid_arg()
                        Usage.cd()
                    else:
                        dir = params[0]
                        self.ftp.cd(dir)

                elif "send" in c:
                    params = self.get_params(cmd, 1, 1)
                    if len(params) is not 1:
                        self.invalid_arg();
                        Usage.send()
                    else:
                        filename = params[0]
                        self.ftp.send(filename)

                elif "get" in c:
                    params = self.get_params(cmd, 2, 2)
                    if len(params) is not 2:
                        self.invalid_arg()
                        Usage.get()
                    else:
                        filename = params[0]
                        save_file = params[1]
                        self.ftp.get(filename, save_file)

                elif "mkdir" in c:
                    params = self.get_params(cmd, 1, 1)
                    if len(params) is not 1:
                        self.invalid_arg()
                        Usage.mkdir()
                    else:
                        dirname = params[0]
                        self.ftp.mkdir(dirname)

                elif "rmdir" in c:
                    params = self.get_params(cmd, 1, 1)
                    if len(params) is not 1:
                        self.invalid_arg()
                        Usage.rmdir()
                    else:
                        dirname = params[0]
                        self.ftp.rmdir(dirname)

                elif "rm" in c:
                    params = self.get_params(cmd, 1, 1)
                    if len(params) is not 1:
                        self.invalid_arg()
                        Usage.rm()
                    else:
                        filename = params[0]
                        self.ftp.rm(filename)

                elif c == "exit":
                    self.ftp.disconnect()
                    RUN = False
                    print("Goodbye!")

                else:
                    print("Error - Command not recognized")

            except Exception as e:
                print("An unknown error ocurred")
                print(e)


    def get_params(self, s, min, max):
        sp = s.split(" ")
        ret = []
        if len(sp) < min + 1 or len(sp) > max + 1:
            if "\"" in s:
                sp = s.split("\"")
                sp = list(filter(self._filter_empty, sp))
                cmd = sp[0].strip()
                param1 = sp[1].strip()
                ret.append(param1)
                if (max > 1):
                    param2 = sp[2].strip()
                    ret.append(param2)
        else:
            cmd = sp[0]
            param1 = sp[1]
            ret.append(param1)
            if (max > 1):
                param2 = sp[2]
                ret.append(param2)
        return ret
