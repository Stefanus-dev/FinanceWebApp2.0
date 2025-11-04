# 💰 FinanceWebApp

Una semplice ma potente applicazione web per la **gestione delle spese mensili**, sviluppata in **Python + Streamlit**.  
Consente di inserire entrate e uscite, visualizzare grafici dinamici, salvare lo storico e ricevere consigli di bilancio.

---

## 🚀 Funzionalità principali

✅ **Registrazione e Login utenti** — sistema sicuro con password hashate (grazie a `passlib[bcrypt]`)  
✅ **Gestione spese** — aggiunta, modifica ed eliminazione di entrate e uscite  
✅ **Storico dati CSV** — i movimenti vengono salvati in un file locale  
✅ **Grafici interattivi** — visualizzazione automatica di entrate/uscite con `matplotlib`  
✅ **Consigli di bilancio** — suggerimenti dinamici in base al saldo mensile  
✅ **Compatibilità totale** — funziona su Windows, Mac, Linux e **Streamlit Cloud**

---

## 🧠 Tecnologie utilizzate

- **Python 3.10+**
- **Streamlit** — per la UI web
- **Pandas** — per la gestione dei dati
- **Matplotlib** — per i grafici
- **Passlib[bcrypt]** — per la sicurezza delle password

---

## ⚙️ Installazione locale

1. Clona il repository:
   ```bash
   git clone https://github.com/Stefanus-dev/FinanceWebApp.git
   cd FinanceWebApp
Installa le dipendenze:
pip install -r requirements.txt

Avvia l’app:
streamlit run app.py

L’app sarà accessibile su:
http://localhost:8501

🌐 Deploy su Streamlit Cloud

L’app è compatibile e già pronta per il deploy su Streamlit Cloud.
Puoi provarla subito da questo link (se pubblico):

https://financewebapp-h9mbzlw2at8rvijg8sueln.streamlit.app/

🧾 Licenza

Questo progetto è distribuito sotto licenza MIT — sei libero di usarlo, modificarlo e condividerlo a fini didattici o personali.
Consulta il file LICENSE.

✨ Autore

Stefanus-dev

---

## 🤖 Integrazioni future con AI

FinanceWebApp è pensata per evolversi nel tempo con l’aiuto dell’intelligenza artificiale.

🚧 Idee già in fase di sviluppo:

- **Analisi intelligente delle spese:** un assistente AI che fornisce suggerimenti personalizzati per migliorare il tuo bilancio.  
- **Previsioni di spesa:** utilizzo di modelli predittivi per stimare le spese dei mesi successivi.  
- **Categorizzazione automatica:** riconoscimento automatico della categoria di ogni spesa (alimentari, trasporti, ecc.).  
- **Chatbot finanziario:** un assistente interattivo per rispondere a domande sul tuo andamento economico.

> In futuro sarà possibile integrare questi strumenti tramite API (es. OpenAI, Hugging Face, o modelli locali) per un’esperienza ancora più personalizzata.

---

