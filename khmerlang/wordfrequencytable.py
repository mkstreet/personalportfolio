from lineoftext import LineOfText


class WordFrequencyTable:
    def __init__(self):
        self.fdict = {}

        self.excld = {"។" : "។", " ":" ", "":""}
        return
    
    def accumulateFrequency(self,  lo_text : LineOfText):

        for tok in lo_text.getTokList():
            tok = tok.strip()

            if self.excld.get(tok)  ==  None:
                val = self.fdict.get(tok)
                

                if val != None:
                    val = val + 1
                else:
                    val = 1

                self.fdict.update({ tok : val })
        return

    def writeWordFreqList(self):
        f = open("wft", "w")

        for w in self.fdict.keys():
            f.write(w + " = " + str( self.fdict.get(w)) + "\n")
            #print(w, " =  ", self.fdict.get(w))
        f.close()
        return
            