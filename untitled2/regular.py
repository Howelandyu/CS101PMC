import string
import challange3
#bigCharacter =   ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
bigCharacter = string.ascii_uppercase
#smallCharacter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
smallCharacter = string.ascii_lowercase
print(smallCharacter[1])
txtStore = []

for character in challange3:
    txtStore.append(character)

for i in range(0,len(txtStore)-7):
    if txtStore[i] in smallCharacter and txtStore[i+1] in bigCharacter and txtStore[i+2] in bigCharacter and txtStore[i+3] in bigCharacter and txtStore[i+4] in smallCharacter and txtStore[i+5] in bigCharacter and txtStore[i+6] in bigCharacter and txtStore[i+7] in bigCharacter and txtStore[i+8] in smallCharacter:
        print(txtStore[i:i+9])