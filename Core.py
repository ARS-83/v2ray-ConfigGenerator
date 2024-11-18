import os
import sqlite3
from print_color import print

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
        name = input("Please Enter Name Server:")
        self.cursor.execute("SELECT * FROM Server WHERE Name = ?", (name,))
        server = self.cursor.fetchone()
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
