# Add whatever it is needed to interface with the DB Table corso

import mysql.connector
from database.DB_connect import get_connection, DBConnect
from model.corso import Corso
from model.studente import Studente

class Corso_DAO:
    def get_allCorsi(self):
        cnx=get_connection()
        listaCorsi=[]
        if cnx is not None:
            cursor=cnx.cursor(dictionary=True)
            query="""select * from corso"""
            cursor.execute(query)
            for row in cursor:
                listaCorsi.append(Corso(row["codins"],row["crediti"],row["nome"],row["pd"]))
            cnx.close()
        return listaCorsi

    def get_iscritti_alcorso(self,codins):
        lista_studenti=[]
        query="""SELECT studente.* 
                FROM iscrizione,studente
                WHERE iscrizione.matricola=studente.matricola 
                AND iscrizione.codins=%s"""
        cnx=get_connection()
        if cnx is not None:
            cursor=cnx.cursor(dictionary=True)
            cursor.execute(query,(codins,))
            for row in cursor:
                lista_studenti.append(Studente(row["matricola"],row["cognome"],row["nome"],row["CDS"]))
            cursor.close()
            cnx.close()
        return lista_studenti




