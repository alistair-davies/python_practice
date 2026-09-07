def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    lines = ["Current User Settings:"]
    for k, v in settings.items():
        lines.append(f"{k.capitalize()}: {v}")
    return "\n".join(lines) + '\n'


settings = {}


# Example dictionary for tests
##test_settings = {
##    "theme": "dark",
##    "notifications": "enabled",
##    "volume": "high"
##}


##settings = {
##    "theme": "dark",
##    "notifications": "enabled",
##    "volume": "high"
##}

##print("name:", __name__)
##if __name__ == "__main__":
##    print("RUNNING TESTS")
##    #settings = {}
##    #print(add_setting(settings, ("Theme","Light")))
##    #print(add_setting(settings, ("theme","dark")))
##    print(update_setting(settings, ("theme","dark")))
##    print(delete_setting(settings, "theme"))
##    print(view_settings(settings))

