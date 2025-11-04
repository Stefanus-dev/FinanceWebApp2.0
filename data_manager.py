<<<<<<< HEAD
# data_manager.py
import pandas as pd
import os
from datetime import datetime

FILE_PATH = "storico.csv"


def inizializza_csv():
    """Crea file CSV se non esiste."""
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=["Data", "Tipo", "Descrizione", "Importo"])
        df.to_csv(FILE_PATH, index=False)


def leggi_storico():
    """Legge il file CSV e lo restituisce come DataFrame."""
    if not os.path.exists(FILE_PATH):
        inizializza_csv()
    try:
        df = pd.read_csv(FILE_PATH)
        if df.empty:
            return pd.DataFrame(columns=["Data", "Tipo", "Descrizione", "Importo"])
        return df
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Data", "Tipo", "Descrizione", "Importo"])


def aggiungi_transazione(tipo, descrizione, importo):
    """Aggiunge una transazione al file CSV."""
    df = leggi_storico()
    nuova = pd.DataFrame([{
        "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Tipo": tipo,
        "Descrizione": descrizione,
        "Importo": importo
    }])
    df = pd.concat([df, nuova], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)


def elimina_transazione(index):
    """Elimina una transazione per indice."""
    df = leggi_storico()
    if index < 0 or index >= len(df):
        raise IndexError("Indice non valido per eliminazione.")
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(FILE_PATH, index=False)


def modifica_transazione(index, tipo, descrizione, importo):
    """Modifica una transazione esistente."""
    df = leggi_storico()
    if index < 0 or index >= len(df):
        raise IndexError("Indice non valido per modifica.")
    df.loc[index, ["Tipo", "Descrizione", "Importo"]] = [tipo, descrizione, importo]
    df.to_csv(FILE_PATH, index=False)

# FinanceApp - Gestione Spese Mensili
# Copyright (c) 2025 [Stefanus-dev]
# Licenza: MIT (vedi file LICENSE)
=======
# data_manager.py
import pandas as pd
import os
from datetime import datetime

FILE_PATH = "storico.csv"


def inizializza_csv():
    """Crea file CSV se non esiste."""
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=["Data", "Tipo", "Descrizione", "Importo"])
        df.to_csv(FILE_PATH, index=False)


def leggi_storico():
    """Legge il file CSV e lo restituisce come DataFrame."""
    if not os.path.exists(FILE_PATH):
        inizializza_csv()
    try:
        df = pd.read_csv(FILE_PATH)
        if df.empty:
            return pd.DataFrame(columns=["Data", "Tipo", "Descrizione", "Importo"])
        return df
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Data", "Tipo", "Descrizione", "Importo"])


def aggiungi_transazione(tipo, descrizione, importo):
    """Aggiunge una transazione al file CSV."""
    df = leggi_storico()
    nuova = pd.DataFrame([{
        "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Tipo": tipo,
        "Descrizione": descrizione,
        "Importo": importo
    }])
    df = pd.concat([df, nuova], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)


def elimina_transazione(index):
    """Elimina una transazione per indice."""
    df = leggi_storico()
    if index < 0 or index >= len(df):
        raise IndexError("Indice non valido per eliminazione.")
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(FILE_PATH, index=False)


def modifica_transazione(index, tipo, descrizione, importo):
    """Modifica una transazione esistente."""
    df = leggi_storico()
    if index < 0 or index >= len(df):
        raise IndexError("Indice non valido per modifica.")
    df.loc[index, ["Tipo", "Descrizione", "Importo"]] = [tipo, descrizione, importo]
    df.to_csv(FILE_PATH, index=False)
>>>>>>> 7388ce14fe9e2429839ee3e4c8a1e52e62d467b9
