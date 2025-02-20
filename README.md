---

### **📌 Instagram Caption Downloader Telegram Bot**  

A Telegram bot that **fetches captions from Instagram Reels**. Run it on **PC**, **Android (Termux)**, or **cloud servers** with **automatic setup!**  

## **✨ Features**  
✅ Fetch captions from **Instagram Reels** 📜  
✅ Works on **PC, Linux, Termux (Android), and cloud platforms** ☁️  
✅ **Easy setup** with a single command ⚡  
✅ Uses **environment variables** for security 🔑  
✅ **Automatic token input** and bot startup 🚀  
✅ **24/7 operation** when deployed on cloud platforms 🌐  

---

## **🚀 How to Set Up Your Own Bot**  

### **1️⃣ Create Your Own Bot and Get Your Telegram Bot Token**  
1. Open [BotFather](https://t.me/BotFather) on Telegram.  
2. Use `/newbot` and follow the steps.  
3. Copy the **bot token** (e.g., `123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).  

---

### **2️⃣ Install & Run on Your Device**  

#### **💻 PC (Windows/Linux/macOS)**
1. **Clone the repo:**  
   ```bash
   git clone https://github.com/zenzer0s/Caption-downloader.git
   cd Caption-downloader
   ```
2. **Run the setup script:**  
   ```bash
   bash setup.sh
   ```
   - The script will **automatically ask for your bot token** and store it securely in the `.env` file.  
   - After setup, the bot local server will **start automatically**.  

3. **To restart the bot later:**  
   ```bash
   python bot.py
   ```
4. **Open your bot on Telegram and send the link.**  

---

#### **📱 Android (Termux)**
1. **Install Termux from F-Droid (not Play Store)**  
2. **Run these commands in Termux:**  
   ```bash
   pkg update -y && pkg upgrade -y
   pkg install git -y
   git clone https://github.com/zenzer0s/Caption-downloader.git
   cd Caption-downloader
   bash setup.sh
   ```
   - The script will **automatically ask for your bot token** and store it securely in the `.env` file.  
   - After setup, the bot will **start automatically**.  

3. **To restart the bot later:**  
   ```bash
   python bot.py
   ```
4. **Open your bot on Telegram and send the link.**  

---

### **☁️ Deploy on Cloud Platforms (24/7 Operation)**  

#### **1️⃣ Google Cloud Platform (GCP)**  
1. **Create a VM Instance:**  
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).  
   - Create a new VM instance with **Ubuntu** or any Linux distribution.  
   - Allow HTTP/HTTPS traffic.  

2. **SSH into the VM:**  
   - Use the **SSH button** in the GCP console or a terminal with `gcloud` CLI.  

3. **Install dependencies and clone the repo:**  
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git python3 python3-pip -y
   git clone https://github.com/zenzer0s/Caption-downloader.git
   cd Caption-downloader
   bash setup.sh
   ```

4. **Run the bot in the background:**  
   Use `tmux` or `nohup` to keep the bot running after closing the SSH session:  
   ```bash
   tmux new -s bot
   python bot.py
   ```
   - Press `Ctrl+B`, then `D` to detach from the session.  
   - To reattach: `tmux attach -t bot`.  

---

#### **2️⃣ Heroku**  
1. **Install the Heroku CLI:**  
   Follow the [Heroku CLI installation guide](https://devcenter.heroku.com/articles/heroku-cli).  

2. **Login to Heroku:**  
   ```bash
   heroku login
   ```

3. **Create a new Heroku app:**  
   ```bash
   heroku create YOUR_APP_NAME
   ```

4. **Set your bot token as an environment variable:**  
   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
   ```

5. **Deploy the bot:**  
   ```bash
   git push heroku main
   ```

6. **Scale the bot:**  
   ```bash
   heroku ps:scale worker=1
   ```

---

#### **3️⃣ AWS (EC2)**  
1. **Launch an EC2 Instance:**  
   - Go to the [AWS EC2 Console](https://aws.amazon.com/ec2/).  
   - Launch an instance with **Ubuntu** or any Linux distribution.  
   - Allow HTTP/HTTPS traffic in the security group.  

2. **SSH into the instance:**  
   ```bash
   ssh -i YOUR_PEM_FILE.pem ubuntu@YOUR_EC2_PUBLIC_IP
   ```

3. **Install dependencies and clone the repo:**  
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git python3 python3-pip -y
   git clone https://github.com/zenzer0s/Caption-downloader.git
   cd Caption-downloader
   bash setup.sh
   ```

4. **Run the bot in the background:**  
   Use `tmux` or `nohup` to keep the bot running after closing the SSH session:  
   ```bash
   tmux new -s bot
   python bot.py
   ```
   - Press `Ctrl+B`, then `D` to detach from the session.  
   - To reattach: `tmux attach -t bot`.  

---

## **📄 Notes**  
- Your **bot token is stored securely** in `.env` (not pushed to GitHub).  
- Make sure your Instagram post **is public** or it won’t fetch captions.  
- The bot will **auto-start** after setup. If you need to restart it, use `python bot.py`.  
- For **24/7 operation**, deploy the bot on a cloud platform like **GCP**, **Heroku**, or **AWS**.  

---

## **📜 License**  
This project is **open-source** under the **MIT License**.  

---

### **🔧 What the `setup.sh` Script Does**  
The `setup.sh` script automates the entire setup process:  
1. **Installs dependencies** (e.g., Python, required libraries).  
2. **Prompts you to enter your bot token** and saves it securely in `.env`.  
3. **Starts the bot automatically** after setup.  

---

### Example `setup.sh` Script  
Here’s a sample `setup.sh` script to match the README instructions:  

```bash
#!/bin/bash

# Install Python and required libraries
echo "Installing dependencies..."
pip install -r requirements.txt

# Ask for bot token
read -p "Enter your Telegram bot token: " token

# Save token to .env
echo "TELEGRAM_BOT_TOKEN=$token" > .env

# Start the bot
echo "Starting the bot..."
python bot.py
```

---
