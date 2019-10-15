import time


friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

def search_linear(xs, target):
    #Find and return the index of target in xs
    for ind, value in enumerate(xs):
        if value == target:
            return ind
    return -1

# print(search_linear(friends, 'Joe'))
# print(search_linear(friends, 'Linh'))

'''
- I removed a lot of words in vocab.txt
 to push file to github
 - You can download full file in here:
 http://openbookproject.net/thinkcs/python/english3e/_downloads/vocab.txt
'''
def load_words_from_file(filename):
    #read words from file name , return list of words
    f = open(filename, 'r')
    file_content =  f.read()
    f.close()
    wds = file_content.split()
    return wds

t0 = time.clock()
bigger_vocab = load_words_from_file('vocab.txt')
t1 = time.clock()
print("There are {0} words in the vocab, starting with\n {1} "
              .format(len(bigger_vocab), bigger_vocab[:6]))

print('Function took {} seconds'.format(t1 - t0))
