<<<<<<< HEAD
# visualizer.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def mostra_grafico(df, frame):
    """Mostra un grafico a barre Entrate vs Uscite, in stile moderno."""
    for widget in frame.winfo_children():
        widget.destroy()

    if df.empty:
        from tkinter import Label
        Label(frame, text="Nessun dato disponibile.", font=("Arial", 12, "italic"), fg="#555").pack(pady=20)
        return

    # Calcolo dei totali
    df_group = df.groupby("Tipo")["Importo"].sum()
    tipi = df_group.index.tolist()
    importi = df_group.values.tolist()

    # Creazione figura
    fig, ax = plt.subplots(figsize=(5, 3.5), dpi=100)
    fig.patch.set_alpha(0)  # Sfondo trasparente
    ax.set_facecolor("white")

    # Colori moderni
    colori = ["#6EE7B7" if t == "Entrata" else "#FCA5A5" for t in tipi]
    barre = ax.bar(tipi, importi, color=colori, width=0.5, edgecolor="#444", linewidth=0.6)

    # Aggiunge i valori sopra le barre
    for rect, val in zip(barre, importi):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + (height * 0.02),
                f"{val:.2f}€", ha='center', va='bottom', fontsize=10, fontweight="bold")

    # Titolo e asse
    ax.set_title("Entrate vs Uscite", fontsize=13, fontweight="bold", color="#333")
    ax.set_ylabel("Importo (€)", fontsize=10, color="#333")
    ax.set_xlabel("")  # Rimuove etichetta asse x
    ax.grid(True, axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()

    # Mostra nel frame Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

# FinanceApp - Gestione Spese Mensili
# Copyright (c) 2025 [Stefanus-dev]
# Licenza: MIT (vedi file LICENSE)
=======
# visualizer.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def mostra_grafico(df, frame):
    """Mostra un grafico a barre Entrate vs Uscite, in stile moderno."""
    for widget in frame.winfo_children():
        widget.destroy()

    if df.empty:
        from tkinter import Label
        Label(frame, text="Nessun dato disponibile.", font=("Arial", 12, "italic"), fg="#555").pack(pady=20)
        return

    # Calcolo dei totali
    df_group = df.groupby("Tipo")["Importo"].sum()
    tipi = df_group.index.tolist()
    importi = df_group.values.tolist()

    # Creazione figura
    fig, ax = plt.subplots(figsize=(5, 3.5), dpi=100)
    fig.patch.set_alpha(0)  # Sfondo trasparente
    ax.set_facecolor("white")

    # Colori moderni
    colori = ["#6EE7B7" if t == "Entrata" else "#FCA5A5" for t in tipi]
    barre = ax.bar(tipi, importi, color=colori, width=0.5, edgecolor="#444", linewidth=0.6)

    # Aggiunge i valori sopra le barre
    for rect, val in zip(barre, importi):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + (height * 0.02),
                f"{val:.2f}€", ha='center', va='bottom', fontsize=10, fontweight="bold")

    # Titolo e asse
    ax.set_title("Entrate vs Uscite", fontsize=13, fontweight="bold", color="#333")
    ax.set_ylabel("Importo (€)", fontsize=10, color="#333")
    ax.set_xlabel("")  # Rimuove etichetta asse x
    ax.grid(True, axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()

    # Mostra nel frame Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)
>>>>>>> 7388ce14fe9e2429839ee3e4c8a1e52e62d467b9
