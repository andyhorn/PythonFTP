# Andy Horn - October, 2019
# FTP.py
#
# Provides a wrapper around the ftplib/FTP object
# to perform FTP operations on a FTP server. Also
# provides a Usage class that will print out the
# usage statements for each available operation.

from ftplib import FTP
import os

class Usage:
    def cd():
        print("Usage:\tcd <dirname>")
        print("\tChange to directory <dirname>")

    def send():
        print("Usage:\tsend <filename>")
        print("\tCopies the file <filename> to the current directory")
        print("\ton the FTP server")

    def get():
        print("Usage:\tget <filename> <save_file>")
        print("\tReads the file <filename> from the FTP server")
        print("\tand writes the data to <save_file>")

    def mkdir():
        print("Usage:\tmkdir <dirname>")
        print("\tCreates the directory <dirname> in the current directory")
        print("\ton the FTP server")

    def rmdir():
        print("Usage:\trmdir <dirname>")
        print("\tRemoves the directory <dirname> from the FTP server")

    def rm():
        print("Usage:\trm <filename>")
        print("\tRemoves the file <filename> from the FTP server")


class Ftp:
    def __init__(self, address, username, pwd = None):
        self.address = address
        self.username = username
        self.pwd = pwd
        self.ftp = FTP(self.address)
        self.is_open = False
        self.need_reset = False


    def connect(self):
        if self.need_reset:
            self.ftp = FTP(self.address)
            self.need_reset = False
        try:
            self.ftp.login(user=self.username)
            self.is_open = True
            print("Connected!")
            print(self.ftp.getwelcome())
        except:
            print("Error, unable to connect!")
            print("Address: %s" % self.address)
            print("Username: %s" % self.username)
            print("Password: %s" % self.pwd)


    def disconnect(self):
        try:
            self.ftp.quit()
        except:
            self.ftp.close()
        finally:
            self.is_open = False
            self.need_reset = True
            print("Connection closed!")


    def ls(self):
        if self.is_open:
            try:
                print(".")
                print("..")
                self.ftp.dir()
            except Exception as e:
                print("Error - %s" % e)
        else:
            print("Error - No connection")


    def pwd(self):
        if self.is_open:
            try:
                self.ftp.pwd()
            except Exception as e:
                print("Error - %s" % e)
        else:
            print("Error - No connection")


    def cd(self, dir):
        if self.is_open:
            print("\t %s" % dir)
            try:
                self.ftp.cwd(dir)
                self.ls()
            except:
                print("Error - Invalid directory")
        else:
            print("Error - No connection")


    def send(self, filename):
        if os.path.exists(filename):
            if self.is_open:
                print("Sending file %s..." % filename)
                try:
                    self.ftp.storbinary("STOR " + filename, open(filename, 'rb'))
                    print("Success!")
                except Exception as e:
                    print("Error - %s" % e)
            else:
                print("Error - No connection")
        else:
            print("Error - Invalid filename")


    def get(self, filename, save_file):
        if self.is_open:
            print("Retrieving file %s..." % filename)
            try:
                localfile = open(save_file, 'wb')
                self.ftp.retrbinary("RETR " + filename, localfile.write, 1024)
                localfile.close()
                print("Success!")
            except Exception as e:
                print("Error - %s" % e)
        else:
            print("Error - No connection")


    def mkdir(self, dirname):
        if self.is_open:
            print("Creating directory %s..." % dirname)
            try:
                self.ftp.mkd(dirname)
                print("Success!")
            except Exception as e:
                print("Error - %s" % e)


    def rmdir(self, dirname):
        if self.is_open:
            print("Removing directory %s" % dirname)
            try:
                self.ftp.rmd(dirname)
                print("Success!")
            except Exception as e:
                print("Error - %s" % e)
        else:
            print("Error - No connection")


    def rm(self, filename):
        if self.is_open:
            print("Deleting file %s..." % filename)
            try:
                self.ftp.delete(filename)
                print("Success!")
            except Exception as e:
                print("Error - %s" % e)
        else:
            print("Error - No connection")
