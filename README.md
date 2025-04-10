# ai-agent-mcp
Un agente AI in python usando l'architettura MCP, nella quale l'agente è diviso in più componenti specializzati

# Struttura del Progetto
Questo progetto è un'applicazione Python standalone basata su Multi-Component Pattern (MCP), con un agente AI che utilizza l'API di ChatGPT e un vector store personalizzato.

🧠 Componenti principali:
main.py
    È il cuore operativo dell'app. Quando lanci il progetto, questo file parte per primo. Qui vengono creati i moduli principali, viene assegnato un obiettivo all’agente e parte tutta la logica per risolverlo.

agents/
Contiene tutti i componenti che compongono l'agente AI, divisi secondo l’architettura MCP:

    - base_agent.py: classe base comune per altri moduli, con funzioni utili condivise.

    - planner.py: decide quali step eseguire a partire da un obiettivo.

    - executor.py: esegue i task generati dal planner, anche con GPT o strumenti esterni.

    - memory.py: tiene traccia della memoria del sistema (storia delle conversazioni, task svolti...).

    - tools.py: strumenti esterni accessori, come chiamate API, scraping, ecc.

api/
Gestisce tutto ciò che riguarda l'interazione con l'API di ChatGPT:

    - client.py: wrapper per semplificare le chiamate a GPT.

    - prompts.py: prompt predefiniti organizzati come costanti.

    - templates/: prompt più lunghi salvati in file .txt separati.

vector_store/
Contiene la logica per la memoria a lungo termine tramite FAISS e embedding:

    - store.py: crea embedding da documenti e gestisce l'indice FAISS.

    - data/: cartella dove inserire PDF o file testuali da indicizzare.

    - __init__.py: dice a Python che questa è una cartella importabile come modulo.

config/
Contiene configurazioni e chiavi API:

    - settings.yaml: parametri configurabili come modello GPT, temperature, ruoli, ecc.

    - .env.example: esempio di file .env dove inserire la tua chiave OpenAI.

gui/
Contiene tutto ciò che riguarda la user interface (front-end)
    - app_gui.py: interfaccia utente

tests/
Test automatici per controllare che ogni componente funzioni correttamente. Ogni file di test verifica un modulo specifico, come planner, executor, tools, ecc.

Altri file utili
README.md: questa guida, utile per capire come funziona il progetto.

clean_git.bat: se startato in console pulisce la cache di git e la riaggiorna in base alle specifiche del gitignore modificate

requirements.txt: librerie da installare per far girare l’app (pip install -r requirements.txt).

LICENSE: licenza del progetto (es. MIT, GPL, ecc.).

# Logica sviluppo
Le fasi di sviluppo dell'app

1. Crea la GUI base con customtkinter
Campo input
Bottone “Esegui”
Area output
Simula la risposta dell’agente con dati finti (es. ["Task 1", "Task 2"])
2. Collega il planner reale
Usa l’API OpenAI solo nel momento in cui premi il bottone
Mostra i risultati del planner nella GUI
3. Collega l’executor e gli altri moduli (uno alla volta)
Integra memoria, retrieval, tools, ecc.
4. Rifinisci la GUI
Loading spinner, dark/light toggle, stile, ecc.

# Testing
Per test Generali
1. Assicurarsi di essere nella cartella giusta
2. Lanciare:
    - python vector_store/store.py : serve per aggiornare il vector store
    - app_gui.py : lancia l'interfaccia GUI

Per debuggare singoli moduli
- python agents/planner.py : se ha un blocco __main__ per test locali
oppure usare un file test come
- pytest tests/

