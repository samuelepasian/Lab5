from database.studente_DAO import Studente_DAO
from database.corso_DAO import Corso_DAO


class Model:
    def __init__(self):
        pass
    def fillstudenti(self):
        studenti=Studente_DAO().get_allStudenti()
        return studenti
    def fillcorsi(self):
        corsi=Corso_DAO().get_allCorsi()
        return corsi

    def get_iscritti_alcorso(self,codins):
        return Corso_DAO().get_iscritti_alcorso(codins)

    def get_studente(self,matricola):
        return Studente_DAO().get_studente(matricola)

    def get_corsi_perstudente(self, matricola):
        return Studente_DAO().get_corsi_perstudente(matricola)
