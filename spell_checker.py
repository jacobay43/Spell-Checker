 
import re
import json
import random

all_dict_words = []
result = False
words = []
    
def testDictionary(word):
    return (word in all_dict_words)
def randomizeWord(word):
    array = re.split(r'',word)
    del array[0]
    array.pop()
    random.shuffle(array)
    return ''.join(array)
def multipleEliminationAllAtOnce(word):
    buffer = ''
    array = re.split(r'',word)
    del array[0] #discard blank spaces in 1st and last pos of array
    array.pop()
    for c in array:
        if c in buffer:
            continue
        else:
            buffer += c
    return buffer
def randomMultipleEliminationsOneByOne(word):
    number = 0
    while True:
        number = random.randrange(len(word)-1)
        if number != 0:
            break
    character = word[number]
    array = re.split(r'',word)
    del array[0]
    array.pop()
    if word[number-1] == character:
        array[number-1] = ' '
    if word[number+1] == character:
        array[number+1] = ' '
    result = ''
    for i in range(len(array)):
        if array[i] != ' ':
            result += array[i]
    return result
def randomExchangeLetters(word):
    buffer = re.split(r'',word)
    del buffer[0]
    buffer.pop()
    number = random.randrange(len(word))
    try:
        buffer[number+1] = word[number]
        buffer[number] = word[number+1]
    except:
        buffer[number-1] = word[number]
        buffer[number] = word[number-1]
    return ''.join(buffer)
def randomReplaceWithNearestKey(word):
    word = word.lower()
    buffer = re.split(r'',word)
    del buffer[0]
    buffer.pop()
    number = random.randrange(len(word))
    
    #characters nearest to the char on the keyboard
    randA = ['q','s','z','w']
    randB = ['v','g','h','n']
    randC = ['x','d','f','v']
    randD = ['s','x','c','f','e','w']
    randE = ['w','s','d','f','r']
    randF = ['d','e','r','t','g','v','c']
    randG = ['f','t','y','h','b','v']
    randH = ['g','y','u','j','n','b']
    randI = ['u','j','k','l','o']
    randJ = ['h','n','m','k','u']
    randK = ['j','i','o','l','m']
    randL = ['k','p','o']
    randM = ['n','j','k','l']
    randN = ['b','h','j','m']
    randO = ['p','l','k','i']
    randP = ['o','l']
    randQ = ['a','w','s']
    randR = ['e','d','f','g','t']
    randS = ['a','w','d','x','z']
    randT = ['r','f','g','h','y']
    randU = ['y','h','j','k','i']
    randV = ['c','f','g','b']
    randW = ['q','a','s','d','e']
    randX = ['z','a','s','d','c']
    randY = ['t','g','h','j','u']
    randZ = ['a','s','x']
    randCol = ['l','p','k']
    
    
    if (word[number] == 'a'):
        buffer[number] = randA[random.randrange(len(randA))] #random nearest key to a
    elif (word[number] == 'b'):
        buffer[number] = randB[random.randrange(len(randB))]
    elif (word[number] == 'c'):
        buffer[number] = randC[random.randrange(len(randC))]
    elif (word[number] == 'd'):
        buffer[number] = randD[random.randrange(len(randD))]
    elif (word[number] == 'e'):
        buffer[number] = randE[random.randrange(len(randE))]
    elif (word[number] == 'f'):
        buffer[number] = randF[random.randrange(len(randF))]
    elif (word[number] == 'g'):
        buffer[number] = randG[random.randrange(len(randG))]
    elif (word[number] == 'h'):
        buffer[number] = randH[random.randrange(len(randH))]
    elif (word[number] == 'i'):
        buffer[number] = randI[random.randrange(len(randI))]
    elif (word[number] == 'j'):
        buffer[number] = randJ[random.randrange(len(randJ))]
    elif (word[number] == 'k'):
        buffer[number] = randK[random.randrange(len(randK))]
    elif (word[number] == 'l'):
        buffer[number] = randL[random.randrange(len(randL))]
    elif (word[number] == 'm'):
        buffer[number] = randM[random.randrange(len(randM))]
    elif (word[number] == 'n'):
        buffer[number] = randN[random.randrange(len(randN))]
    elif (word[number] == 'o'):
        buffer[number] = randO[random.randrange(len(randO))]
    elif (word[number] == 'p'):
        buffer[number] = randP[random.randrange(len(randP))]
    elif (word[number] == 'q'):
        buffer[number] = randQ[random.randrange(len(randQ))]
    elif (word[number] == 'r'):
        buffer[number] = randR[random.randrange(len(randR))]
    elif (word[number] == 's'):
        buffer[number] = randS[random.randrange(len(randS))]
    elif (word[number] == 't'):
        buffer[number] = randT[random.randrange(len(randT))]
    elif (word[number] == 'u'):
        buffer[number] = randU[random.randrange(len(randU))]
    elif (word[number] == 'v'):
        buffer[number] = randV[random.randrange(len(randV))]
    elif (word[number] == 'w'):
        buffer[number] = randW[random.randrange(len(randW))]
    elif (word[number] == 'x'):
        buffer[number] = randX[random.randrange(len(randX))]
    elif (word[number] == 'y'):
        buffer[number] = randY[random.randrange(len(randY))]
    elif (word[number] == 'z'):
        buffer[number] = randZ[random.randrange(len(randZ))]
    elif (word[number] == ';'):
        buffer[number] = randCol[random.randrange(len(randCol))]
    
    return ''.join(buffer)
if __name__ == '__main__':
    try:
        with open('dictionary.json','r') as d:
            dictionary = json.load(d)
            all_dict_words = list(map(lambda x: x, dictionary.keys()))
            #print(all_dict_words[:20])
        with open('words.txt','r') as w:
            words = [x.strip() for x in w.readlines()]
        for word in words:
            result = testDictionary(word)
            if result == False:
                print(f'Word "{word}" is not spelled correctly.')
                buffer = word
                random_count = 0
                while True:
                    if random_count <= 5000:
                        if random_count == 0:
                            print('Trying random exchange of letters')
                        buffer = randomExchangeLetters(word)
                        result = testDictionary(buffer)
                        if result == True:
                            break
                    if random_count > 5000 and random_count <= 7000:
                        if random_count == 5001:
                            print('Trying randomizing the word')
                        buffer = randomizeWord(word)
                        result = testDictionary(buffer)
                        if result == True:
                            break
                    if random_count == 7001:
                        print('Trying duplicate letter elimination')
                        buffer = multipleEliminationAllAtOnce(word)
                        result = testDictionary(buffer)
                        if result == True:
                            break
                    if random_count > 7001 and random_count <= 8000:
                        if random_count == 7002:
                            print('Trying duplicate elimination one-by-one')
                        buffer = randomMultipleEliminationsOneByOne(word)
                    if random_count > 8000:
                        if random_count == 8001:
                            print('Trying replacement with nearest keyboard key')
                        buffer = randomReplaceWithNearestKey(word)
                    if random_count > 10_900:
                        if random_count == 10_9001:
                            print('Trying the above 2 methods combined')
                        buffer = randomMultipleEliminationsOneByOne(word)
                        buffer = randomReplaceWithNearestKey(buffer)
                    if random_count == 11_900:
                        break
                    result = testDictionary(buffer)
                    if result == True:
                        break
                    random_count += 1
                if result == True:
                    print(f'Did you mean "{buffer}"?')
                else:
                    print('Word could not be resolved.')
                print()
    except IOError as e:
        print(e)