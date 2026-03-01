# FLY — Python Prototype

This folder contains a fully working local version of FLY.

It runs in two modes:

- Demo Mode (no API key required)
- AI Mode (uses OpenAI if a key is provided)

You do not need prior AI experience to run this.

------------------------------------------------------------

# Step-by-Step: From Zero to Running

## 1) Clone the Repository

From your terminal:

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

Then:

cd YOUR_REPO/python

------------------------------------------------------------

## 2) Install Dependencies

python3 -m pip install -r requirements.txt

------------------------------------------------------------

## 3) Start the Server

python3 main.py

You should see:

Uvicorn running on http://0.0.0.0:8000

Leave this terminal window open.

------------------------------------------------------------

## 4) Test in Your Browser

Open Chrome (or any browser) and paste:

http://localhost:8000/test?message=you%20never%20listen%20to%20me

You should see JSON like:

{"status":"respond","response":"[FLY] ..."}

Try a neutral message:

http://localhost:8000/test?message=ok%20sounds%20good

You should see:

{"status":"silent"}

That means it works.

------------------------------------------------------------

# Demo Mode (Default)

If you do nothing else, FLY runs in demo mode.

Demo mode:
- Uses simple rule-based detection
- Requires no API key
- Works immediately after install

------------------------------------------------------------

# Enable AI Mode (Optional)

If you want real AI reframing:

1) Inside the python folder, copy the template:

cp .env.example .env

2) Open the .env file and set:

OPENAI_API_KEY=your_key_here

3) Restart the server:

python3 main.py

Now FLY will automatically use OpenAI.

If no key is present, it safely falls back to demo mode.

------------------------------------------------------------

# API Endpoint

POST endpoint:

http://localhost:8000/message

Example request body:

{"message":"you never listen to me"}

Response:

{"status":"silent"}
or
{"status":"respond","response":"[FLY] ..."}

------------------------------------------------------------

# What This Prototype Demonstrates

- Embedded conversational AI logic
- Escalation detection
- Safe fallback architecture
- Public-safe API key handling
- Clean separation of demo vs AI mode

------------------------------------------------------------

# Next Expansions

- Twilio SMS integration
- Slack adapter
- WhatsApp adapter
- Configurable sensitivity
- Logging and governance layer

------------------------------------------------------------

Built as an experiment in distributed conversational intelligence.
