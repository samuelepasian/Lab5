# Add whatever it is needed to interface with the DB Table studente
import mysql.connector
from database.DB_connect import get_connection, DBConnect
from database.corso_DAO import Corso_DAO
from model.studente import Studente
from model.corso import Corso

class Studente_DAO:
    def get_allStudenti(self):
        cnx=get_connection()
        listaStudenti=[]
        if cnx is not None:
            cursor=cnx.cursor(dictionary=True)
            query="""select * from studente"""
            cursor.execute(query)
            for row in cursor:
                listaStudenti.append(Studente(row["matricola"],row["cognome"],row["nome"],row["CDS"]))
            cnx.close()
        return listaStudenti

    def get_studente(self, matricola):
        studente=None
        cnx = get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * from studente WHERE studente.matricola=%s"""
            cursor.execute(query,(matricola,))
            for row in cursor:
                studente=Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            cursor.close()
            cnx.close()
        return studente

    def get_corsi_perstudente(self,matricola):
        lista_corsi=[]
        cnx = get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT corso.* 
                    FROM iscrizione,corso 
                    WHERE iscrizione.codins=corso.codins and iscrizione.matricola=%s"""
            cursor.execute(query, (matricola,))
            for row in cursor:
                lista_corsi.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            cursor.close()
            cnx.close()
        return lista_corsi


