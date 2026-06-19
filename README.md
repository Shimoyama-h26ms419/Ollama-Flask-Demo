# Ollama-Flask-Demo
[![GitHub repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github)](https://github.com/Shimoyama-h26ms419/Ollama-Flask-Demo) [![Ollama v0.30.10](https://img.shields.io/badge/Ollama-v0.30.10-white?logo=ollama)](https://ollama.com/) [![Flask v3.1.3](https://img.shields.io/badge/Flask-v3.1.3-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)

![Ollama-Flask-Demo](./demo.gif)

## 0. TL;DR
- [**Ollama**](https://ollama.com/) の出力をいい感じに表示するWebアプリを作りました

## 1. Overview（概要）
- 従来のChatGPTのように、Markdown形式で出力されるLLMの回答をWebアプリで表示できるようにしました
- Ollama で pull したモデルをドロップダウンから選択できます。
- お使いのPCのスペックに合わせてモデルを pull してください。

## 2. Setup（環境構築）

### 2.1 Ollama のインストール
- [**Ollama**](https://ollama.com/) 公式サイトを参考にインストールします。

### 2.2 リポジトリのクローン
- このリポジトリをクローンします。

```
git clone https://github.com/Shimoyama-h26ms419/Ollama-Flask-Demo.git
```

### 2.3 venv の作成
- プロジェクトに移動します。
```
cd ./Ollama-Demo-Flask
```

- 以下のコマンドによりプロジェクトに venv を作成します。
```
python -m venv ./.venv
```

### 2.4 必要ライブラリのインストール
- `flask` と `requests` をインストールします。
```
pip install flask requests
```

### 2.5 Ollama の起動
- 以下のコマンドで Ollama を起動します。
  - 既に起動済みなら問題ありません。
```
ollama serve
```

### 2.5 モデルの pull
- デフォルトで必要な `gemma4:e2b` モデルを pull します。
```
ollama pull gemma4:e2b
```

- モデルの一覧を表示することもできます。
```
ollama list
```

### 2.6 Flask の起動
- Flask を起動し、 `localhost:5000` でブラウザからアクセスすることが可能です。
```
python ./app.py
```
