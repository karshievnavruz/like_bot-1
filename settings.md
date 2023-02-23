# Setup environment

## Create virtual environment

```bash
python3 -m venv venv
```

## Activate virtual environment

```bash
source venv/bin/activate
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Git ignore

```bash
echo "venv" >> .gitignore
```

## Set environment variables

The following environment variables are required to run the bot:
-Telegram bot token

```bash
export TOKEN="your token"
```
