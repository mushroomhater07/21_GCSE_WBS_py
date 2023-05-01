#Find the index values from the array alphabet for the letters in the word "computer"

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = "computer"

for indexW in range(len(word)):
  for indexA in range(len(alphabet)):
    if word[indexW] == alphabet[indexA]:
      print(indexA)
