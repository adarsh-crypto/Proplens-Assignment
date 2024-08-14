import gradio as gr
import requests

def chatbot_response(user_input, chat_history=None):
    api_url = "http://127.0.0.1:9001/api"  

    payload = {"content": user_input}
    
    try:
        api_response = requests.post(api_url, json=payload)
        api_response.raise_for_status()
        response_data = api_response.json().get("content", "No response content found")
        return response_data
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except Exception as e:
        return f"Error processing request: {str(e)}"

bot_avatar = ""
user_avatar = ""

# Gradio interface setup for the chatbot
gr.ChatInterface(
    fn=chatbot_response,
    chatbot=gr.Chatbot(height=300,
                       bubble_full_width=False,
                       render=False,
                       container=True,
                       elem_id="chatbot",
                       show_copy_button=True,
                       label="Proplens Co-Pilot",
                    #    avatar_images=(
                    #        user_avatar,
                    #        bot_avatar,
                    #    ),
    ),
    textbox=gr.Textbox(placeholder="Start the conversation with Proplens Co-Pilot", container=False, scale=7),
    theme='ParityError/Interstellar',
    css="""
        footer {visibility: hidden;}
        #chatbot { flex-grow: 1 !important; overflow: auto !important;}
    """,
    cache_examples=False,
    retry_btn=None,
    undo_btn=None,
    clear_btn=None,
).launch(server_name="0.0.0.0", server_port=9002, share=False)
