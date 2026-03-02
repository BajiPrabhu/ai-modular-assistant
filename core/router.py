from datetime import datetime

def greet():
    return "Hello Shubham, how can I assist you?"

def get_name():
    return "I am your modular AI assistant."

def get_time():
    now = datetime.now().strftime("%H:%M")
    return f"The current time is {now}"

def stop_assistant():
    return "Stopping assistant."

# Command mapping dictionary
COMMANDS = {
    "hello": greet,
    "your name": get_name,
    "time": get_time,
    "stop": stop_assistant
}

def handle_command(command_text):
    command_text = command_text.lower()

    for keyword, function in COMMANDS.items():
        if keyword in command_text:
            return function()

    return "I did not understand that command."