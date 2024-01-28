# TELEGRAM BOT PER IL TEXT-TO-SPEECH CHE UTILIZZA WHISPER DI OPENAI

from telegram.ext import Updater, MessageHandler, Filters
from openai import OpenAI
import html
import os

OPENAI_API_KEY = "<inserisci la tua api key di OPENAI qui>"
TELEGRAM_API_TOKEN = "<inserisci la tua api key di TELEGRAM qui>"

# Inizializza il client OpenAI
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio(audio_file_path):
    # Esegui la trascrizione dell'audio utilizzando l'API di OpenAI
    with open(audio_file_path, "rb") as audio_file:
        transcript = openai_client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="it"
        )
    return transcript.text

def voice_message(update, context):
    # Get the voice message object
    voice = update.message.voice
    file_id = voice.file_id

    # Get the username of the sender
    user_name = update.message.from_user.first_name

    # Download the audio file
    new_file = context.bot.get_file(file_id)
    file_path = new_file.download()

    # Transcribe the audio
    transcribed_text = transcribe_audio(file_path)

    # Escape HTML characters in the transcribed text
    transcribed_text = html.escape(transcribed_text)

    # Format the transcribed text for better readability
    transcribed_text = transcribed_text.replace("\n", "\n\n")

    # Construct the personalized message with HTML formatting
    personalized_message = f'<b>{user_name}</b> dice:\n<i>"{transcribed_text}"</i>'

    # Send the personalized message to the Telegram chat with HTML formatting
    update.message.reply_html(personalized_message)

    # Delete the temporary audio file
    os.remove(file_path)

def main():
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.voice, voice_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
