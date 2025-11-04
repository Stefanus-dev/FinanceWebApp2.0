import pandas as pd
import os

# --- Percorsi file ---
STORICO_FILE = "data/storico.csv"
UTENTI_FILE = "data/utenti.csv"

# --- Storico ---
def carica_storico():
    if os.path.exists(STORICO_FILE):
        return pd.read_csv(STORICO_FILE)
    else:
        return pd.DataFrame(columns=["Utente", "Tipo", "Importo", "Categoria", "Data"])

def salva_storico(df):
    df.to_csv(STORICO_FILE, index=False)

# --- Utenti ---
def carica_utenti():
    if os.path.exists(UTENTI_FILE):
        return pd.read_csv(UTENTI_FILE)
    else:
        return pd.DataFrame(columns=["Utente", "Password"])

def salva_utenti(df):
    df.to_csv(UTENTI_FILE, index=False)
