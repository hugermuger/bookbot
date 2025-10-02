def sort_on(items):
    return items["num"]

def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    charakter_dic = {}
    for c in book_text:
        c = c.lower()
        if c in charakter_dic:
            charakter_dic[c] += 1
        else:
            charakter_dic[c] = 1
    return charakter_dic

def sorted_list(input_dict):
    new_list = []
    for i in input_dict:
        new_list.append({"name": i, "num": input_dict[i]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list