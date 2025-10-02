def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    charakter_dic = {}
    for c in book_text:
        if c.lower() in charakter_dic:
            charakter_dic[c.lower()] += 1
        else:
            charakter_dic[c.lower()] = 1
    return charakter_dic