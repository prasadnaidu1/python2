vowels='aeiouAEIOU'
finalvowel=[]
def increment(sentence):
    for letter in sentence:
        if letter in vowels:
            finalvowel.append(letter)
    return finalvowel
k=increment('prasadnaidu is good boy and he has good habbits. recenctly he completed his post graduation. now he is doing python software course')
print(k)
