fd = open("Input.txt", "r")
data = fd.read()
fd.close()

special_char = ",.?!"
for s_char in special_char:
    if s_char in data:
        data = data.replace(s_char, "")

word_list = data.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(f"{key} occurs : {value}")