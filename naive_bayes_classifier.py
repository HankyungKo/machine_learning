import re
import math

def main():
    # 1
    training_sentence = input()
    training_model = create_BOW(training_sentence)

    # 2
    testing_sentence = input()
    testing_model = create_BOW(testing_sentence)

    # 3
    alpha = float(input())

    print(calculate_doc_prob(training_model, testing_model, alpha))

def calculate_doc_prob(training_model, testing_model, alpha):
    # Implement likelihood function here...
    size_training = sum(training_model[1])
    len_dic = len(training_model[1])
    train_dic = training_model[0]
    train_list = training_model[1]
    testing_dic = testing_model[0]
    testing_list = testing_model[1]
    
    flip_train_dic = {y:x for x,y in train_dic.items()}
    flip_testing_dic = {y:x for x, y in testing_dic.items()}
    logprob = 0
    for i in range(len(testing_list)):
        for j in range(int(testing_list[i])):
            try:
                logprob += math.log((int(train_list[int(train_dic[flip_testing_dic[i]])]) + alpha) / (size_training + len_dic*alpha))
            except:
                logprob += math.log(alpha / (size_training + len_dic*alpha))
    return logprob



def create_BOW(sentence):
    bow_dict = {}
    bow = []

    sentence = sentence.lower()
    sentence = replace_non_alphabetic_chars_to_space(sentence)
    words = sentence.split(' ')
    for token in words:
        if len(token) < 1: continue
        if token not in bow_dict:
            new_idx = len(bow)
            bow.append(0)
            bow_dict[token] = new_idx
        bow[bow_dict[token]] += 1

    return bow_dict, bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()