from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api"
DEFAULT_MODEL = "gemma4:e2b"


def get_available_models():
    """Ollama にインストール済みのモデル一覧を取得する"""
    try:
        res = requests.get(f"{OLLAMA_API_URL}/tags", timeout=5)
        res.raise_for_status()
        data = res.json()
        models = [m["name"] for m in data.get("models", [])]
        if DEFAULT_MODEL not in models:
            models.insert(0, DEFAULT_MODEL)
        return models
    except requests.RequestException:
        # Ollama に接続できない場合はデフォルトのみ返す
        return [DEFAULT_MODEL]


@app.route("/")
def index():
    models = get_available_models()
    return render_template(
        "index.html",
        models=models,
        default_model=DEFAULT_MODEL,
    )


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    prompt = (payload.get("prompt") or "").strip()
    model = payload.get("model") or DEFAULT_MODEL

    if not prompt:
        return jsonify({"error": "プロンプトが空です"}), 400

    try:
        res = requests.post(
            f"{OLLAMA_API_URL}/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )
        res.raise_for_status()
        data = res.json()
        return jsonify({"response": data.get("response", "")})
    except requests.RequestException as e:
        return jsonify({"error": f"Ollama との通信に失敗しました: {e}"}), 502


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
