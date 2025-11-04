# --- Calcoli bilancio ---
def calcola_totali(df_user):
    entrate = df_user[df_user["Tipo"]=="Entrata"]["Importo"].sum()
    uscite = df_user[df_user["Tipo"]=="Uscita"]["Importo"].sum()
    saldo = entrate - uscite
    return entrate, uscite, saldo
