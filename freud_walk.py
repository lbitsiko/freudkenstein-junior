import os
import sys
import numpy as np
import freud_functs as ff
# from freud_functs import load_dict_from_pickle, basic_dict_categorization, pick_random_words, create_dictionary_from_txt

# mydictionary = ff.create_dictionary_from_txt('./input/freud.txt')
# ff.save_dict_to_pickle('./dict_feud.pickle', mydictionary)

mydictionary = ff.load_dict_from_pickle('./dict_feud.pickle')

verbs, nouns = ff.basic_dict_categorization(mydictionary)

folder_contents = os.listdir('./output/random_walk')
if folder_contents == []:
    fname = './output/random_walk/output.txt'
else:
    fname = './output/random_walk/output{}.txt'.format(
        int(folder_contents[len(folder_contents) - 1].split('.')[0].split('output')[1])+1)
seed = np.random.randint(0,len(mydictionary))
ff.pick_random_words(fname, mydictionary)