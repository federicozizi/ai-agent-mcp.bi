# ⚙️ Cartella: config/

Questa cartella contiene i file di configurazione generali del progetto.  
Serve a centralizzare tutte le impostazioni chiave dell'agente AI, evitando di scrivere dati sensibili o modificabili direttamente nel codice.

---

## 📄 settings.yaml

Contiene le **impostazioni dell’agente AI** in formato leggibile.  
Può includere:
- il nome dell’agente o del ruolo GPT da usare,
- il modello OpenAI da chiamare (es. gpt-4, gpt-3.5-turbo),
- parametri di configurazione come temperature, massimo numero di step, ecc.

✅ Vantaggi:
- puoi modificare il comportamento del sistema senza toccare il codice
- è facile da leggere e aggiornare manualmente

---

## 📄 .env.example

Questo file è un **modello di esempio** per creare un file `.env` contenente le variabili d’ambiente.  
Ad esempio:

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx


Queste variabili vengono caricate automaticamente da Python (tramite `python-dotenv`) e ti permettono di:
- tenere le chiavi API **fuori dal codice**,
- non caricare informazioni sensibili su GitHub,
- personalizzare la configurazione in base all’ambiente (sviluppo, produzione...).

⚠️ Dopo aver copiato `.env.example` in `.env`, assicurati che il file `.env` sia incluso nel `.gitignore`.

---

## ✅ Suggerimenti

- Non tracciare `.env` su Git.
- Mantieni `settings.yaml` generico, senza dati sensibili.
- Se hai più ambienti (es. locale, cloud), puoi creare varianti come `settings.dev.yaml`, `settings.prod.yaml`, ecc.

