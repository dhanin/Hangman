def check_email(string):
    if " " in string:
        return False
    if "@." in string:
        return False
    if "@" in string:
        if str(string).count("@") > 1:
            return False
        index = str(string).find('@')
        if str(string).find('.', index + 2) != -1:
            return True
        else:
            return False
        if str(string).find('.', index - 2) != -1:
            return True
        else:
            return False
    return False