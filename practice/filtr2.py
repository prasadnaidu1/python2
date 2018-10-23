vowels='aeiouAEIOU'
finalvowel=[]
str='prasad'
str1=list(filter(lambda str: vowels if str in vowels else str,str))
finalvowel.append(vowels)
print(str1)
