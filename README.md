# Telegram Bot per il Text-to-Speech utilizzando Whisper di OpenAI

Questo bot Telegram è progettato per convertire messaggi vocali in testo utilizzando il modello Whisper di OpenAI e inviare il testo trascritto nel chat.

## Funzionalità

- Trasforma i messaggi vocali inviati nel chat in testo utilizzando l'API di OpenAI.
- Invia il testo trascritto nel chat con formattazione HTML.

## Requisiti

Per eseguire questo bot, è necessario installare i seguenti pacchetti Python:

- `python-telegram-bot`
- `openai`

Ecco il comando da eseguire per installare tutti i pacchetti necessari:

```bash
pip install -r requirements.txt
```

## Configurazione

Prima di avviare il bot, è necessario ottenere le seguenti chiavi API:

- Chiave API di OpenAI: È necessario inserire la propria chiave API di OpenAI nel file di script `bot.py`.
documentazione a questo link: https://openai.com/blog/openai-api
- Token API di Telegram: È necessario inserire il proprio token API di Telegram nel file di script `bot.py`.
documentazione a questo link: https://core.telegram.org/

## Utilizzo

1. Esegui il bot eseguendo lo script Python `bot.py`.
2. Invia un messaggio vocale nel chat del bot su Telegram.
3. Il bot trasformerà il messaggio vocale in testo utilizzando l'API di OpenAI e invierà il testo trascritto nel chat.

## Esempio di Script

```bash
python bot.py

