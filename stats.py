def count_words(text):
    words = text.split()
    return len(words)

def calculate_char_stats(text):
    ret = {}
    for ch in text:
        key = ch.lower()
        ret[key] = ret.get(key, 0) + 1
    return ret

def sorted_char_stats(stats):
    ret = list(stats.items())
    ret.sort(key=lambda it: it[1], reverse=True)
    return ret

    

    
