def count_characters(st):
    count_dict = {}
    for c in st:
        count_dict[c] = count_dict.get(c,0) + 1
    print(count_dict)
    
if __name__ == '__main__':
    string = "Happiness"
    
    count_characters(string)