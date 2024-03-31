emojis={
    ":):"!!!",
    ":(":"😕"
    }

output=''
tense=input("Say something...")
if tense[-1] in emojis:
    output+=tense.get(emojis)
    
print(output)

