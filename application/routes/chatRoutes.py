from flask import request, abort
from flask import Blueprint
from application.controllers.chatController import chat

chat_blueprint = Blueprint("chat_blueprint", __name__)
@chat_blueprint.route("/api/v1/chat", methods=["POST"])
def chat_function():
    if not request.is_json:
        abort(415, description="Unsupported Media Type. Please use application/json")
    
    data = request.get_json()
    user_input = data.get("message", "")
    return chat(user_input)
