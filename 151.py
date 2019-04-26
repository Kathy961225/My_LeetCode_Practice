 if not s:
        return ""        
    res = []
    curr_word = ""
    count = 0
    
    for i in s:
        if i != " ":
            curr_word +=i
            count = 1             
        elif i == " ": 
            if count == 1:
                res.insert(0,curr_word)
                curr_word = ""
            count = 0               
    if i != " ":
        res.insert(0,curr_word)
    return " ".join(res)