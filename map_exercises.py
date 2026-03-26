def convert_to_uppercase(strings):
    
    uppercase_strings = map(lambda x: x.upper(), strings)
    
    return list(uppercase_strings)

def calculate_lengths(words):
    
    word_lengths = list(map(lambda x: len(x), words))
    
    return list(word_lengths)