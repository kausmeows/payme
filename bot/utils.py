import json

def load_recipients(file_path):
    """
    Load recipients' chat IDs from a JSON file.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return list(data.get("recipients", {}).values())
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading recipients: {e}")
        return []
