Data={
    "Name":"Muhammad Yousuf",
    "Age":20,
    "license": False
}

for key, val in Data.items():
    print(f"{key}: {val}")
    
print(Data.get("BirthDate", "10th Jan 2004"))

numbers={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}

num=input("Write any number:")

output=''
for ch in num:
    output+=numbers.get(ch) + " "
    
print(output)