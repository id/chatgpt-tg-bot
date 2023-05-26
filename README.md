# ChatGPT Telegram Bot

Simple Telegram bot that uses gpt-3.5-turbo model to generate text based on the chat history.

- uses pyTelegramBotAPI
- limit usage based on user id
- designed to be run on AWS Lambda (see `./deploy.sh`, update profile and region if necessary)

```bash
./package.sh
./deploy.sh
```
