def concatener(*str):
    result = ""
    for i in str:
        # Concatène des chaînes de caractères
        result += i+" "
    return result

def to_upper(*s):
    result = ""
    for i in s:
        # Met des chaînes de caractères en majuscules
        result += i.upper()+"\n"
    return result

