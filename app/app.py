from flask import Flask, request
import requests
from datetime import datetime

BRAIN_URL = "http://brain.vape-jet.com"
BRAIN_WEBHOOK_URL = f"{BRAIN_URL}/webhook/atlassian"

app = Flask(__name__)


@app.route("/")
def index():
    return "OK"


@app.route("/api/webhook/atlassian", methods=["POST"])
def atlassian_webhook():
    try:
        prefix = f"[{datetime.now().isoformat()}] - JIRA"
        print(f"{prefix} - {request.json}")

        response = requests.post(BRAIN_WEBHOOK_URL, json=request.json)
        response.raise_for_status()

        return "OK", 200
    except Exception as e:
        app.logger.error(e)
        return "ERROR", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
