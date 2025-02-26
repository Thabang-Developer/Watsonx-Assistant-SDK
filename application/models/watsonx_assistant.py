from dotenv import load_dotenv
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

# Load environment variables
load_dotenv()

CLOUD_API_KEY = os.getenv("cloud_apikey")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
ASSISTANT_URL = os.getenv("ASSISTANT_URL")
DRAFT_ENV_ID = os.getenv("DRAFT_ENV_ID")

if not CLOUD_API_KEY or not ASSISTANT_ID or not ASSISTANT_URL:
    raise ValueError("Missing required environment variables. Check .env file.")

# Watsonx Assistant authentication
authenticator = IAMAuthenticator(CLOUD_API_KEY)
assistant = AssistantV2(
    version="2024-08-25",
    authenticator=authenticator
)
assistant.set_service_url(ASSISTANT_URL)

def create_session():
    try:
        session_response = assistant.create_session(
            assistant_id=DRAFT_ENV_ID
        ).get_result()
        session_id = session_response.get("session_id")
        print("Created session:", session_id)
        return session_id
    except Exception as e:
        print("Error creating session:\n", e)

def send_message(user_input, session_id):
    try:
        response = assistant.message(
            assistant_id = DRAFT_ENV_ID,
            session_id = session_id,
            input={
                "message_type": "text", 
                "text": user_input
            }
        ).get_result()
        
        output = response.get("output", {})
        generic = output.get("generic", [])
        extracted_text = None
        for item in generic:
            if item.get("response_type") == "text":
                extracted_text = item.get("text")
                break
        
        if extracted_text:
            print("Watsonx Assistant:", extracted_text)
        else:
            print("No text response found.")
        
        return extracted_text
    
    except Exception as e:
        print("Error sending message:\n", e)
