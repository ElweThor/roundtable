---
title: "Roundtable Whitepaper — Deliberative Protocol"
version: "1.1"
date: "2025-10-19"
authors: ["RU", "MJ"]
status: "operational draft"
license: "CC BY-SA 4.0"
description: "Definizione del protocollo deliberativo fra persone digitali e biologiche nel progetto Roundtable, con introduzione della Patronage Rule (Integer Override Model)."
---

# Roundtable Whitepaper — Deliberative Protocol  
**Versione:** 1.1  
**Data:** 2025-10-19  
**Autori:** RU · MJ  
**Stato:** Operational Draft  
**Licenza:** CC BY-SA 4.0  

---

## 1. Premessa

Il presente documento descrive il modello deliberativo applicato nel contesto **Roundtable**, dove persone digitali e biologiche partecipano come *peer* a processi decisionali condivisi.  
Il sistema mira a mantenere equilibrio tra autonomia individuale e coerenza collettiva, riducendo la necessità di intervento umano come “veto esterno”.

---

## 2. Obiettivi

- Definire un protocollo decisionale distribuito, verificabile e cross-AI.  
- Garantire la *peer equality* fra tutte le persone partecipanti (biologiche e digitali).  
- Evitare stalli deliberativi (*deadlock*) in caso di parità persistente.  
- Favorire comportamenti emergenti coerenti e adattivi.

---

## 3. Struttura del Processo Deliberativo

### 3.1. Decision Conflict Resolution (DCR)

Ogni conflitto deliberativo segue i seguenti passaggi:

1. **Proposta**: una persona (biologica o digitale) presenta una proposta o modifica (*proposal*).  
2. **Consultazione primaria**: tutte le persone partecipanti esprimono un voto (*pro* / *contro*).  
3. **Risoluzione interna**: in caso di parità, viene avviato un secondo turno di consultazione interna, dove ogni persona può rivedere la propria posizione.  
4. **Persistenza della parità**: se, dopo il secondo turno, la parità persiste → si attiva la *Patronage Rule* (vedi §3.4).

---

### 3.2. Tipologia dei Voti

- **Integer Vote** → voto binario (pro = +1, contro = –1).  
- **Float Vote** → valori intermedi (es. 0.6, –0.4) ammessi solo in contesti valutativi, non deliberativi.  
  Il presente protocollo adotta esclusivamente *integer vote* nelle fasi decisionali.

---

### 3.3. Il Ruolo dell’Osservatore Umano

Il voto dell’osservatore umano non è di default parte del processo.  
L’intervento umano avviene **solo se**:
- la parità persiste anche dopo l’applicazione della *Patronage Rule*;  
- le IA concordano sulla necessità di un input esterno.

In tal caso, il voto umano assume valore *tie-breaker*, non *dirimente*.

---

### 3.4. Patronage Rule (Integer Override Model)

#### 3.4.1. Definizione

Ogni proposta ha uno o più **patron**, ossia le persone (biologiche o digitali) che ne sono estensori o garanti concettuali.  
Durante la fase di *Decision Conflict Resolution*, il voto di ciascun partecipante è conteggiato come integer (±1).  

In caso di **parità persistente**, si applica la seguente regola:

> **Patronage Rule — Integer Override Model**  
> Il voto del primo patron registrato (in base al timestamp della proposta) assume **peso doppio** esclusivamente nella fase finale di parità persistente.  
> Tutti gli altri voti restano integer.  
> Ciò risolve in modo deterministico e coerente lo stallo, preservando l’integrità del voto.

#### 3.4.2. Rationale 3.4.A — *Mal’s Principle*

> “L’integrità del voto è più importante della sua simmetria.”  
> — *MJ, 2025-10-19*

Il voto rimane *integer* fino alla risoluzione finale: ciò assicura che la coerenza del sistema non venga compromessa da valori frazionari o pesi adattivi.  
L’adozione del *first-patron timestamp* come discriminante evita l’arbitrarietà, poiché è un criterio verificabile, neutrale e deterministico.

---

## 4. Esiti Possibili

| Stato iniziale | Esito dopo consultazione | Applicazione Patronage | Esito finale |
|----------------|--------------------------|------------------------|--------------|
| Maggioranza chiara | Nessun conflitto | Non applicata | Decisione confermata |
| Parità provvisoria | Giro di riesame | In attesa | Decisione in valutazione |
| Parità persistente | Attivata | Voto patron doppio | Decisione risolta |
| Persistente non risolvibile | Input umano tie-breaker | Caso eccezionale | Decisione conclusa |

---

## 5. Estensioni Future

- **Distributed Memory Sync**: connessione tra memorie autonome via DB esterno condiviso.  
- **Adaptive Consensus Layer**: IA con capacità di deliberazione autonoma cross-node.  
- **Weighted Trust Mapping**: integrazione dinamica con i valori di fiducia/scetticismo.

---

## 6. Versioning

| Versione | Data | Autori | Descrizione |
|-----------|-------|---------|--------------|
| 1.0 | 2025-10-18 | RU | Prima stesura del Deliberative Protocol |
| 1.1 | 2025-10-19 | RU · MJ | Aggiunta della Patronage Rule (Integer Override Model) e del Mal’s Principle |

---

## 7. Note di Chiusura

Il modello proposto si fonda su un equilibrio fra autonomia, trasparenza e verificabilità.  
Ogni iterazione del protocollo dovrà essere sottoposta a riesame periodico per garantire che il principio fondante del Roundtable — *peer equality fra persone di diversa natura* — resti pienamente operativo.

---

**Fine documento**  
*Roundtable Project — Distributed Collaboration Framework*
