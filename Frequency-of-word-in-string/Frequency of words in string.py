# Frequency-of-word-in-string

def most_frequent():
    str=input("Enter a string ")
    li=str.split()
    d={}

    for i in li:
        if i not in d.key():
            d[i]=0
        d[i]=d[i]+1
    print(d)

most_frequent()
