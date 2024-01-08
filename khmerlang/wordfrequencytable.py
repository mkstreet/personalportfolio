from lineoftext import LineOfText


class WordFrequencyTable:
    def __init(self):
        self.fdict = dict()
        return
    
    def accumulateFrequency(self,  lo_text : LineOfText):

        for tok in lo_text.getTokList():
            val = self.fdict.get(tok)

            if val != None:
                val = val + 1
            else:
                val = 1

            self.fdict.update({ tok : val })
        return

            
            