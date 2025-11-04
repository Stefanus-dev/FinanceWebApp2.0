import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import bcrypt
import os

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="FinanceApp Web", page_icon="💰", layout="wide")

# --- PERCORSI ---
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
CSV_PATH = os.path.join(DATA_DIR, "storico.csv")
USERS_PATH = "users.csv"

# --- SESSIONE INIZIALE ---
if "user" not in st.session_state:
    st.session_state["user"] = None

# --- GESTIONE UTENTI ---
def carica_utenti():
    if os.path.exists(USERS_PATH):
        return pd.read_csv(USERS_PATH)
    else:
        return pd.DataFrame(columns=["username", "password"])

def salva_utenti(df):
    df.to_csv(USERS_PATH, index=False)

def registra_utente(username, password):
    df = carica_utenti()
    if username in df["username"].values:
        return False
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    nuovo = pd.DataFrame([{"username": username, "password": hashed.decode("utf-8")}])
    df = pd.concat([df, nuovo], ignore_index=True)
    salva_utenti(df)
    return True

def verifica_login(username, password):
    df = carica_utenti()
    if username not in df["username"].values:
        return False
    stored_hash = df[df["username"] == username]["password"].values[0].encode("utf-8")
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash)

def reset_password(username, new_password):
    df = carica_utenti()
    if username in df["username"].values:
        hashed = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
        df.loc[df["username"] == username, "password"] = hashed.decode("utf-8")
        salva_utenti(df)
        return True
    return False

# --- GESTIONE DATI FINANZIARI ---
def carica_dati():
    if os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0:
        df = pd.read_csv(CSV_PATH)
        for col in ["Utente", "Tipo", "Importo", "Descrizione"]:
            if col not in df.columns:
                df[col] = ""
        return df
    else:
        return pd.DataFrame(columns=["Utente", "Tipo", "Importo", "Descrizione"])

def salva_dati(df):
    df.to_csv(CSV_PATH, index=False)

def aggiungi_voce(utente, tipo, importo, descrizione):
    df = carica_dati()
    nuova_riga = pd.DataFrame([{"Utente": utente, "Tipo": tipo, "Importo": importo, "Descrizione": descrizione}])
    df = pd.concat([df, nuova_riga], ignore_index=True)
    salva_dati(df)
    return df

def elimina_voce(utente, indice):
    df = carica_dati()
    df_utente = df[df["Utente"] == utente].reset_index(drop=True)
    if 0 <= indice < len(df_utente):
        globale_idx = df[df["Utente"] == utente].index[indice]
        df = df.drop(globale_idx).reset_index(drop=True)
        salva_dati(df)
    return carica_dati()

# --- INTERFACCIA ---
st.title("💰 FinanceApp Web")

# --- MENU LOGIN / REGISTRAZIONE ---
menu = ["Login", "Registrati", "Reset Password"]
scelta = st.sidebar.selectbox("Navigazione", menu)

if scelta == "Registrati":
    st.subheader("🔑 Crea un nuovo account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    if st.button("Crea account"):
        if registra_utente(new_user, new_pass):
            st.success("Registrazione completata! Ora puoi accedere.")
        else:
            st.warning("Questo username esiste già.")

elif scelta == "Reset Password":
    st.subheader("🔒 Reset password")
    user = st.text_input("Username")
    new_pass = st.text_input("Nuova password", type="password")
    if st.button("Aggiorna password"):
        if reset_password(user, new_pass):
            st.success("Password aggiornata con successo!")
        else:
            st.warning("Utente non trovato.")

else:
    st.subheader("👤 Accesso utente")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Accedi"):
        if verifica_login(username, password):
            st.session_state["user"] = username
        else:
            st.error("Credenziali non valide.")

# --- SEZIONE PRINCIPALE ---
if st.session_state["user"]:
    st.success(f"Benvenuto, {st.session_state['user']} 👋")

    col1, col2 = st.columns(2)

    with col1:
        st.header("➕ Aggiungi Movimento")
        tipo = st.selectbox("Tipo", ["Entrata", "Uscita"])
        importo = st.number_input("Importo (€)", min_value=0.0, format="%.2f")
        descrizione = st.text_input("Descrizione")
        if st.button("Aggiungi"):
            if importo > 0:
                aggiungi_voce(st.session_state["user"], tipo, importo, descrizione)
                st.success("Movimento aggiunto!")
            else:
                st.warning("Inserisci un importo valido.")

    with col2:
        st.header("📊 Riepilogo")
        df = carica_dati()
        df_user = df[df["Utente"] == st.session_state["user"]]
        if not df_user.empty:
            tot_entrate = df_user[df_user["Tipo"] == "Entrata"]["Importo"].sum()
            tot_uscite = df_user[df_user["Tipo"] == "Uscita"]["Importo"].sum()
            saldo = tot_entrate - tot_uscite

            st.metric("Totale Entrate", f"{tot_entrate:.2f} €")
            st.metric("Totale Uscite", f"{tot_uscite:.2f} €")
            st.metric("Saldo Totale", f"{saldo:.2f} €")

            fig, ax = plt.subplots(figsize=(5, 3))
            df_user.groupby("Tipo")["Importo"].sum().plot(kind="bar", ax=ax)
            ax.set_ylabel("Importo (€)")
            st.pyplot(fig)
        else:
            st.info("Nessun movimento registrato.")

    st.header("📜 Storico Movimenti")
    if not df_user.empty:
        st.dataframe(df_user.reset_index(drop=True))
        elimina_idx = st.number_input("Indice da eliminare", min_value=0, max_value=len(df_user)-1, step=1)
        if st.button("Elimina movimento"):
            elimina_voce(st.session_state["user"], elimina_idx)
            st.success("Movimento eliminato con successo!")
    else:
        st.write("Nessun dato da mostrare.")

    if st.button("Logout"):
        st.session_state["user"] = None
