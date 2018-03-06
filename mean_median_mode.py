import numpy as np

def descriptive_mean(length, input_list):
    length = int(length)
    input_list = [int(num) for num in input_list.split(' ')]
    
    if len(input_list) < 1:
        return 0
    
    def calculate_mode(num_list):
        hashTable = {}
        
        for num in num_list:
            if num in hashTable:
                counter = hashTable[num]
                counter += 1
                hashTable[num] = counter
            else:
                hashTable[num] = 1

        maxCount = 0

        for key in hashTable:
            if hashTable.get(key) > maxCount:
                maxCount = hashTable[key]
                modeNum = key
            elif hashTable.get(key) == maxCount and key < modeNum:
                modeNum = key

        if maxCount == 1:
            modeNum = min(num_list)
        
        return modeNum

    listMean = round(np.mean(input_list), 1)
    listMedian = round(np.median(input_list), 1)
    listMode = calculate_mode(input_list)
    
    print(listMean)
    print(listMedian)
    print(listMode)

num_length = input()
num_list = input()
descriptive_mean(num_length, num_list)