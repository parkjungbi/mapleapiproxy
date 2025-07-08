from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "메이플 캐릭터 중계 API입니다."

@app.route('/api/character/<nickname>')
def get_character(nickname):
    url = f"https://maplemworlds.kr/api/character/basic/{nickname}"
    res = requests.get(url).json()

    return jsonify({
        "nickname": res.get("character_name"),
        "level": res.get("character_level"),
        "job": res.get("character_class"),
        "guild": res.get("guild_name"),
        "image": res.get("character_image"),
        "power_score": res.get("stat_main", 0) + res.get("stat_sub", 0)
    })
