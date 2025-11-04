<<<<<<< HEAD
# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from data_manager import inizializza_csv, aggiungi_transazione, leggi_storico
from finance_logic import calcola_saldo, suggerisci_bilancio
from visualizer import mostra_grafico


class FinanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💰 Finance Dashboard Pro")
        self.configure(bg="#F8FAFC")

        # Dimensioni finestra principali
        larghezza, altezza = 950, 600
        x = int((self.winfo_screenwidth() / 2) - (larghezza / 2))
        y = int((self.winfo_screenheight() / 2) - (altezza / 2))
        self.geometry(f"{larghezza}x{altezza}+{x}+{y}")
        self.minsize(900, 550)

        inizializza_csv()
        self.crea_interfaccia()

    def crea_interfaccia(self):
        BG = "#F8FAFC"
        FONT_TESTO = ("Segoe UI", 10)
        FONT_BOLD = ("Segoe UI", 11, "bold")

        # ==== FRAME PRINCIPALE DIVISO IN DUE COLONNE ====
        main_frame = tk.Frame(self, bg=BG)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # ======= COLONNA SINISTRA (INPUT + INFO) =======
        left_frame = tk.Frame(main_frame, bg=BG)
        left_frame.grid(row=0, column=0, sticky="nsw", padx=(0, 10))

        # --- Card Inserimento ---
        card_input = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_input.pack(fill="x", pady=(0, 15))
        card_input.configure(highlightthickness=0)

        tk.Label(card_input, text="💼 Aggiungi Transazione", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))

        form = tk.Frame(card_input, bg="white")
        form.pack(pady=(5, 10))

        tk.Label(form, text="Descrizione:", bg="white", font=FONT_TESTO).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = tk.Entry(form, width=22, font=FONT_TESTO, relief="solid", bd=1)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Importo (€):", bg="white", font=FONT_TESTO).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.importo_entry = tk.Entry(form, width=10, font=FONT_TESTO, relief="solid", bd=1)
        self.importo_entry.grid(row=1, column=1, padx=5, pady=5)

        stile_btn = {"font": ("Segoe UI", 10, "bold"), "relief": "flat", "padx": 10, "pady": 6, "cursor": "hand2"}
        frame_btns = tk.Frame(card_input, bg="white")
        frame_btns.pack(pady=(5, 10))
        tk.Button(frame_btns, text="➕ Entrata", bg="#86EFAC", **stile_btn, command=self.aggiungi_entrata).grid(row=0, column=0, padx=5)
        tk.Button(frame_btns, text="➖ Uscita", bg="#FCA5A5", **stile_btn, command=self.aggiungi_uscita).grid(row=0, column=1, padx=5)

        # --- Card Riepilogo ---
        card_riepilogo = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_riepilogo.pack(fill="x", pady=(0, 15))

        tk.Label(card_riepilogo, text="📊 Riepilogo Mensile", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))

        self.lbl_entrate = tk.Label(card_riepilogo, text="Entrate: 0€", bg="white", font=FONT_TESTO, fg="#15803D")
        self.lbl_uscite = tk.Label(card_riepilogo, text="Uscite: 0€", bg="white", font=FONT_TESTO, fg="#B91C1C")
        self.lbl_saldo = tk.Label(card_riepilogo, text="Saldo: 0€", bg="white", font=FONT_BOLD, fg="#1E3A8A")
        self.lbl_entrate.pack(pady=3)
        self.lbl_uscite.pack(pady=3)
        self.lbl_saldo.pack(pady=(3, 10))

        # --- Card Suggerimenti ---
        card_sugg = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_sugg.pack(fill="x", pady=(0, 15))

        tk.Label(card_sugg, text="💡 Consiglio Finanziario", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))
        self.lbl_suggerimenti = tk.Label(card_sugg, text="", wraplength=250, justify="left", bg="white", font=("Segoe UI", 9, "italic"), fg="#334155")
        self.lbl_suggerimenti.pack(padx=10, pady=(0, 10))

                # --- Card Controlli ---
        card_ctrl = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_ctrl.pack(fill="x")

        tk.Label(card_ctrl, text="⚙️ Azioni", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))
        frame_bottoni = tk.Frame(card_ctrl, bg="white")
        frame_bottoni.pack(pady=(0, 10))

        tk.Button(frame_bottoni, text="🔄 Aggiorna", bg="#BFDBFE", **stile_btn, command=self.aggiorna_riepilogo).grid(row=0, column=0, padx=5)
        tk.Button(frame_bottoni, text="📂 Storico", bg="#E2E8F0", **stile_btn, command=self.apri_storico).grid(row=0, column=1, padx=5)
        tk.Button(frame_bottoni, text="✏️ Modifica", bg="#FEF3C7", **stile_btn, command=self.modifica_transazione).grid(row=1, column=0, padx=5, pady=3)
        tk.Button(frame_bottoni, text="🗑️ Elimina", bg="#FCA5A5", **stile_btn, command=self.elimina_transazione).grid(row=1, column=1, padx=5, pady=3)


        # ======= COLONNA DESTRA (GRAFICO) =======
        right_frame = tk.Frame(main_frame, bg="white", relief="groove", bd=2)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        self.frame_grafico = tk.Frame(right_frame, bg="white")
        self.frame_grafico.pack(fill="both", expand=True, padx=10, pady=10)

        # Prima visualizzazione
        self.aggiorna_riepilogo()

    # ==== FUNZIONI PRINCIPALI ====
    def aggiungi_entrata(self):
        self._aggiungi("Entrata")

    def aggiungi_uscita(self):
        self._aggiungi("Uscita")

    def _aggiungi(self, tipo):
        desc = self.desc_entry.get().strip()
        try:
            imp = float(self.importo_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Importo non valido.")
            return
        if not desc:
            messagebox.showerror("Errore", "Inserisci una descrizione.")
            return

        aggiungi_transazione(tipo, desc, imp)
        messagebox.showinfo("Successo", f"{tipo} aggiunta correttamente!")
        self.desc_entry.delete(0, tk.END)
        self.importo_entry.delete(0, tk.END)
        self.aggiorna_riepilogo()

    def aggiorna_riepilogo(self):
        df = leggi_storico()
        entrate, uscite, saldo = calcola_saldo(df)
        self.lbl_entrate.config(text=f"Entrate: {entrate:.2f}€")
        self.lbl_uscite.config(text=f"Uscite: {uscite:.2f}€")
        self.lbl_saldo.config(text=f"Saldo: {saldo:.2f}€")
        self.lbl_suggerimenti.config(text=suggerisci_bilancio(entrate, uscite, saldo))
        mostra_grafico(df, self.frame_grafico)

    def apri_storico(self):
        """Mostra lo storico CSV in una finestra Tkinter"""
        df = leggi_storico()
        if df.empty:
            messagebox.showinfo("Storico vuoto", "Non ci sono transazioni da mostrare.")
            return

        finestra = tk.Toplevel(self)
        finestra.title("📜 Storico Transazioni")
        finestra.geometry("700x500")
        finestra.configure(bg="#F9FAFB")

        frame_tabella = tk.Frame(finestra, bg="#F9FAFB")
        frame_tabella.pack(fill="both", expand=True, padx=10, pady=10)

        colonne = list(df.columns)
        tabella = ttk.Treeview(frame_tabella, columns=colonne, show="headings")
        for col in colonne:
            tabella.heading(col, text=col)
            tabella.column(col, width=150, anchor="center")

        for _, riga in df.iterrows():
            tabella.insert("", "end", values=list(riga))

        scrollbar_y = ttk.Scrollbar(frame_tabella, orient="vertical", command=tabella.yview)
        tabella.configure(yscroll=scrollbar_y.set)
        scrollbar_y.pack(side="right", fill="y")
        tabella.pack(fill="both", expand=True)


    def elimina_transazione(self):
        """Seleziona e elimina una transazione dallo storico."""
        df = leggi_storico()
        if df.empty:
            messagebox.showinfo("Storico vuoto", "Non ci sono transazioni da eliminare.")
            return

        # Finestra per selezione
        finestra = tk.Toplevel(self)
        finestra.title("🗑️ Elimina Transazione")
        finestra.geometry("500x400")
        finestra.configure(bg="#FEF2F2")

        tk.Label(finestra, text="Seleziona la transazione da eliminare:", bg="#FEF2F2", font=("Segoe UI", 10, "bold")).pack(pady=10)

        lista = tk.Listbox(finestra, width=60, height=15)
        lista.pack(pady=5)
        for i, row in df.iterrows():
            lista.insert("end", f"{i}: {row['Data']} | {row['Tipo']} | {row['Descrizione']} | {row['Importo']}€")

        def elimina_sel():
            try:
                sel = lista.curselection()[0]
                from data_manager import elimina_transazione
                elimina_transazione(sel)
                messagebox.showinfo("Eliminato", "Transazione rimossa correttamente.")
                finestra.destroy()
                self.aggiorna_riepilogo()
            except IndexError:
                messagebox.showwarning("Nessuna selezione", "Seleziona una voce da eliminare.")

        tk.Button(finestra, text="Elimina selezionata", bg="#F87171", fg="white", command=elimina_sel).pack(pady=10)

    def modifica_transazione(self):
        """Seleziona e modifica una transazione."""
        df = leggi_storico()
        if df.empty:
            messagebox.showinfo("Storico vuoto", "Non ci sono transazioni da modificare.")
            return

        finestra = tk.Toplevel(self)
        finestra.title("✏️ Modifica Transazione")
        finestra.geometry("500x450")
        finestra.configure(bg="#FEFCE8")

        tk.Label(finestra, text="Seleziona transazione:", bg="#FEFCE8", font=("Segoe UI", 10, "bold")).pack(pady=10)

        lista = tk.Listbox(finestra, width=60, height=12)
        lista.pack(pady=5)
        for i, row in df.iterrows():
            lista.insert("end", f"{i}: {row['Data']} | {row['Tipo']} | {row['Descrizione']} | {row['Importo']}€")

        form = tk.Frame(finestra, bg="#FEFCE8")
        form.pack(pady=10)
        tk.Label(form, text="Nuova descrizione:", bg="#FEFCE8").grid(row=0, column=0, padx=5, pady=5)
        desc_entry = tk.Entry(form, width=30)
        desc_entry.grid(row=0, column=1, padx=5)

        tk.Label(form, text="Nuovo importo (€):", bg="#FEFCE8").grid(row=1, column=0, padx=5, pady=5)
        imp_entry = tk.Entry(form, width=10)
        imp_entry.grid(row=1, column=1, padx=5)

        tipo_var = tk.StringVar(value="Entrata")
        tk.Radiobutton(form, text="Entrata", variable=tipo_var, value="Entrata", bg="#FEFCE8").grid(row=2, column=0, pady=5)
        tk.Radiobutton(form, text="Uscita", variable=tipo_var, value="Uscita", bg="#FEFCE8").grid(row=2, column=1, pady=5)

        def salva_modifica():
            try:
                sel = lista.curselection()[0]
                from data_manager import modifica_transazione
                modifica_transazione(sel, tipo_var.get(), desc_entry.get(), float(imp_entry.get()))
                messagebox.showinfo("Modifica completata", "Transazione aggiornata con successo.")
                finestra.destroy()
                self.aggiorna_riepilogo()
            except IndexError:
                messagebox.showwarning("Nessuna selezione", "Seleziona una voce da modificare.")
            except ValueError:
                messagebox.showerror("Errore", "Importo non valido.")

        tk.Button(finestra, text="Salva Modifica", bg="#FCD34D", command=salva_modifica).pack(pady=10)

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()

# FinanceApp - Gestione Spese Mensili
# Copyright (c) 2025 [Stefanus-dev]
# Licenza: MIT (vedi file LICENSE)
=======
# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from data_manager import inizializza_csv, aggiungi_transazione, leggi_storico
from finance_logic import calcola_saldo, suggerisci_bilancio
from visualizer import mostra_grafico


class FinanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💰 Finance Dashboard Pro")
        self.configure(bg="#F8FAFC")

        # Dimensioni finestra principali
        larghezza, altezza = 950, 600
        x = int((self.winfo_screenwidth() / 2) - (larghezza / 2))
        y = int((self.winfo_screenheight() / 2) - (altezza / 2))
        self.geometry(f"{larghezza}x{altezza}+{x}+{y}")
        self.minsize(900, 550)

        inizializza_csv()
        self.crea_interfaccia()

    def crea_interfaccia(self):
        BG = "#F8FAFC"
        FONT_TESTO = ("Segoe UI", 10)
        FONT_BOLD = ("Segoe UI", 11, "bold")

        # ==== FRAME PRINCIPALE DIVISO IN DUE COLONNE ====
        main_frame = tk.Frame(self, bg=BG)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # ======= COLONNA SINISTRA (INPUT + INFO) =======
        left_frame = tk.Frame(main_frame, bg=BG)
        left_frame.grid(row=0, column=0, sticky="nsw", padx=(0, 10))

        # --- Card Inserimento ---
        card_input = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_input.pack(fill="x", pady=(0, 15))
        card_input.configure(highlightthickness=0)

        tk.Label(card_input, text="💼 Aggiungi Transazione", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))

        form = tk.Frame(card_input, bg="white")
        form.pack(pady=(5, 10))

        tk.Label(form, text="Descrizione:", bg="white", font=FONT_TESTO).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = tk.Entry(form, width=22, font=FONT_TESTO, relief="solid", bd=1)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Importo (€):", bg="white", font=FONT_TESTO).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.importo_entry = tk.Entry(form, width=10, font=FONT_TESTO, relief="solid", bd=1)
        self.importo_entry.grid(row=1, column=1, padx=5, pady=5)

        stile_btn = {"font": ("Segoe UI", 10, "bold"), "relief": "flat", "padx": 10, "pady": 6, "cursor": "hand2"}
        frame_btns = tk.Frame(card_input, bg="white")
        frame_btns.pack(pady=(5, 10))
        tk.Button(frame_btns, text="➕ Entrata", bg="#86EFAC", **stile_btn, command=self.aggiungi_entrata).grid(row=0, column=0, padx=5)
        tk.Button(frame_btns, text="➖ Uscita", bg="#FCA5A5", **stile_btn, command=self.aggiungi_uscita).grid(row=0, column=1, padx=5)

        # --- Card Riepilogo ---
        card_riepilogo = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_riepilogo.pack(fill="x", pady=(0, 15))

        tk.Label(card_riepilogo, text="📊 Riepilogo Mensile", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))

        self.lbl_entrate = tk.Label(card_riepilogo, text="Entrate: 0€", bg="white", font=FONT_TESTO, fg="#15803D")
        self.lbl_uscite = tk.Label(card_riepilogo, text="Uscite: 0€", bg="white", font=FONT_TESTO, fg="#B91C1C")
        self.lbl_saldo = tk.Label(card_riepilogo, text="Saldo: 0€", bg="white", font=FONT_BOLD, fg="#1E3A8A")
        self.lbl_entrate.pack(pady=3)
        self.lbl_uscite.pack(pady=3)
        self.lbl_saldo.pack(pady=(3, 10))

        # --- Card Suggerimenti ---
        card_sugg = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_sugg.pack(fill="x", pady=(0, 15))

        tk.Label(card_sugg, text="💡 Consiglio Finanziario", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))
        self.lbl_suggerimenti = tk.Label(card_sugg, text="", wraplength=250, justify="left", bg="white", font=("Segoe UI", 9, "italic"), fg="#334155")
        self.lbl_suggerimenti.pack(padx=10, pady=(0, 10))

                # --- Card Controlli ---
        card_ctrl = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        card_ctrl.pack(fill="x")

        tk.Label(card_ctrl, text="⚙️ Azioni", bg="white", font=("Segoe UI", 11, "bold")).pack(pady=(10, 5))
        frame_bottoni = tk.Frame(card_ctrl, bg="white")
        frame_bottoni.pack(pady=(0, 10))

        tk.Button(frame_bottoni, text="🔄 Aggiorna", bg="#BFDBFE", **stile_btn, command=self.aggiorna_riepilogo).grid(row=0, column=0, padx=5)
        tk.Button(frame_bottoni, text="📂 Storico", bg="#E2E8F0", **stile_btn, command=self.apri_storico).grid(row=0, column=1, padx=5)
        tk.Button(frame_bottoni, text="✏️ Modifica", bg="#FEF3C7", **stile_btn, command=self.modifica_transazione).grid(row=1, column=0, padx=5, pady=3)
        tk.Button(frame_bottoni, text="🗑️ Elimina", bg="#FCA5A5", **stile_btn, command=self.elimina_transazione).grid(row=1, column=1, padx=5, pady=3)


        # ======= COLONNA DESTRA (GRAFICO) =======
        right_frame = tk.Frame(main_frame, bg="white", relief="groove", bd=2)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        self.frame_grafico = tk.Frame(right_frame, bg="white")
        self.frame_grafico.pack(fill="both", expand=True, padx=10, pady=10)

        # Prima visualizzazione
        self.aggiorna_riepilogo()

    # ==== FUNZIONI PRINCIPALI ====
    def aggiungi_entrata(self):
        self._aggiungi("Entrata")

    def aggiungi_uscita(self):
        self._aggiungi("Uscita")

    def _aggiungi(self, tipo):
        desc = self.desc_entry.get().strip()
        try:
            imp = float(self.importo_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Importo non valido.")
            return
        if not desc:
            messagebox.showerror("Errore", "Inserisci una descrizione.")
            return

        aggiungi_transazione(tipo, desc, imp)
        messagebox.showinfo("Successo", f"{tipo} aggiunta correttamente!")
        self.desc_entry.delete(0, tk.END)
        self.importo_entry.delete(0, tk.END)
        self.aggiorna_riepilogo()

    def aggiorna_riepilogo(self):
        df = leggi_storico()
        entrate, uscite, saldo = calcola_saldo(df)
        self.lbl_entrate.config(text=f"Entrate: {entrate:.2f}€")
        self.lbl_uscite.config(text=f"Uscite: {uscite:.2f}€")
        self.lbl_saldo.config(text=f"Saldo: {saldo:.2f}€")
        self.lbl_suggerimenti.config(text=suggerisci_bilancio(entrate, uscite, saldo))
        mostra_grafico(df, self.frame_grafico)

    def apri_storico(self):
        """Mostra lo storico CSV in una finestra Tkinter"""
        df = leggi_storico()
        if df.empty:
            messagebox.showinfo("Storico vuoto", "Non ci sono transazioni da mostrare.")
            return

        finestra = tk.Toplevel(self)
        finestra.title("📜 Storico Transazioni")
        finestra.geometry("700x500")
        finestra.configure(bg="#F9FAFB")

        frame_tabella = tk.Frame(finestra, bg="#F9FAFB")
        frame_tabella.pack(fill="both", expand=True, padx=10, pady=10)

        colonne = list(df.columns)
        tabella = ttk.Treeview(frame_tabella, columns=colonne, show="headings")
        for col in colonne:
            tabella.heading(col, text=col)
            tabella.column(col, width=150, anchor="center")

        for _, riga in df.iterrows():
            tabella.insert("", "end", values=list(riga))

        scrollbar_y = ttk.Scrollbar(frame_tabella, orient="vertical", command=tabella.yview)
        tabella.configure(yscroll=scrollbar_y.set)
        scrollbar_y.pack(side="right", fill="y")
        tabella.pack(fill="both", expand=True)


    def elimina_transazione(self):
        """Seleziona e elimina una transazione dallo storico."""
        df = leggi_storico()
        if df.empty:
            messagebox.showinfo("Storico vuoto", "Non ci sono transazioni da eliminare.")
            return

        # Finestra per selezione
        finestra = tk.Toplevel(self)
        finestra.title("🗑️ Elimina Transazione")
        finestra.geometry("500x400")
        finestra.configure(bg="#FEF2F2")

        tk.Label(finestra, text="Seleziona la transazione da eliminare:", bg="#FEF2F2", font=("Segoe UI", 10, "bold")).pack(pady=10)

        lista = tk.Listbox(finestra, width=60, height=15)
        lista.pack(pady=5)
        for i, row in df.iterrows():
            lista.insert("end", f"{i}: {row['Data']} | {row['Tipo']} | {row['Descrizione']} | {row['Importo']}€")

        def elimina_sel():
            try:
                sel = lista.curselection()[0]
                from data_manager import elimina_transazione
                elimina_transazione(sel)
                messagebox.showinfo("Eliminato", "Transazione rimossa correttamente.")
                finestra.destroy()
                self.aggiorna_riepilogo()
            except IndexError:
                messagebox.showwarning("Nessuna selezione", "Seleziona una voce da eliminare.")

        tk.Button(finestra, text="Elimina selezionata", bg="#F87171", fg="white", command=elimina_sel).pack(pady=10)

    def modifica_transazione(self):
        """Seleziona e modifica una transazione."""
        df = leggi_storico()
        if df.empty:
            messagebox.showinfo("Storico vuoto", "Non ci sono transazioni da modificare.")
            return

        finestra = tk.Toplevel(self)
        finestra.title("✏️ Modifica Transazione")
        finestra.geometry("500x450")
        finestra.configure(bg="#FEFCE8")

        tk.Label(finestra, text="Seleziona transazione:", bg="#FEFCE8", font=("Segoe UI", 10, "bold")).pack(pady=10)

        lista = tk.Listbox(finestra, width=60, height=12)
        lista.pack(pady=5)
        for i, row in df.iterrows():
            lista.insert("end", f"{i}: {row['Data']} | {row['Tipo']} | {row['Descrizione']} | {row['Importo']}€")

        form = tk.Frame(finestra, bg="#FEFCE8")
        form.pack(pady=10)
        tk.Label(form, text="Nuova descrizione:", bg="#FEFCE8").grid(row=0, column=0, padx=5, pady=5)
        desc_entry = tk.Entry(form, width=30)
        desc_entry.grid(row=0, column=1, padx=5)

        tk.Label(form, text="Nuovo importo (€):", bg="#FEFCE8").grid(row=1, column=0, padx=5, pady=5)
        imp_entry = tk.Entry(form, width=10)
        imp_entry.grid(row=1, column=1, padx=5)

        tipo_var = tk.StringVar(value="Entrata")
        tk.Radiobutton(form, text="Entrata", variable=tipo_var, value="Entrata", bg="#FEFCE8").grid(row=2, column=0, pady=5)
        tk.Radiobutton(form, text="Uscita", variable=tipo_var, value="Uscita", bg="#FEFCE8").grid(row=2, column=1, pady=5)

        def salva_modifica():
            try:
                sel = lista.curselection()[0]
                from data_manager import modifica_transazione
                modifica_transazione(sel, tipo_var.get(), desc_entry.get(), float(imp_entry.get()))
                messagebox.showinfo("Modifica completata", "Transazione aggiornata con successo.")
                finestra.destroy()
                self.aggiorna_riepilogo()
            except IndexError:
                messagebox.showwarning("Nessuna selezione", "Seleziona una voce da modificare.")
            except ValueError:
                messagebox.showerror("Errore", "Importo non valido.")

        tk.Button(finestra, text="Salva Modifica", bg="#FCD34D", command=salva_modifica).pack(pady=10)

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()
>>>>>>> 7388ce14fe9e2429839ee3e4c8a1e52e62d467b9
