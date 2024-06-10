f = open('AIO2024/P1_data.txt','r')
def word_count(file):
    word_dict = {}
    for line in file:
        words = line.split()
        for word in words:
            word = word.rstrip('\n')
            word_dict[word] = word_dict.get(word,0) + 1
    print(word_dict)    
        
word_count(f)
