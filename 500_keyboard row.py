def findWords(words):
    ans = []
    keyset = ['qwertyuiop', 'asdfghjkl','zxcvbnm']
    for key in keyset:
        for word in words:
            line = set(word.lower())
            if line.issubset(set(key)):
                ans.append(word)
    return ans


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    word = findWords(words)
    print(word)
 