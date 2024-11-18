import os
import sys 
import httpx
import json
from print_color import print


class core:
 
 def __init__(self ,db,curser):

   self.db = db
   self.curser = curser
   self.value = ''
 def main(self):
 
  os.system("clear")

  print("""    _    ____  ____  
   / \  |  _ \/ ___| 
  / _ \ | |_) \___ \ 
 / ___ \|  _ < ___) |
/_/   \_\_| \_\____/ 
                     """,color="green")
  print("""**********************       
1. Add Server
2. Edit Server
3. Server List
4. Get Config
5. Delete Config
6. Exit                             
**********************   
     
""",color="red")

  self.value = input("Enter A Number :  ")      
 def CheckData(data:str):
   print(data)
 def AddServer(self):
   os.system("clear")
   print("* Add Server *\n" ,color="red")
   ServerUrl = self.CheckData("Enter Your UserName [Menu = 0]:")
   if ServerUrl == "0":
     return 
   
   UserName =  self.CheckData("Enter Your UserName [Menu = 0]:")
   if UserName == "0":
     return 
   Password =  self.CheckData("Enter Your Password [Menu = 0]:")
   if Password == "0":
     return    

   