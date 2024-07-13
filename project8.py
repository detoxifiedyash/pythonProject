#typing speed
from time import *
import random as r


def mistake(paratest, usertest):

    error = 0
  
    min_length = min(len(paratest), len(usertest))
   
    for i in range(min_length):
        if paratest[i] != usertest[i]:
            error += 1
    
    error += abs(len(paratest) - len(usertest))
    
    return error
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed =  len(userinput)/ time_R
    return round(speed)

#you can add anything of your choice in the paragraph as a test case
test = ["You are supposed to write a paragraph and i will calculate your speed",
"i am yash","lewis hamilton is the goat","the world is mine","how's going","go forever in therapy heeps november geography","you can eat what you think",
"alex pareira is currently the best in the category but he may not win against the goat jon jones"]
test1 = r.choice(test)
print("*** typing speed calculator ***")

print(test1)
print()
print()
time_1 = time()
testinput=input(" Enter your word : ")
time_2 = time()

print('Speed : ',speed_time(time_1, time_2, testinput),"w/sec")
print("Error : ",mistake(test1, testinput))
