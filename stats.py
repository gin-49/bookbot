def count_words(content):
    count = len(content.split())
    return count


def count_characters(content):
    letters = {}
    for i in content:
        letter = i.lower()
        if letter in letters:
            letters[letter] += 1
        elif letter not in letters:
            letters[letter] = 1
    return letters


def sort_on(items):
    return items["num"]


def sorted_list(characters):
    l = []
    for i in characters:
        dic = {}
        dic["char"] = i
        dic["num"] = characters[i]
        l.append(dic)
    l.sort(reverse=True, key=sort_on)
    return l
