from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

BOT_TOKEN = "7729481183:AAH6kE5H8l8GPXtm_9bNZLUwmxhcgrmMIvg"
CHAT_ID = "-1002895078616"

@app.route('/send', methods=['POST'])
def send_to_telegram():
    data = request.get_json()
    image_base64 = data['image'].split(',')[1]
    summary = data['summary']

    image_bytes = base64.b64decode(image_base64)

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {'photo': ('detection.jpg', image_bytes)}
    payload = {'chat_id': CHAT_ID, 'caption': summary}

    r = requests.post(telegram_url, data=payload, files=files)

    if r.status_code == 200:
        return jsonify({"status": "sent"})
    else:
        return jsonify({"status": "failed", "error": r.text}), 500

if __name__ == '__main__':
    app.run()
