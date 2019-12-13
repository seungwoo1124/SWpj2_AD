class Word:
    def __init__(self):
        pass

    def readWords(self, filename):
        words = {}
        f = open(filename, 'r')
        while True:
            line = f.readline()
            line.rstrip()
            if not line : break
            lst = line.split(" ")
            words[lst[0]] = str(lst[1:]).strip()
        return words

    def writeWords(self, filename, words): # 틀린 단어가 들어갈 text파일이름과 dic형태의 단어들이 들어감.
        f = open(filename, 'w')
        for key, value in words.items():
            f.write(key + " " + value)

