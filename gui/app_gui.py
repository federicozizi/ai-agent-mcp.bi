"""
app_gui.py

Interfaccia grafica dell'agente AI usando customtkinter.
Questa GUI consente all'utente di inserire un obiettivo e visualizzare
i task suggeriti dal planner. Per ora la risposta è simulata,
ma è già pronta per collegare il backend reale.
"""

import customtkinter as ctk

# Imposta tema chiaro o scuro
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crea la finestra principale
app = ctk.CTk()
app.title("Agente AI - MCP")
app.geometry("600x500")


# Funzione da eseguire quando clicchi "Esegui"
def esegui_agente():
    obiettivo = input_entry.get()

    if not obiettivo.strip():
        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end")
        output_textbox.insert("end", "⚠️ Inserisci un obiettivo valido.")
        output_textbox.configure(state="disabled")
        return

    # ATTENZIONE
    # Simula una risposta (qui va collegato il planner vero con le task reali)
    tasks = [
        "1. Analizza il problema.",
        "2. Ricerca informazioni rilevanti.",
        "3. Genera una proposta di soluzione.",
    ]

    # Mostra i task in output
    output_textbox.configure(state="normal")
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", f"🎯 Obiettivo: {obiettivo}\n\n")
    output_textbox.insert("end", "\n".join(tasks))
    output_textbox.configure(state="disabled")


# ======= UI ELEMENTS =======

title_label = ctk.CTkLabel(app, text="Agente AI • MCP", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

input_entry = ctk.CTkEntry(app, width=500, height=40, placeholder_text="Inserisci un obiettivo...")
input_entry.pack(pady=10)

esegui_button = ctk.CTkButton(app, text="Esegui", command=esegui_agente)
esegui_button.pack(pady=10)

output_textbox = ctk.CTkTextbox(app, width=520, height=300)
output_textbox.pack(pady=20)
output_textbox.configure(state="disabled")

# Avvia la GUI
app.mainloop()
