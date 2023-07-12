text = input("Enter the text: ")
wrd = ",.<>?/';:]}{[|`~!"
new_text = ''.join(a.lower() if a not in wrd else ' ' for a in text).split()
new_dict = {i: new_text.count(i) for i in  new_text}
print(new_dict)
