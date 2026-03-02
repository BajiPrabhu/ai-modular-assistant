def handle_command(command_text):
    command_text = command_text.lower()

    if "hello" in command_text:
        return "Hello Shubham, how can I assist you?"

    elif "your name" in command_text:
        return "I am your modular AI assistant."

    elif "time" in command_text:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return f"The current time is {now}"

    elif "stop" in command_text:
        return "Stopping assistant."

    else:
        return "I did not understand that command."