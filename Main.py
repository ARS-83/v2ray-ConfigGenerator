#!/usr/bin/env python3
from print_color import print
import os
import sys
# import Generator 
import sqlite3
from Core import Core
db = sqlite3.connect("./db/ars.db")
curser = db.cursor()
core = Core(db,curser)
global value
  
 
core.main()
while True:

 if core.value == "1":
  core.add_server()
  
 
 elif core.value == "2":
  core.edit_server()
  
 elif core.value == "3":
  core.get_server_list()
 elif core.value == "4":
  core.get_config()
    
 elif core.value == "5":
  core.delete_server()
  

 elif core.value == "6":
   sys.exit(1)
