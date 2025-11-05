# --- Calcoli totali ---
def calcola_totali(df):
    entrate = df[df["Tipo"]=="Entrata"]["Importo"].sum()
    uscite = df[df["Tipo"]=="Uscita"]["Importo"].sum()
    saldo = entrate - uscite
    return entrate, uscite, saldo

# --- Assegna categoria ---
def assegna_categoria(descrizione):
    descrizione_lower = descrizione.lower()
    
    categorie = {
        "Stipendio": ["stipendio", "salary", "paga"],
        "Affitto": ["affitto", "rent", "luce", "gas", "bollette"],
        "Spesa": ["supermercato", "spesa", "carrefour", "esselunga", "lidl"],
        "Svago": ["cinema", "palestra", "ristorante", "bar", "pizza", "uber", "netflix"],
        "Shopping": ["amazon", "zara", "h&m", "shopping", "nike", "adidas"]
    }
    
    for cat, keywords in categorie.items():
        for kw in keywords:
            if kw in descrizione_lower:
                return cat
    return "Altro"
