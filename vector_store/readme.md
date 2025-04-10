# 🧠 Cartella: vector_store/

Questa cartella contiene la gestione completa della **memoria vettoriale** dell'agente AI.  
È qui che vengono elaborati i documenti da cui l'agente può trarre conoscenza e richiamare informazioni 
durante l'interazione con l'utente.

---

## 📄 store.py

File principale che si occupa di:
- leggere ed estrarre testo da documenti (es. PDF, TXT...),
- generare embedding con l'API di OpenAI,
- salvare gli embedding in un indice FAISS locale,
- effettuare ricerche per similarità semantica.

Viene utilizzato per creare e interrogare il vector store dell’agente.

---

## 📂 data/

Questa sottocartella contiene i **documenti originali** che vuoi rendere accessibili all’agente AI.  
Puoi salvare file in formato `.pdf`, `.txt`, `.md` o altri testi da cui `store.py` estrae il contenuto per generare gli embedding.  
È a tutti gli effetti la **fonte informativa** della memoria vettoriale del sistema.

---

## 📄 vector.index & corpus.json

Questi file vengono **generati automaticamente** da `store.py`:

- `vector.index`: l’indice FAISS che contiene gli embedding (vettori numerici)
- `corpus.json`: l’elenco dei testi originali associati agli embedding, utile per sapere quale contenuto è stato memorizzato

> Entrambi i file vengono salvati nella cartella `vector_store/` e non dovrebbero essere tracciati da Git (aggiungili al `.gitignore`).

---

## 📄 __init__.py

Questo file rende la cartella `vector_store/` un **modulo Python importabile**, così puoi usare `store.py` da altri punti del progetto (es. `from vector_store import store`).

---

## ✅ In sintesi

Questa cartella rappresenta il "cervello passivo" dell’agente, cioè la sua capacità di **leggere documenti, memorizzarli come vettori** e poi recuperarli su richiesta con ricerche semantiche.
