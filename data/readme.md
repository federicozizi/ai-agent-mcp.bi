# 📁 Cartella: data/

Questa cartella contiene i **dati locali** che l'agente AI può utilizzare, generare o salvare durante l'esecuzione. 
È una zona di lavoro dinamica che può contenere sia file di input (es. documenti da indicizzare), 
sia file di output (es. log delle conversazioni o esempi salvati). Di seguito trovi la descrizione delle sottocartelle principali.

---

## 📂 logs/

Questa sottocartella contiene i **log delle interazioni** o dei task eseguiti dall'agente.
Può includere:
- conversazioni salvate,
- task pianificati ed eseguiti,
- errori o esiti rilevanti,
- output grezzi dei moduli principali (planner, executor, memory...).

Questi log sono utili per:
- analizzare il comportamento dell'agente,
- fare debugging,
- conservare la storia delle sessioni (memoria a lungo termine esterna).

---

## 📂 examples/

Questa sottocartella contiene **dati di esempio** usati per i test o la documentazione.
Ad esempio:
- obiettivi di esempio da passare al planner,
- output generati da task specifici,
- file dimostrativi da usare nel vector store.

È utile per verificare il funzionamento dei moduli senza dover ogni volta creare dati da zero.

---

## 📁 Altri file

Puoi anche salvare singoli file direttamente in `data/` (es. file `.txt` o `.json`) 
che vuoi usare come input o esportazioni temporanee.  
La cartella può essere adattata in base alle esigenze del progetto, ma è consigliato mantenere una struttura ordinata 
usando le sottocartelle `logs/` ed `examples/`.

---

## 🔐 Importante

Questa cartella **non dovrebbe essere tracciata da Git** se contiene dati sensibili o generati dinamicamente.  
Aggiungila nel tuo `.gitignore` se necessario:

