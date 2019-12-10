#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__ =   "0.1"
__author__  =   "@odiq"
__date__    =   "2019/12/10"
"""


import os

directory = "/data/data/com.termux/files/home/.termux"
path = "/termux.properties"
ek = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"

def create():
   print("Creating please wait...")
   open(directory+path, "w+").write(ek)
   os.system("termux-reload-settings")

def gas():
   try:
      os.makedirs(directory)
   except OSError:
      os.makedirs(directory)
   create()

if __name__ == "__main__":
   try:
       gas()
       print("\nSucess!")
   except:
	print("\nFailed!")
