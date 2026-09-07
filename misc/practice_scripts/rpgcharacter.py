

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    #Check name is a string
    if not isinstance(name, str): 
        return 'The character name should be a string'
    #Check the characer name isn't blank
    if name == "":
        return 'The character should have a name'
    #Check character name length is longer than 10 
    if len(name) > 10:
        return 'The character name is too long'
    #Check to see if character name contains spaces
    if " " in name:
        return 'The character name should not contain spaces'
    

    stats = (strength, intelligence, charisma)

    
    for x in stats:
        if not isinstance(x, int):
           return "All stats should be integers"
        if x < 1:
            return 'All stats should be no less than 1'
        if x > 4:
            return 'All stats should be no more than 4'

    if sum(stats) != 7:
        return 'The character should start with 7 points'

    def status_bar(dot_scale):
        return dot_scale * full_dot + (10-dot_scale) * empty_dot



    lines = [
            name,
        f"STR {status_bar(strength)}",
        f"INT {status_bar(intelligence)}",
        f"CHA {status_bar(charisma)}",
    ]

    return "\n".join(lines)

print(create_character('ren', 4, 2, 1)) 




