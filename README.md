# FastAPI 人気投票アプリ

このプロジェクトは人気投票を行うためのシンプルな Web アプリケーションです。バックエンドには FastAPI を、データ保存には PostgreSQL を使用しています。

## PostgreSQL のセットアップ

アプリケーションはローカルに PostgreSQL サーバーがあることを前提としています。以下に基本的なセットアップ手順を示します。

1. **PostgreSQL のインストール**

   Ubuntu/Debian 系の場合:
   ```bash
   sudo apt-get update
   sudo apt-get install postgresql
   ```

   macOS で Homebrew を使う場合:
   ```bash
   brew install postgresql
   ```

2. **データベースとユーザーの作成**

   PostgreSQL サービスを開始したら次のコマンドを実行します。
   ```bash
   sudo -u postgres psql -c "CREATE DATABASE polls;"
   sudo -u postgres psql -c "CREATE USER postgres WITH ENCRYPTED PASSWORD 'password';"
   sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE polls TO postgres;"
   ```
   ユーザー名やパスワードは必要に応じて変更してください。

3. **接続 URL の確認**

   `database.py` の `DATABASE_URL` が設定に合っていることを確認します。デフォルトでは次のようになっています。
   ```
   postgresql://postgres:password@localhost/polls
   ```

PostgreSQL が起動して設定できたら、以下の手順でアプリを初期化して実行します。

## セットアップ

1. 依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```
2. PostgreSQL が動作しており、`database.py` の `DATABASE_URL` が自分の設定に合っているかを確認します。
3. サンプルの候補者でデータベースを初期化します。
   ```bash
   python init_db.py
   ```
4. アプリケーションを起動します。
   ```bash
   uvicorn main:app --reload
   ```
5. ブラウザで `http://localhost:8000` を開き、投票や結果表示を行います。

## Docker

付属の `docker-compose.yml` ファイルを使って、アプリケーションと PostgreSQL を Docker 上で動かすこともできます。

1. サービスをビルドして起動します。
   ```bash
   docker compose up --build
   ```
2. `http://localhost:8000` にアクセスするとアプリを利用できます。データベースは `postgres_data` ボリュームに保存され、コンテナを再起動しても残ります。
3. 終了する際は `Ctrl+C` で停止し、以下のコマンドでコンテナを削除します。
   ```bash
   docker compose down
   ```
