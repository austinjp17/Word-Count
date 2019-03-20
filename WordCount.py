
class letters:
    wordList = []
    secondWordList = []
    TextDocument = open('FILEPATH', 'r').read()  #Enter Path to text file here
    splitTextDocument = TextDocument.translate(None, ',.!').split()
    def __init__(self, *argv):
        print('\n')
        for arg in argv:
            for word in self.splitTextDocument:
                if arg in word:
                    self.wordList.append(word)
            print ('\n' + arg + ': ' + str(len(self.wordList)) + '\n')
            self.wordList = []
        print('\n')


#Call as shown below with at least 1 argument
letters('h', 'asd', 'fdsd')
# letters('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
