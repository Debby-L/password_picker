#密碼產生器
#密碼: adj+n+num+標點符號
#建立隨機random/字串模組
#建立模組清單
#利用隨機模組裡的函式choice()挑選清單內容
#randrange(0,100)隨機選數字0~99
#挑選特殊字元special_char = random.choice(string.punctuation)
import random
import string
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange','yellow','green', 'blue']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'duck']
print ('Welcom to password picker!')

#加入迴圈多次產生密碼
while True:
    for num in range(3): #for迴圈指定執行三次程式碼，一次產生三個不同密碼
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
    
        password = adjective + noun +str(number) + special_char
        print ('Your new password is: %s' % password)

#詢問使用者是否需要更新密碼
    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
    	break