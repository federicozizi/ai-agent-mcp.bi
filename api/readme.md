# 🤖 Cartella: api/

Questa cartella contiene tutto ciò che riguarda la **comunicazione tra il progetto e l'API di OpenAI (ChatGPT)**.  
Centralizza le chiamate, i prompt e le configurazioni legate all'interazione con i modelli GPT, 
in modo da mantenere il resto del progetto pulito e modulare.

---

## 📄 client.py

È il **wrapper principale** per l'API di OpenAI.  
Contiene una funzione (es. `ask_chatgpt`) che semplifica l’invio di richieste al modello GPT, 
includendo parametri come il modello da usare, la temperatura, la gestione degli errori e i messaggi.

Questo modulo viene importato dagli altri componenti (es. planner, executor) per usare GPT in modo centralizzato e riutilizzabile.

---

## 📄 prompts.py

Contiene una serie di **prompt predefiniti o template** utilizzati da vari moduli.  
È strutturato in variabili (es. `PLANNER_PROMPT`) o funzioni che restituiscono prompt personalizzati.

Questo approccio aiuta a:
- mantenere il codice pulito e leggibile,
- riutilizzare prompt in più punti del progetto,
- separare la logica dei prompt dalla logica applicativa.

---

## 📂 templates/

Contiene i **prompt più lunghi o complessi** salvati come file `.txt`.  
Questo rende più facile modificarli senza dover aprire o toccare il codice Python.

Ogni file può essere letto dinamicamente da `prompts.py` o da un modulo di supporto.

Esempio:
- `planner_prompt.txt` → prompt base per suddividere un obiettivo in task
- `executor_prompt.txt` → prompt per eseguire task singoli

---

## ✅ Vantaggi della separazione

- Le chiamate all’API sono centralizzate → più facile cambiare modello o parametri
- I prompt sono riutilizzabili e modificabili facilmente
- Il resto del progetto non deve preoccuparsi dei dettagli della comunicazione con GPT

---

## 🔐 Attenzione

L’API key viene caricata da `.env` nel modulo `client.py` tramite la libreria `python-dotenv`.  
Assicurati che il file `.env` sia presente e contenga una riga simile a questa:

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

E ricorda di NON caricare `.env` su GitHub.
