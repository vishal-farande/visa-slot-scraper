# Visa Slot Availability Notifier

This project is a Visa Slot Availability Notifier that scrapes visa appointment availability from visaslots.info and sends a Telegram notification whenever slots are available at Mumbai VAC.

## Features

1. Automated Slot Checking: Runs every 5 minutes using GitHub Actions.
2. Telegram Notifications: Sends a message when slots are available.
3. Free & Serverless: Runs on GitHub Actions (No need to keep your system on!).
4. Customizable: Modify locations, frequency, or add email alerts.


## Prerequisites

1. Python 3.9+ installed on your system (for local testing).
2. GitHub Account to set up GitHub Actions.
3. Telegram Bot & Chat ID for notifications.

## Setting up Telegram Bot
1. Go to BotFather on Telegram.
2. Type /newbot and follow the instructions.
3. Save your Bot Token.
4. Get your Chat ID by messaging @userinfobot on Telegram.



## GitHub Actions Automation

### Step 1: Push Code to GitHub
git add .
git commit -m "Initial commit"
git push origin main

### Step 2: Set Up GitHub Actions

1. Navigate to GitHub → Your Repo → Actions.
2. You should see a workflow named Visa Slot Scraper.
3. It will run every 5 minutes automatically.
4. Manually Trigger the Workflow
5. Go to Actions in your GitHub repo.
6. Select Visa Slot Scraper.
7. Click Run Workflow.