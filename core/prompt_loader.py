
SYSTEM_PROMPT_PATH = "prompts/system_prompt.md"

def get_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as file:
        system_prompt_content = file.read()
    return system_prompt_content