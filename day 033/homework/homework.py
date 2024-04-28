def generate_hashtag(s):
    result = ["#"]
    splited = s.split(" ")
    for word in splited:
        word = word.capitalize()
        result.append(word)
    
    if len("".join(result)) > 140:
        return False
    elif s == "" or "".join(result) == "":
        return False
    else:
        return "".join(result)