pattern = "abba"
pattern_list = list(pattern)
s = "dog cat cat dog"
words = list(s.split())
if len(pattern)!= len(words):
    print(False)
dict1 = {}

for i in range(len(s)):
    dict1[pattern_list[i]] = words[i]
    if dict1[pattern_list[i]] in dict1:
        continue
print(dict1)