
from dataclasses import dataclass
@dataclass()
class Studente:
    matricola:str
    cognome:str
    nome:str
    CDS:str

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.matricola})"


