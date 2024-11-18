import os
import sqlite3
from print_color import print
import requests
import time
from Generator import GetConfig
import json
class Core:
    def __init__(self, db: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.db = db
        self.cursor = cursor
        self.value = ''

    def main(self):
        os.system("clear")
        print(r"""    _    ____  ____  
   / \  |  _ \/ ___| 
  / _ \ | |_) \___ \ 
 / ___ \|  _ < ___) |
/_/   \_\_| \_\____/ 
                     """, color="green")
        print("""**********************       
1. Add Server
2. Edit Server
3. Server List
4. Get Config
5. Delete Server
6. Exit                             
**********************   
     
""", color="blue")
        self.value = input("Enter A Number :  ")

    def check_data(self, txt: str):
        while True:
            data = input(txt)
            if data.isspace() or data.strip() == "":
                continue
            else:
                return data

    def add_server(self):
        os.system("clear")
        print("\n* Add Server *", color="blue")
        server_url = self.check_data("\nEnter Your URL Server [Menu = 0]:")
        if server_url == "0":
            return
        username = self.check_data("\nEnter Your UserName Server [Menu = 0]:")
        if username == "0":
            return
        password = self.check_data("\nEnter Your Password Server [Menu = 0]:")
        if password == "0":
            return
        name = self.check_data("\nEnter Your Name Server [Menu = 0]:")
        if name == "0":
            return
        domain = self.check_data("\nEnter Your Domain Server [Menu = 0]:")
        if domain == "0":
            return
        try:
            self.cursor.execute("INSERT INTO Server(Name, URL, UserName, Password, Address) VALUES(?,?,?,?,?)",
                                (name, server_url, username, password, domain))
            self.db.commit()
            print(f"Server added \n", tag="Success", tag_color="green", color="green")
            input("Input Enter Key To Continue :")
        except Exception as e:
            print(e.args[0], color="magenta", tag="Error", tag_color="red")

    def edit_server(self):
        os.system("clear")
        print("\n* Edit Server *", color="blue")
        name = input("Please Enter Name Server [Main = 0]:")
        self.cursor.execute("SELECT * FROM Server WHERE Name = ?", (name,))
        server = self.cursor.fetchone()
        if name == "0":
            return self.main()
        if server is None:
            print("Server is not defined", tag="Error", tag_color="red", color="magenta")
            return

        print(f"""
Server Found Info :
             
*********             
1. Name : {server[1]}
2. URL : {server[2]}
3. UserName : {server[3]}
4. Password : {server[4]}
5. Domain : {server[5]}


""", color="white")
        key = input("Enter Key For Edit Field [Main = 0]:")
        if key == "0":
            return self.main()
        while True:
            value = ""
            if value == "0":
                print(f"""
Server Found Info :
             
*********             
1. Name : {server[1]}
2. URL : {server[2]}
3. UserName : {server[3]}
4. Password : {server[4]}
5. Domain : {server[5]}


""", color="white")
                key = input("Enter Key For Edit Field [Main = 0]:")
                if key == "0":
                    return self.main()
            if key == "1":
                value = input("Enter New Name [Main = 0]:")
                if value == "0" or value.isspace() or value.strip() == "":
                    continue
                try:
                    self.cursor.execute("UPDATE Server SET Name = ? WHERE Name = ?", (value, name))
                    self.db.commit()
                    print(f"Edit server success \n", tag="Success", tag_color="green", color="green")
                    value = "0"
                except Exception as e:
                    print(e.args[0], color="magenta", tag="Error", tag_color="red")

            if key == "2":
                value = input("Enter New URL [Main = 0]:")
                if value == "0" or value.isspace() or value.strip() == "":
                    continue
                try:
                    self.cursor.execute("UPDATE Server SET URL = ? WHERE Name = ?", (value, name))
                    self.db.commit()
                    print(f"Edit server success \n", tag="Success", tag_color="green", color="green")
                    value = "0"
                except Exception as e:
                    print(e.args[0], color="magenta", tag="Error", tag_color="red")

            if key == "3":
                value = input("Enter New UserName [Main = 0]:")
                if value == "0" or value.isspace() or value.strip() == "":
                    continue
                try:
                    self.cursor.execute("UPDATE Server SET UserName = ? WHERE Name = ?", (value, name))
                    self.db.commit()
                    print(f"Edit server success \n", tag="Success", tag_color="green", color="green")
                    value = "0"
                except Exception as e:
                    print(e.args[0], color="magenta", tag="Error", tag_color="red")

            if key == "4":
                value = input("Enter New Password [Main = 0]:")
                if value == "0" or value.isspace() or value.strip() == "":
                    continue
                try:
                    self.cursor.execute("UPDATE Server SET Password = ? WHERE Name = ?", (value, name))
                    self.db.commit()
                    print(f"Edit server success \n", tag="Success", tag_color="green", color="green")
                    value = "0"
                except Exception as e:
                    print(e.args[0], color="magenta", tag="Error", tag_color="red")

            if key == "5":
                value = input("Enter New Domain [Main = 0]:")
                if value == "0" or value.isspace() or value.strip() == "":
                    continue
                try:
                    self.cursor.execute("UPDATE Server SET Domain = ? WHERE Name = ?", (value, name))
                    self.db.commit()
                    print(f"Edit server success \n", tag="Success", tag_color="green", color="green")
                    value = "0"
                except Exception as e:
                    print(e.args[0], color="magenta", tag="Error", tag_color="red")

    def get_server_list(self):
        data = self.cursor.execute("SELECT * FROM Server")
        servers = data.fetchall()
        counter = 1
        os.system("clear")
        print("\n* Server List *\n", color="blue")
        for server in servers:
            print(f"{counter}. {server[1]}")
            counter += 1

        input("Input Enter Key To Continue :")
        return self.main()
    def delete_server(self):
        print("\n* Delete Server *", color="blue")
        os.system("clear")
        name = input("Please Enter Name Server [Main = 0]:")
        if name == "0":
            return self.main()
        self.cursor.execute("SELECT * FROM Server WHERE Name = ?", (name,))
        server = self.cursor.fetchone()
        if server is None:
            print("Server is not defined", tag="Error", tag_color="red", color="magenta")
            return
        try:
         self.cursor.execute(f"DELETE Server WHERE Id = '{server[0]}'")
         self.db.commit()
         print(f"delete server success \n", tag="Success", tag_color="green", color="green")
         return
        except Exception as e:
                    print(e.args[0], color="magenta", tag="Error", tag_color="red")
    def get_config(self):
      step = 0
      
      while True:
       if step == 0:

        os.system("clear")
        print("\n* Get Config Server *", color="blue")
        name = input("Please Enter Name Server [Main = 0]:")
        if name == "0":
            return self.main()
        self.cursor.execute("SELECT * FROM Server WHERE Name = ?", (name,))
        global server 
        server = self.cursor.fetchone()
        if server is None:
            print("Server is not defined", tag="Error", tag_color="red", color="magenta")
            return
        else :step =1
       if step == 1:
            global inbound
            inbound = input("Enter Inbound Id Your Server [Main = 0]:")
            if not inbound.isdigit() : continue
            if inbound=="0":
                return self.main()
            else: step = 2
       if step == 2:
            global uuid
            uuid = input("Enter Your Config UUID [Main = 0]:")
       
            if uuid=="0":
                return self.main()
            else: step = 3
       if step == 3:
            global ConfigName
            ConfigName = input("Enter Your Config Name Config [Main = 0]:")
       
            if ConfigName=="0":
                return self.main()
            else: step = 4            
       if step == 4:
        try:  
          response = None
          try:

           response =  requests.post(f"{server[3]}/login",data={"username": f"{server[1]}", "password": f"{server[2]}"})
          except:
           response =  requests.post(f"{server[3]}/login",data={"username": f"{server[1]}", "password": f"{server[2]}"})

          responseLogon = json.loads(response.text)
          if responseLogon['success'] == False:
              print(f"can not login server. details : {response.text}\n",tag_color="red",tag="Error" ,color="magenta" )
              input("Input Enter To Back Main :")
              return self.main()
          session = ""
          if len(response.headers.get("Set-Cookie").split("; ") )>= 6:
      
             session =  response.headers.get("Set-Cookie").split("; ")[4]  
             session =session.split(", ")[1]
          else:
            session =  response.headers.get("Set-Cookie").split("; ")[0]             
          origin = server[2].split("/")
  
          headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Origin': f'{origin[0]}://{origin[2]}',
                    'Connection': 'keep-alive',
                    'Referer': f'{server[2]}/panel/inbounds',
                    'Cookie': f'lang=en-US; {session}'
                }
          try:
              
               response = requests.request("POST", f"{server[2]}/panel/inbound/list", headers=headers)
          except:
             response = requests.request("POST", f"{server[2]}/panel/inbound/list", headers=headers)

          responseLogon = json.loads(response.text)   
          if responseLogon['success'] == True:
              for inbound in responseLogon['obj']:
                  if inbound['id'] == int(inbound):
                      try:
                       config = GetConfig(inbound,config,ConfigName,inbound['port'],inbound['protocol'],server[3])
                       print("create config success fully",tag="success",tag_color="green",color="magenta")
                       print(f"Config : {config}  \n")
                       input("Input Enter To Back Main :")   
                       return self.main()      
                      except:
                          print(f"There was a problem while creating the configuration.\n",tag_color="red",tag="Error" ,color="magenta" )
                          input("Input Enter To Back Main :")   
                          return self.main()      
              print(f"can not read data as server. details : {response.text}\n",tag_color="red",tag="Error" ,color="magenta" )
              input("Input Enter To Back Main :")   
              return self.main()      
          else:
              print(f"can not read data as server. details : {response.text}\n",tag_color="red",tag="Error" ,color="magenta" )
              input("Input Enter To Back Main :")
              return self.main() 

          
        except:
            print(f"error in Login or Get Data:\n",tag_color="red",tag="Error" ,color="magenta" )
            input("Input Enter To Back Main :")
            return self.main()
        
   