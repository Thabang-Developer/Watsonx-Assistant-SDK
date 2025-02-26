from flask import Flask
from flask_cors import CORS
from application.routes.chatRoutes import chat_blueprint  # ✅
import os


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    # app.config['DB_URL'] = os.getenv('DB_URL')
    # app.config['DB_NAME'] = 'Future-DB'

    # try:
    #     app.mongo_client = MongoClient(app.config['DB_URL'])
    #     app.db = app.mongo_client[app.config['DB_NAME']]
    #     print("Connected to MongoDB successfully.")

    # except Exception as e:
    #     print(f"Error connecting to MongoDB: {e}")


    app.register_blueprint(chat_blueprint)


    return app
