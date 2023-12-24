# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.


# Function:
def atbash(txt):
    right = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!']
    left =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!']
    zip_lis = zip(left, right)
    myDict = dict(zip_lis)
    myList = []
    for i in txt:
        if i in myDict:
            myList.append(myDict.get(i))
            
    print("".join(myList))

atbash("apple") # ➞ "zkkov"

atbash("Hello world!") # ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") # ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
