import re

def main():
    sentence = input()
    BOW_dict, BOW = create_BOW(sentence)

    print(BOW_dict)
    print(BOW)

def create_BOW(sentence):
    # Exercise
    temp = replace_non_alphabetic_chars_to_space(sentence.lower())
    words = temp.strip().split(" ")
    
    for i in range(len(words)):
        if len(words[i])<1:
            words.remove(words[i])
    
    count = 0
    bow_dict = {}
    dic_words = []
    for i in range(len(words)):
        if words[i] not in bow_dict.keys():
            bow_dict[words[i]] = count
            dic_words.append(words[i])
            count += 1
    bow = [words.count(i) for i in dic_words]
    
    return bow_dict, bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()