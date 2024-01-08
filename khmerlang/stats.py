from lineoftext import LineOfText


## Statistics Class

class Stats:

    def __init__(self):
        self.wordcount = 0
        self.sentencecount  = 0
        return
    
    def accumulateCounts(self, lineoftext: LineOfText):
        self.wordcount = self.wordcount + lineoftext.getWordCount()
        self.sentencecount = self.sentencecount + lineoftext.getSentenceCount()
        return
