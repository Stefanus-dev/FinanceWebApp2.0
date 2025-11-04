<<<<<<< HEAD
# finance_logic.py
def calcola_saldo(df):
    """Calcola entrate, uscite e saldo"""
    entrate = df[df["Tipo"] == "Entrata"]["Importo"].sum()
    uscite = df[df["Tipo"] == "Uscita"]["Importo"].sum()
    saldo = entrate - uscite
    return entrate, uscite, saldo

def suggerisci_bilancio(entrate, uscite, saldo):
    if entrate == 0 and uscite == 0:
        return "Nessuna attività registrata. Inizia a inserire le tue spese o entrate!"

    rapporto = (uscite / entrate) * 100 if entrate > 0 else 0
    suggerimento = ""

    # Analisi delle proporzioni
    if entrate > 0 and uscite == 0:
        suggerimento = "Ottimo! Solo entrate registrate, ma ricordati di segnare anche le spese."
    elif rapporto > 100:
        suggerimento = "⚠️ Attenzione! Le uscite superano le entrate: serve un piano di risparmio."
    elif rapporto > 70:
        suggerimento = "🔸 Spese alte rispetto alle entrate. Prova a ridurre i costi non essenziali."
    else:
        suggerimento = "✅ Ottima gestione! Il tuo bilancio è in equilibrio."

    # Controllo “entrata molto superiore”
    if entrate > 0 and (entrate / (uscite + 1)) > 10:
        suggerimento += "\n💰 Hai un'entrata molto elevata rispetto alle spese: valuta di investire una parte."

    return suggerimento

# FinanceApp - Gestione Spese Mensili
# Copyright (c) 2025 [Stefanus-dev]
# Licenza: MIT (vedi file LICENSE)
=======
# finance_logic.py
def calcola_saldo(df):
    """Calcola entrate, uscite e saldo"""
    entrate = df[df["Tipo"] == "Entrata"]["Importo"].sum()
    uscite = df[df["Tipo"] == "Uscita"]["Importo"].sum()
    saldo = entrate - uscite
    return entrate, uscite, saldo

def suggerisci_bilancio(entrate, uscite, saldo):
    if entrate == 0 and uscite == 0:
        return "Nessuna attività registrata. Inizia a inserire le tue spese o entrate!"

    rapporto = (uscite / entrate) * 100 if entrate > 0 else 0
    suggerimento = ""

    # Analisi delle proporzioni
    if entrate > 0 and uscite == 0:
        suggerimento = "Ottimo! Solo entrate registrate, ma ricordati di segnare anche le spese."
    elif rapporto > 100:
        suggerimento = "⚠️ Attenzione! Le uscite superano le entrate: serve un piano di risparmio."
    elif rapporto > 70:
        suggerimento = "🔸 Spese alte rispetto alle entrate. Prova a ridurre i costi non essenziali."
    else:
        suggerimento = "✅ Ottima gestione! Il tuo bilancio è in equilibrio."

    # Controllo “entrata molto superiore”
    if entrate > 0 and (entrate / (uscite + 1)) > 10:
        suggerimento += "\n💰 Hai un'entrata molto elevata rispetto alle spese: valuta di investire una parte."

    return suggerimento

>>>>>>> 7388ce14fe9e2429839ee3e4c8a1e52e62d467b9
