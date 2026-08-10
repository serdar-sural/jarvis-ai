import core.ai as ai

def start_chat(name, conversation_service, message_service):
    print("Willkommen zum Jarvis AI Chat!")
    conversation = conversation_service.create_conversation("Jarvis AI Chat")
    chat_running = True
    while chat_running:
        chat_message = get_chat_message(name)
        chat_running = check_exit_command(chat_message)
        if not chat_running:
            break
        message_service.create_message(conversation.id, "user", chat_message)
        response_text = ai.generate_response(chat_message)
        message_service.create_message(conversation.id, "assistant", response_text)
        show_chat_response(response_text)

def get_chat_message(name):
    message = input(name + ": ")
    return message

def check_exit_command(chat_message):
    if chat_message.lower() == "exit":
        print("Beende Chat...")
        return False
    return True

def show_chat_response(response_text):
    print("Jarvis AI: " + response_text)
