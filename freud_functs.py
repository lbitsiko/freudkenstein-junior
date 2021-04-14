import numpy as np
import random
import time
import pickle

def words(stringIterable):
    #upcast the argument to an iterator, if it's an iterator already, it stays the same
    lineStream = iter(stringIterable)
    for line in lineStream: #enumerate the lines
        for word in line.split(): #further break them down
            yield word

def create_dictionary_from_txt(filename):
    start = time.time()
    mydictionary = set()
    with open(filename, 'r', encoding='utf8') as myself:
        # for word in words(myself):
        #     print(word)
        lines = myself.readlines()
        # sys.exit()
        for line in lines:
            # print(set(line.split()))
            # sys.exit()
            mydictionary = mydictionary.union(set(line.split()))
    stop = time.time()
    print(stop - start)
    return mydictionary

def save_dict_to_pickle(filename, mydictionary):
    filehandler = open(filename, 'wb')
    pickle.dump(mydictionary, filehandler)
    filehandler.close()

def load_dict_from_pickle(filename):
    filehandler = open(filename, 'rb')
    return pickle.load(filehandler)

def basic_dict_categorization(mydictionary):
    verbs = set()
    nouns = set()
    for word in mydictionary:
        if word[-2:] == 'ed':
            verbs = verbs.union({word})
        if word[-3:] == 'ing':
            verbs = verbs.union(({word}))
        if word[-1:] == 't':
            nouns = nouns.union({word})
        if word[-2:] == 'ns':
            nouns = nouns.union({word})
    return  verbs, nouns

def basic_random_walk_on_dict(filename, seed, mydictionary):
    f = open(filename, "a")
    verbs, nouns = basic_dict_categorization(mydictionary)
    dict_list = list(mydictionary)
    dict_list = random.sample(dict_list, len(dict_list))
    do = True
    start_word = dict_list[seed]
    f.write(start_word+'\n')
    count = 0
    while do:
        notFound = True
        while notFound:
            prob = np.random.uniform(0, 1)
            if prob < 0.5 :
                seed += 1
            else:
                seed -= 1
            next_word = dict_list[seed]
            if start_word in nouns:
                if next_word not in nouns:
                    notFound = False
                else:
                    continue
            else:
                if next_word not in verbs:
                    notFound = False
                else:
                    continue
        f.write(next_word + '\n')
        start_word = next_word
        count += 1
        if count > 1000: do = False
    f.close()

def pick_random_words(filename, mydictionary):
    random_ints = [ random.randint(1,len(mydictionary)) for i in range(100)]
    f = open(filename, "a")
    f.write('\n')
    dict_list = list(mydictionary)
    for ran_int in random_ints:
        print(dict_list[ran_int])
        f.write(dict_list[ran_int]+'\n')
    f.close()
