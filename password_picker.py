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

adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)
password = adjective + noun +str(number) + special_char
print ('Your new password is: %s' % password)