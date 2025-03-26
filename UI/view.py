from cProfile import label

import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_matricola = None
        self.txt_nome=None
        self.txt_cognome=None
        self.btn_cerca = None
        self.dd_corsi=None
        self.txt_result = None
        self.txt_container = None
        self._btn_studente = None
        self._btn_corsi = None
        self._btn_iscriviti = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd_corsi=ft.Dropdown(label="Corsi", options=self._controller.get_options())
        #ROW with some controls
        # text field for the name

        # button for the "hello" reply
        self.btn_cerca = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.getIscrittialCorso)
        row1 = ft.Row([self.dd_corsi, self.btn_cerca],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self.txt_matricola = ft.TextField(
            label="Matricola",
            width=200,
            hint_text="Matricola", on_change=self._controller.ripristino_textfields
        )
        self.txt_nome = ft.TextField(
            read_only=True,
            label="Nome",
            width=200,
            hint_text="Nome"
        )
        self.txt_cognome = ft.TextField(
            read_only=True,
            label="Cognome",
            width=200,
            hint_text="Cognome"
        )
        row2 = ft.Row([self.txt_matricola,self.txt_nome, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._btn_studente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.get_studente)
        self._btn_corsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.get_corsi_perstudente)
        self._btn_iscriviti = ft.ElevatedButton (text="Iscriviti")
        row3=ft.Row([self._btn_studente,self._btn_corsi,self._btn_iscriviti],  alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
