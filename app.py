import streamlit as st
import pandas as pd
from datetime import date

from data_manager import carica_storico, salva_storico, carica_utenti, salva_utenti
from finance_logic import calcola_totali
from visualizer import grafico_categoria

# --- Streamlit App ---
st.title("💰 Finance Web App")

# --- Login / Registrazione ---
if "user" not in st.session_state:
    st.session_state["user"] = None

utenti_df = carica_utenti()

with st.sidebar:
    st.header("🔑 Login / Registrazione")

    tab = st.radio("Seleziona", ["Login", "Registrazione"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if tab == "Registrazione":
        if st.button("Registrati"):
            if username in utenti_df["Utente"].values:
                st.error("Utente già registrato")
            else:
                utenti_df = pd.concat([utenti_df, pd.DataFrame([{"Utente": username, "Password": password}])], ignore_index=True)
                salva_utenti(utenti_df)
                st.success("Registrazione avvenuta!")
    else:  # Login
        if st.button("Accedi"):
            if username in utenti_df["Utente"].values and utenti_df.loc[utenti_df["Utente"]==username, "Password"].values[0] == password:
                st.session_state["user"] = username
                st.success(f"Benvenuto, {username}!")
            else:
                st.error("Credenziali non valide")

# --- Se loggato ---
if st.session_state["user"]:
    df = carica_storico()

    st.header("➕ Aggiungi Transazione")
    with st.form("aggiungi"):
        tipo = st.selectbox("Tipo", ["Entrata", "Uscita"])
        importo = st.number_input("Importo", min_value=0.0, step=0.01)
        categoria = st.text_input("Categoria")
        data = st.date_input("Data", value=date.today())
        submit = st.form_submit_button("Aggiungi")
        
        if submit:
            new_row = {
                "Utente": st.session_state["user"],
                "Tipo": tipo,
                "Importo": importo,
                "Categoria": categoria,
                "Data": data
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            salva_storico(df)
            st.success("Transazione aggiunta!")

    # --- Riepilogo ---
    st.header("📊 Riepilogo")
    df_user = df[df["Utente"] == st.session_state["user"]]
    
    if not df_user.empty:
        entrate, uscite, saldo = calcola_totali(df_user)
        st.metric("Totale Entrate", f"{entrate} €")
        st.metric("Totale Uscite", f"{uscite} €")
        st.metric("Saldo", f"{saldo} €")
        st.dataframe(df_user)
        chart = grafico_categoria(df_user)
        if chart:
            st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Nessuna transazione presente.")
