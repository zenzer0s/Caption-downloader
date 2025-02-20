#!/bin/bash

echo "🚀 Starting setup..."

# Update package lists (for Termux users)
if [ -n "$TERMUX_VERSION" ]; then
    echo "📦 Updating Termux packages..."
    pkg update -y && pkg upgrade -y
    pkg install python -y
else
    echo "📦 Updating system packages..."
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-venv -y
fi

# Create and activate a virtual environment (recommended for Python projects)
echo "🐍 Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate  # Use venv/Scripts/activate for Windows

# Install required dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check if .env file exists, if not, create one and ask for token
if [ ! -f ".env" ]; then
    echo "🔑 .env file not found. Enter your Telegram Bot Token:"
    read BOT_TOKEN
    echo "BOT_TOKEN=$BOT_TOKEN" > .env
    echo "✅ .env file created with your bot token!"
else
    echo "✅ .env file already exists! Skipping token setup."
fi

# Start the bot
echo "🤖 Starting the bot..."
python bot.py
