name = "Ada Balogun"
print(name.upper()) #uppercase

#Titlecase
sentence = "python is amazing"
print(sentence.title())

#Lowercase
sentence = "python is amazing"
print(sentence.lower())

# strip
text = "  Abuja   "
print(text.strip())
text = "   Ngozi is a smart lady@  ."
print(text.strip())

#replace()
message = "I love Java"
print(message.replace("Java","Python"))
message = "I love You"
print(message.replace("You", "Jesus"))

#swapcase
text = "Hello ABEOKUTA"
print(text.swapcase())

#Istrip()
text = "Nigeria     "
print(text.lstrip())

#rstrip()
text = "Nigeria  "
print(text.rstrip())

#split()
fruits = "mango orange banana"
print(fruits.split())

#rsplit
text = "one, two,three,four"
print(text.rsplit(",", 2))
 
 #splitlines()
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

#join()
words = ["I", "love", "Python"]
print(' '.join(words))

#Center
text = "Python"
print(text.center(10,"-"))

#ljust()
text = "python"
print(text.ljust(10, "*"))

#rjust
text = "Python"
print(text.rjust(10, "*"))

#zfill()
num = "43"
print(num.zfill(5))

#isalpha()
print("Lagos".isalpha()) #True
print("Lagos123".isalpha()) #False

#isdigit()
print("12345".isdigit()) #True
print("12345a".isdigit()) #False

#isalnum()
print("Python3".isalnum()) #True
print("Python 3".isalnum()) #false

#Task1
#Reverse a String
text = "ADA, oyibo"
print(text.swapcase())