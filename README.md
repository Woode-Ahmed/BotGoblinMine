# BotGoblinMine
GoblinMine

START:-

pkg update && pkg upgrade -y && pkg install python git nano -y

git clone https://github.com/Woode-Ahmed/BotGoblinMine

cd BotGoblinMine

cp .env-example .env

nano .env

pip install -r requirements.txt

python main.py
