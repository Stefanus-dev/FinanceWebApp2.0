# 💰 Finance Web App 2.0

Questa applicazione permette di gestire facilmente le proprie finanze personali tramite un'interfaccia web semplice e veloce.  
Permette di registrare **entrate** e **uscite**, categorizzarle automaticamente e visualizzare riepiloghi chiari e grafici.

---

## 🚀 Funzionalità Principali

- 🔑 **Login e Registrazione Utenti**
- ➕ **Aggiunta di Entrate e Uscite**
- 🧠 **Categorizzazione Automatica** basata sulla descrizione
- 📊 **Grafico a Torta** per la distribuzione delle spese
- 🗑️ **Eliminazione delle Transazioni**
- 💾 **Salvataggio Persistente** su file `.csv`
- 👤 Ogni utente vede solo i propri dati

---

## 🧱 Struttura del Progetto

FinanceWebApp2.0/
│
├── app.py # Interfaccia e logica principale Streamlit
├── data_manager.py # Funzioni per leggere e salvare i dati
├── finance_logic.py # Calcolo totali e categoria automatica
├── visualizer.py # Grafico a torta delle categorie
│
└── data/
├── storico.csv # Storico transazioni
└── utenti.csv # Credenziali utenti
└── categorie.csv # Mappatura dinamica

---

📝 Licenza

Distribuito sotto MIT License — libero utilizzo e modifica.

👤 Autore

Stefanus-dev
GitHub: https://github.com/Stefanus-dev


