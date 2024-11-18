import os
import sys 
import httpx
import json
from print_color import print

import sqlite3
class core:
 
 def __init__(self ,db:sqlite3.Connection,curser:sqlite3.Cursor):

   self.db = db
   self.curser = curser
   self.value = ''
 def main(self):
 
  os.system("clear")

  print(r"""    _    ____  ____  
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
5. Delete Server
6. Exit                             
**********************   
     
""",color="blue")

  self.value = input("Enter A Number :  ")      
 def CheckData(self,txt:str):
  while True:
    data = input(txt)
    if data.isspace() == True or data.strip() == "":
      continue
    else : return data
   
 def AddServer(self):
   os.system("clear")
   print("\n* Add Server *" ,color="blue")
   ServerUrl = self.CheckData("\nEnter Your URL Server [Menu = 0]:")
   if ServerUrl == "0":
     return 
   UserName =  self.CheckData("\nEnter Your UserName Server [Menu = 0]:")
   if UserName == "0":
     return 
   Password =  self.CheckData("\nEnter Your Password Server [Menu = 0]:")
   if Password == "0":
     return    
   Name =  self.CheckData("\nEnter Your Name Server [Menu = 0]:")
   if Name == "0":
     return 
   Domain =  self.CheckData("\nEnter Your Domain Server [Menu = 0]:")
   if Domain == "0":
     return    
   try:
    self.curser.execute("INSERT INTO Server(Name,URL,UserName,Password,Address) VALUES(?,?,?,?,?)",(Name,ServerUrl,UserName,Password,Domain))
    self.db.commit()
    print( f"server added \n",tag="Success",tag_color="green",color="green")
    input("Input Enter Key To Continue :")
   except Exception as e:
     print(e.args[0],color="magenta",tag="Error" ,tag_color="red")
 def EditServer(self):
   os.system("clear")
   Name = input("Please Enter Name Server:")
   Server = self.curser.fetchone(f"SELECT * FROM Server WHERE Name = '{Name}'")      
   if Server == None:
     print("server is not defined" , tag="Error",tag_color="red",color="magenta")
     return

   print(f"""
Server Found Info :
             
*********             
1. Name : {Server[1]}
2. URL : {Server[2]}
3. UserName : {Server[3]}
4. Password : {Server[4]}
5. Domain : {Server[5]}


""",color="white")
   key = input("Enter Key For Edit Field [Main = 0]:")  
   if key == "0":
     return self.main() 
   while True:
    value = ""
    if value =="0":
      print(f"""
Server Found Info :
             
*********             
1. Name : {Server[1]}
2. URL : {Server[2]}
3. UserName : {Server[3]}
4. Password : {Server[4]}
5. Domain : {Server[5]}


""",color="white")
      key = input("Enter Key For Edit Field [Main = 0]:")  
      if key == "0":
          return self.main() 
    if key == "1":
      value = input("Enter New Name [Main = 0]:")
      if value == "0" or value.isspace() == True or value.strip() =="":continue
        
      try :
       self.curser.execute("UPDATE Server SET Name = '?' WHERE Name = '?'",(value,Name))
       self.db.commit()       
       print( f"edit server success \n",tag="Success",tag_color="green",color="green")
       value ="0"
      except Exception as e :
         print(e.args[0],color="magenta",tag="Error" ,tag_color="red")
      
    if key == "2":
      value = input("Enter New URL [Main = 0]:")
      if value == "0" or value.isspace() == True or value.strip() =="":continue
        
      try :
       self.curser.execute("UPDATE Server SET URL = '?' WHERE Name = '?'",(value,Name))
       self.db.commit()       
       print( f"edit server success \n",tag="Success",tag_color="green",color="green")
       value ="0"       
      except Exception as e :
         print(e.args[0],color="magenta",tag="Error" ,tag_color="red")
    if key == "3":
      value = input("Enter New UserName [Main = 0]:")
      if value == "0" or value.isspace() == True or value.strip() =="":continue
        
      try :
       self.curser.execute("UPDATE Server SET UserName = '?' WHERE Name = '?'",(value,Name))
       self.db.commit()       
       print( f"edit server success \n",tag="Success",tag_color="green",color="green")
       value ="0"       
      except Exception as e :
         print(e.args[0],color="magenta",tag="Error" ,tag_color="red")
            
    if key == "4":
      value = input("Enter New Password [Main = 0]:")
      if value == "0" or value.isspace() == True or value.strip() =="":continue
        
      try :
       self.curser.execute("UPDATE Server SET Password = '?' WHERE Name = '?'",(value,Name))
       self.db.commit()
       print( f"edit server success \n",tag="Success",tag_color="green",color="green")
       value ="0"       
      except Exception as e :
         print(e.args[0],color="magenta",tag="Error" ,tag_color="red")
    if key == "5":
      value = input("Enter New Domain [Main = 0]:")
      if value == "0" or value.isspace() == True or value.strip() =="":continue
        
      try :
       self.curser.execute("UPDATE Server SET Domain = '?' WHERE Name = '?'",(value,Name))
       self.db.commit()
       print( f"edit server success \n",tag="Success",tag_color="green",color="green")
       value ="0"       
      except Exception as e :
         print(e.args[0],color="magenta",tag="Error" ,tag_color="red")
 def GetServerList(self):
  data = self.curser.execute("SELECT * FROM Server")
  servers = data.fetchall()
  counter = 1
  os.system("clear")
  print("\n* Server List *\n" ,color="blue")
  for server in servers  :
    print(f"{counter}. {server[1]} ")       
    counter+=1  
    
  input("Input Enter Key To Continue :")   
  return self.main()   





   

   