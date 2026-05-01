import json
import time

FILE = "chat_data.json"

def get_time():
    t = time.localtime()
    return f"{t.tm_hour}hr :{t.tm_min}min"

def read_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"messages": []}

def write_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

#  Add message
def add_message(username, message):
    data = read_data()

    new_msg = {
        "user": username,
        "message": message,
        "time": get_time()
    }

    data["messages"].append(new_msg)
    write_data(data)

    return new_msg

#  Get all messages
def get_all_messages():
    data = read_data()
    return data.get("messages", [])

# Search by user
def search_user(username):
    messages = get_all_messages()
    result = []

    for msg in messages:
        if msg.get("user") == username:
            result.append(msg)

    return result

# Search by keyword
def search_keyword(keyword):
    messages = get_all_messages()
    result = []

    for msg in messages:
        if keyword in msg.get("message", ""):
            result.append(msg)

    return result