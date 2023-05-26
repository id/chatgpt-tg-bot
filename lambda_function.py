import json
import openai
import os
import telebot

tg_user_ids = [int(id.strip()) for id in os.environ.get('TELEGRAM_USER_IDS', '').split(',')]
openai.api_key = os.environ.get('OPENAI_API_KEY')
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    message = response.choices[0].message.content.strip()
    return message


def lambda_handler(event, context):
    try:
        message = json.loads(event['body'])['message']
        chat_id = message['chat']['id']
        user_id = int(message['from']['id'])
        text = message['text']
        if user_id not in tg_user_ids:
            print(f"Received message from unathorized user {user_id}: {text}")
            return {
                'statusCode': 200,
                'body': json.dumps('Not allowed')
            }
        print(f"Received message from {user_id}: {text}")
        response = generate_response(text)
        print(f"Response from openai: {response}")
        bot.send_message(chat_id, response)

    except Exception as e:
        print(str(e))
        pass
