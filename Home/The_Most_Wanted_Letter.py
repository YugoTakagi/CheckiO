def checkio(letter_before):
    #replace this for solution
    maxnum=0
    word='a'
    letter = ''.join(str.lower(letter_before).rsplit())
    for l in letter:
        if "a"<=l<="z":
            counter = letter.count(l)
            if maxnum < counter:
                maxnum = counter
    words = [w for w in letter if maxnum == letter.count(w)]
    for w in sorted(words):
        if "a"<=w<="z":
            return w
        else:
            pass
if __name__ == '__main__':
    word = checkio('a -z')
    print(word)
