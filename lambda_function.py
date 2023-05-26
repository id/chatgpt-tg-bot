import json
import openai
import os
import telebot

tg_user_ids = [int(id.strip()) for id in os.environ.get('TELEGRAM_USER_IDS', '').split(',')]
openai.api_key = os.environ.get('OPENAI_API_KEY')
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))

def chat_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    message = response['choices'][0]['message']['content']
    return message.strip()

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


def lambda_handler(event, context):
    try:
        message = json.loads(event['body'])['message']
        chat_id = message['chat']['id']
        user_id = int(message['from']['id'])
        prompt = message['text']
    except Exception as e:
        print(str(e))
        return

    if user_id not in tg_user_ids:
        print(f"Received message from unathorized user {user_id}: {prompt}")
        bot.send_message(chat_id, response)
        return

    print(f"Received message from {user_id}: {prompt}")
    response = ''
    try:
        if prompt.startswith('/image'):
            response = generate_image(prompt)
        else:
            response = chat_completion(prompt)
    except openai.error.OpenAIError as e:
        response = str(e)

    print(f"Response from openai: {response}")
    bot.send_message(chat_id, response)
