import core.ai as ai

def start_chat(name, conversation_service, message_service):
    print("Willkommen zum Jarvis AI Chat!")
    conversation = select_conversation(conversation_service)
    if conversation is None:
        print("Keine gültige Konversation ausgewählt.")
        return
    messages = message_service.get_messages_by_conversation(conversation.id)
    ai.load_messages(messages)
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

def show_conversations(conversation_service):
    """
    Displays all available conversations.
    """
    conversations = conversation_service.get_all_conversations()

    if not conversations:
        print("No conversations found.")
        return

    print()
    print("Available conversations:")

    for conversation in conversations:
        print(
            f"{conversation.id}: "
            f"{conversation.title}"
        )

def select_conversation(conversation_service):
    """
    Allows the user to select an existing conversation.
    """
    conversations = conversation_service.get_all_conversations()

    if not conversations:
        print("No conversations found.")
        return None

    show_conversations(conversation_service)

    while True:
        choice = input("Select a conversation ID: ")

        if not choice.isdigit():
            print("Please enter a valid conversation ID.")
            continue

        conversation_id = int(choice)

        for conversation in conversations:
            if conversation.id == conversation_id:
                return conversation

        print("Invalid conversation ID. Please try again.")