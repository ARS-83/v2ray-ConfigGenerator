from print_color import print
import os
import sys
# import Generator 
import sqlite3
from Core import core
db = sqlite3.connect("./db/ars.db")
curser = db.cursor()
Core = core(db,curser)
global value
  
 

while True:
 Core.main()
 if Core.value == "1":
  Core.AddServer()
 
 


 if Core.value == "6":
   sys.exit(1)