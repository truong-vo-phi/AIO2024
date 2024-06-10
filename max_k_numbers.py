def max(data):
    max_value = data[0]
    for e in data[1:]:
        if e > max_value:
            max_value = e
    return max_value

def max_k_numbers(data,k):
    start_i = 0
    end_i = k
    result = []
    while end_i <= len(data):
        k_data = data[start_i:end_i]
        result.append(max(k_data))
        start_i += 1
        end_i += 1
    return result

if __name__ == '__main__':
    data = [3,4,5,1,-44,5,10,12,33,1]
    while True:
        try:
            k = int(input('Input k: '))
            break
        except:
            print('Re-enter!')
    
    result = max_k_numbers(data,k)
    print(result)