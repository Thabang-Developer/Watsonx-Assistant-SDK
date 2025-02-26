from flask import jsonify
from application.models import watsonx_assistant

session_id = watsonx_assistant.create_session()

def chat(user_input):
    
    if session_id is None:
        print("No session id.")
        
        return None
    
    response = watsonx_assistant.send_message(user_input, session_id)
        
    return jsonify({
        "response": response
    })
