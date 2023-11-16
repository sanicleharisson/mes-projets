import sqlite3
import json
import os
import sys
def read_data(nom):
    with open(nom, "r", encoding="utf-8") as f:
        return json.load(f)

def write_data(nom, data):
    with open(nom, "w", encoding="utf-8") as f:
        json.dump(data, f)
class JsonData():
    def __init__(self,url,mode="no"):
        with open(url,"r",encoding="utf-8") as f:
            self.data=json.load(f)
        self.url=url
    def getData(self):
        return self.data
    def modifyData(self,data):
        self.data=data
    def saveData(self):
        with open(self.url,"w",encoding="utf-8") as f:
            json.dump(self.data,f)
        del self

class DatabaseHandler():
    def __init__(self,url=""):
        self.url=url
    def __del__(self):
        if hasattr(self,'db'):
            try:
                self.db.close()
            except:
                pass
    def connectToDb(self):
        
        try:
            self.db=sqlite3.connect(self.url)
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"[*] Erreur [*]\nType : {exc_type}\n Nom du Fichier : {fname}\n Ligne : {exc_tb.tb_lineno}\nNote : DatabaseHandler->executeQueries : Database url wrong.")
        
        
    def getLastPushId(self):
        return self.curs.lastrowid
    def executeQueries(self,queries=""):
        try:
            self.connectToDb()
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"[*] Erreur [*]\nType : {exc_type}\n Nom du Fichier : {fname}\n Ligne : {exc_tb.tb_lineno}\nNote : DatabaseHandler->executeQueries : Database url wrong.")
        self.curs=self.db.cursor()
        self.curs.execute(queries)
        try:
            return self.curs.fetchall()
        except:
            pass
    def commitChanges(self):
        try:
            self.db.commit()
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"[*] Erreur [*]\nType : {exc_type}\n Nom du Fichier : {fname}\n Ligne : {exc_tb.tb_lineno}\nNote : DatabaseHandler->commitChanges : Can't commit.")
    def closeDb(self):
        self.db.close()