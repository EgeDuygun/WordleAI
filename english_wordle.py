import numpy as np
import time

start = time.time()

file = open('answers.txt', 'r')

file.readline()

all_words = [line[-6:-1] for line in file]
answers = [all_words[i] for i in range(2315)]

file.close()

def get_class(word, target):
    
    word = word.lower()
    output = ""
    
    for i in range(len(word)):
        if word[i] not in target:
            output += "b"
        elif word[i] == target[i]:
            output += "g"
        else:
            output += "y"
            
    return output


def get_entropy(word, current_list):
    
    probs = {}
    
    for i in current_list:
        word_class = get_class(word,i)        
        if word_class not in probs:
            probs[word_class] = 1/len(current_list)
        else:
            probs[word_class] += 1/len(current_list)
            
    entropy = 0
    
    for k in probs:
        entropy += probs[k] * (-np.log2(probs[k]))
    
    return entropy



def narrow_list(guess, output, current_list):
    
    l_form = output.split()
    s_form = set(l_form)
    
    
    if len(s_form) == len(output):    
    
        for i in range(len(output)):
            
            if output[i] == "g":       
                for j in current_list[:]:
                    if guess[i] != j[i]:
                        current_list.remove(j)
            
            elif output[i] == "b":
                for j in current_list[:]:
                    if guess[i] in j:
                        current_list.remove(j)
                        
            else:
                for j in current_list[:]:
                    if (guess[i] not in j) or (guess[i] == j[i]):
                        current_list.remove(j)
                        
    else:
        
        for i in range(len(guess)):
            cnt = guess.count(guess[i])
            
            if cnt == 1:
                
                if output[i] == "g":       
                    for j in current_list[:]:
                        if guess[i] != j[i]:
                            current_list.remove(j)
                
                elif output[i] == "b":
                    for j in current_list[:]:
                        if guess[i] in j:
                            current_list.remove(j)
                            
                else:
                    for j in current_list[:]:
                        if (guess[i] not in j) or (guess[i] == j[i]):
                            current_list.remove(j)
                            
            else:
                strng = ""              
                    
                for j in range(len(guess)):
                    
                    if (guess[i] == guess[j]):
                        strng += output[j]
                    else:
                        strng += "_"
                        
                #print(strng)
                    
                if (strng.count("b") == cnt):
                    for j in current_list[:]:
                        if guess[i] in j:
                            current_list.remove(j)
                            
                elif ("b" in strng) and ("g" in strng):
                    idx = strng.find("g")
                    for j in current_list[:]:
                        if (guess[idx] != j[idx]):
                            current_list.remove(j)
                            
                elif ("b" in strng) and ("y" in strng):
                    idx = strng.find("y")
                    for j in current_list[:]:
                        if (guess[idx] not in j):
                            current_list.remove(j)
                            
    return current_list
                    

def prediction(curr_list):
    
    entropies = {}
    
    for i in curr_list:
        entropies[i] = get_entropy(i, curr_list)
        
    sorted_ent = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_ent


pred = prediction(answers)

print("Your set of first guesses should be:", pred[0:10])

guess = 0

while True:    
    
    
    pred = str(input("What is your answer?: ")).lower() 
    
    if len(pred) != 5 or (pred not in answers):
        while True:
            pred = str(input("Please make a valid guess!: ")).lower() 
            if len(pred) == 5 and (pred in answers):
                break
        
    guess += 1
    inp = str(input("What is the current response (in terms of g = green, y = yellow, b = black): ")).lower()  
    
    if inp == "ggggg":
        print("Congratulations! The word was '"+ str(pred)+ "' and you have found it in", guess,"trials!")
        break

    
    
    answers.remove(pred)
    answers = narrow_list(guess = pred, output = inp, current_list = answers)
    
    pred_list = prediction(answers)

    print("Your new guess should be:", pred_list)

    


end = time.time()

print("It took this seconds:", end-start)




