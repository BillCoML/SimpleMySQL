import mysql.connector

class Database:
    def __init__(self, password:str):
        self.database = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = password,
            database = "myDB"
        )
        
    def checkCommand(self,command):
        if ("select") in command: return "fetch"
        commitable = ["update","insert","modify","delete","set"]#update more keys
        for i in commitable:
            if i in command : return "commit"
        return None
        

    def commit(self, command):
        """
        Commit change on SQL_table
        """
        mycursor = self.database.cursor()
        if (self.checkCommand(command.lower())=="commit"):
            mycursor.execute(command)
            self.database.commit()
            return
        print("Not a committing method")
            
        
    def query(self, command):
        """
        return data fetched from SQL_tables
        """
        mycursor = self.database.cursor()
        if (self.checkCommand(command.lower())=="fetch"):
            mycursor.execute(command)
            return mycursor.fetchall()
        print("Not fetched anything")

        
            