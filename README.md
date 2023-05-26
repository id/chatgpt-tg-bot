# ChatGPT Telegram Bot

Simple Telegram bot that uses gpt-3.5-turbo model to generate text based on the chat history.

- uses pyTelegramBotAPI
- limit usage based on user id
- designed to be run on AWS Lambda (see `./deploy.sh`, update profile and region if necessary)

## Prerequisites

- create a [Telegram bot and obtain a token](https://core.telegram.org/bots/features#botfather)
- create an [OpenAI account and obtain an API key](https://platform.openai.com/account/api-keys)
- create an AWS API Gateway endpoint and [register it as a webhook for the Telegram bot](https://core.telegram.org/bots/api#setwebhook)

## Configuration

The code uses environment variables for configuration:

- `OPENAI_API_KEY` - [OpenAI API key](https://platform.openai.com/account/api-keys)
- `TELEGRAM_BOT_TOKEN` - [Telegram bot token](https://core.telegram.org/bots/features#botfather)
- `TELEGRAM_USER_IDS` - comma separated list of user ids that are allowed to use the bot

To get Telegram user id, run the bot, send it a message, and obtain the id from the log.

```bash
./package.sh # fetch dependencies and create a zip file
./deploy.sh  # deploy zip package to AWS Lambda
```
