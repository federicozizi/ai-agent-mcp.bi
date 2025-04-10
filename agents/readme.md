# 🧠 Cartella: agents/

Questa cartella contiene i **componenti principali dell'agente AI**, strutturati secondo l’architettura MCP (Multi-Component Pattern).  
Ogni file in questa cartella rappresenta una "parte del cervello" dell’agente, con una responsabilità specifica: pianificare, eseguire, ricordare o utilizzare strumenti esterni.

---

## 📄 base_agent.py

Classe base da cui gli altri moduli possono ereditare.  
Contiene funzioni comuni (es. logging, reset, setup) utili per standardizzare il comportamento dei vari componenti (planner, executor, memory...).

---

## 📄 planner.py

Riceve un **obiettivo** dall’utente e lo trasforma in una lista di **task eseguibili**.  
Utilizza l'API di ChatGPT per analizzare la richiesta e suddividerla in passaggi logici.

Esempio:  
Obiettivo: "Organizza una riunione di team"  
→ Task: "1. Verifica disponibilità", "2. Prepara un ordine del giorno", "3. Invia inviti"

---

## 📄 executor.py

Si occupa di **eseguire i task** uno alla volta.  
Può usare GPT, strumenti esterni o funzioni definite in `tools.py`.  
È responsabile di portare a termine i compiti generati dal planner e restituire un risultato utile.

---

## 📄 memory.py

Gestisce la **memoria temporanea o persistente** dell’agente.  
Può salvare:
- conversazioni passate
- task già svolti
- risultati ottenuti

Questo permette all’agente di mantenere un contesto anche tra più richieste.

---

## 📄 tools.py

Contiene **strumenti aggiuntivi** o utilità esterne che possono essere usate dall’executor.  
Ad esempio:
- chiamate API REST
- scraping di siti
- operazioni di sistema o file

I tool sono pensati per essere modulari e facilmente riutilizzabili.

---

## ✅ Struttura modulare e riutilizzabile

Grazie alla separazione in moduli:
- ogni componente può essere testato e migliorato indipendentemente
- è più facile estendere o
