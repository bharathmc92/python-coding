greeting = "HELLO WORLD!"
print(greeting[0])
print(greeting[11])
print(len(greeting))

#ex:2
word1 = "Good"
word2 = "Morning"
end1 = word1[2] + word1[3] + word2[4]
print(end1)

#using slices to access parts of a string
word = "PYTHON"
w = word[2:5]
print(w)

#slice formula and shortcuts
a = word1[0:2]
b = word1[2:4]
print(a,b)

#using string slice shortcut
print(a, word2[2:6])

#index at the halfway point
half1 = len(word1)/2
half2 = len(word2)/2
print(half1)
print(half2)
half3 = len(word1)//2
half4 = len(word2)//2
print(half3)
print(half4, ",", len(word2))

#making our program more reusable
word1 = "Good"
half1 = len(word1)//2
end = word1[half1:]
word2 = "Evening"
half2 = len(word2)//2
end3 = word2[half2:]
print(end,end3)
