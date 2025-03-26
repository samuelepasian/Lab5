import flet as ft
from model.modello import Model
from UI.view import View
from database.corso_DAO import Corso_DAO

class Controller:
    def __init__(self, view:View, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def get_options(self):
        corsi=self._model.fillcorsi()
        options=[]
        for corso in corsi:
            options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        return options

    def getIscrittialCorso(self,e):
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._view.dd_corsi.value==None:
            self._view.txt_result.controls.append(ft.Text("Nessun corso selezionato"))
            self._view.update_page()
        else:
            corso=self._view.dd_corsi.value
            lista_iscritti=self._model.get_iscritti_alcorso(corso)
            for iscritto in lista_iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{iscritto.__str__()}"))
            self._view.update_page()

    def get_studente(self, e):
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._view.txt_matricola.value=="":
            self._view.txt_result.controls.append(ft.Text("Nessuna matricola selezionata"))
            self._view.update_page()
        else:
            studente=self._model.get_studente(self._view.txt_matricola.value)
            if studente==None:
                self._view.create_alert("Nessuno studente con questa matricola")
            else:
                self._view.txt_nome.value=f"{studente.nome}"
                self._view.txt_cognome.value=f"{studente.cognome}"
                self._view.update_page()

    def ripristino_textfields(self,e):
        self._view.txt_nome.value=""
        self._view.txt_cognome.value=""

    def get_corsi_perstudente(self, e):
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._view.txt_matricola.value == "":
            self._view.txt_result.controls.append(ft.Text("Nessuna matricola selezionata"))
            self._view.update_page()
        else:
            if self._model.get_studente(self._view.txt_matricola.value)== None:
                self._view.create_alert("Nessuno studente con questa matricola")
            else:
                corsi=self._model.get_corsi_perstudente(self._view.txt_matricola.value)
                self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi a cui è iscritto:"))
                for corso in corsi:
                    self._view.txt_result.controls.append(ft.Text(f"{corso.__str__()}"))
                self._view.update_page()