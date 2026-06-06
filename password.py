password=input()
higher=False;lower=False;digit=False;special=False;space=False
for i in password:
    if i.isupper():
        higher=True
    elif i.islower():
        lower=True
    elif i.isdigit():
        digit=True
    elif i.isspace():
        space=True
    else:
        special=True

if len(password)>=8 and higher and digit and lower and special and not space:
    print("Valid Password")
else:
    print("Invalid Password")