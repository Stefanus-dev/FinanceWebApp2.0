import streamlit as st
import pandas as pd
from datetime import date

from data_manager import carica_storico, salva_storico, carica_utenti, salva_utenti
from finance_logic import calcola_totali, assegna_categoria
from visualizer import grafico_categoria

st.set_page_config(page_title="💰 Finance Web App", layout="wide")
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
    else:
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
        descrizione = st.text_input("Descrizione")
        data = st.date_input("Data", value=date.today())
        submit = st.form_submit_button("Aggiungi")
        
        if submit:
            categoria_finale = assegna_categoria(descrizione)
            new_row = {
                "Utente": st.session_state["user"],
                "Tipo": tipo,
                "Importo": importo,
                "Categoria": categoria_finale,
                "Descrizione": descrizione,
                "Data": pd.to_datetime(data)
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            salva_storico(df)
            st.rerun()

    st.header("📊 Riepilogo")
    df_user = df[df["Utente"] == st.session_state["user"]]

    if not df_user.empty:
        entrate, uscite, saldo = calcola_totali(df_user)
        st.metric("Totale Entrate", f"{entrate} €")
        st.metric("Totale Uscite", f"{uscite} €")
        st.metric("Saldo", f"{saldo} €")

        st.subheader("🗑️ Transazioni")
        display_df = df_user.copy()
        display_df["Data"] = display_df["Data"].dt.strftime("%Y-%m-%d")
        for i, row in df_user.iterrows():
            cols = st.columns([1, 2, 1, 1, 1, 1])
            cols[0].write(row["Tipo"])
            cols[1].write(row["Descrizione"])
            cols[2].write(f"{row['Importo']} €")
            cols[3].write(row["Categoria"])
            cols[4].write(row["Data"])
            if cols[5].button("Elimina", key=f"del_{i}"):
                df = df.drop(i)
                salva_storico(df)
                st.rerun()

        # Grafico a torta
        chart = grafico_categoria(df_user)
        if chart:
            st.altair_chart(chart, width='stretch')
    else:
        st.info("Nessuna transazione presente.")
