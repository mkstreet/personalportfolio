from khmernltk import sentence_tokenize
from khmernltk import word_tokenize


class LineOfText:

    def __init__(self, txt) :
        
        self.scount = len(sentence_tokenize(txt))

        self.wtokens = word_tokenize(txt)
        self.wcount =  len(self.wtokens)
        
        return
    


    def getSentenceCount(self) -> int:
        return self.scount
    

    
    def getWordCount(self) -> int:
        return self.wcount
    

    def getTokList(self) -> list:
        return  self.wtokens.copy()
    



