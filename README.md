# Caption Downloader Bot

This is a Telegram bot that downloads captions from Instagram Reels and Stories and sends them to the user.

## Features
- Download captions from Instagram Reels ✅
- Download captions from Instagram Stories ✅
- Run locally on your computer ✅
- Run on Android using Termux ✅

## Installation & Setup

### Running Locally
1. Install Python (if not already installed).
2. Clone this repository:
   ```sh
   git clone https://github.com/zenzer0s/Caption-downloader.git
   ```
3. Navigate to the project directory:
   ```sh
   cd Caption-downloader
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Set up your Telegram bot token.
6. Run the bot:
   ```sh
   python bot.py
   ```

### Running on Android (Termux)
1. Install Termux from the Play Store.
2. Update and install Python:
   ```sh
   pkg update && pkg upgrade
   pkg install python git
   ```
3. Clone the repository:
   ```sh
   git clone https://github.com/zenzer0s/Caption-downloader.git
   ```
4. Navigate to the project directory:
   ```sh
   cd Caption-downloader
   ```
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Run the bot:
   ```sh
   python bot.py
   ```

## Usage
- Send an Instagram Reel or Story link to the bot.
- The bot will extract and send back the caption.

## Contributing
Feel free to submit issues or pull requests to improve this project!

## License
This project is open-source under the MIT License.

