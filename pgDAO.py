import psycopg2
import hashlib
import json
class pgDAO:
    def __init__(self):
        pass
    
    def openConnection(self):
        self.myConnection = psycopg2.connect( host="tanl.cgnbxyetzh4a.us-east-1.rds.amazonaws.com", user="tanl", password="Semmakata$7", dbname="tanl" )
    def closeConnection(self):
        self.myConnection.close()
 
    
    def getConfig(self):
        self.openConnection()
        cur = self.myConnection.cursor()
        cur.execute( "select company, quarter from transcripts" )
        for company, quarter in cur.fetchall() :
            print(company+quarter)
        self.closeConnection()
        return "test"
    

    def iTranscript(self, trans):
        self.openConnection()
        cur = self.myConnection.cursor()
        sql = """INSERT INTO transcripts(tr_key, company, year, quarter, ticker)
             VALUES(%s, %s, %s, %s, %s) """
        data = (trans.tr_key, trans.company, trans.year, trans.quarter, trans.stock,)
        cur.execute(sql, data)
        self.myConnection.commit()
        self.closeConnection()

    def iExecutive(self, executive):
        self.openConnection()
        cur = self.myConnection.cursor()
        sql = """INSERT INTO executives(ex_key, company, name)
             VALUES(%s, %s, %s) """
        data = (executive.ex_key, executive.company, executive.name)
        cur.execute(sql, data)
        self.myConnection.commit()
        self.closeConnection()
    
    def iAnalyst(self, analyst):
        self.openConnection()
        cur = self.myConnection.cursor()
        sql = """INSERT INTO analyst(an_key, company, name)
             VALUES(%s, %s, %s) """
        data = (analyst.an_key, analyst.company, analyst.name)
        cur.execute(sql, data)
        self.myConnection.commit()
        self.closeConnection()

    def iQA(self, qa):
        self.openConnection()
        cur = self.myConnection.cursor()
        sql = """INSERT INTO questionanswer(qa_key, tr_key, an_key, ex_key, question, answer, questionasw, answerasw)
             VALUES(%s, %s, %s, %s,%s, %s, %s, %s) """
        data = (qa.qa_key, qa.tr_key, qa.an_key, qa.ex_key, qa.question, qa.answer, qa.questionASW, qa.answerASW)
        #print(cur.mogrify(sql, data))
        cur.execute(sql, data)
        self.myConnection.commit()
        self.closeConnection()
    
    def iQAKeyword(self, keys, tr_key, qa_key, type):
        self.openConnection()
        cur = self.myConnection.cursor()
        for keyword in keys:
            sql = """INSERT INTO keywords(qa_key, tr_key, type, keyword)
             VALUES(%s, %s, %s, %s) """
            data = (qa_key, tr_key, type, keyword)
            cur.execute(sql, data)
        self.myConnection.commit()
        self.closeConnection()
    
    def getTr_Key(self, trans):
        hashKey = hashlib.sha1(json.dumps({"company":trans.company,"quarter":trans.quarter,"year":trans.year}, sort_keys=True)).hexdigest()
        return hashKey
    
    def getAn_Key(self, analyst):
        hashKey = hashlib.sha1(json.dumps({"company":analyst.company,"name":analyst.name}, sort_keys=True)).hexdigest()
        return hashKey
    
    def getEx_Key(self, executive):
        hashKey = hashlib.sha1(json.dumps({"company":executive.company,"name":executive.name}, sort_keys=True)).hexdigest()
        return hashKey
