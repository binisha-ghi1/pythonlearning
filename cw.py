#write a program to detect double space in a string.
sentence = input("Enter a sentence: ")
if "  " in sentence:
    print("Please, avoid double spacing (    )")
else:
    print("No double space found")


    #replace the double space from problem a with a single space
sentence1 = input("Enter your name: ")  
sentence2 = sentence1.replace("  ", " ")  
print("Original sentence:", sentence1)
print("Fixed sentence   :", sentence2)


#write a program to format the following letter using escape sequence character
#letter ="Dear Students, This python course is going well . Thank you"
letter = "Dear Students,\nThis python course is going well.\nThank you"
print(letter)   