# word frequency counter

from lineoftext import LineOfText
from wordfrequencytable import WordFrequencyTable
from stats import Stats

#lot = LineOfText("ក្រោយចេញពីសាលា ខ្ញុំទៅហាត់ប្រដាល់ថៃ។ ខ្ញុំរីករាយនឹងកីឡានេះណាស់។")

st = Stats()
wft = WordFrequencyTable()



with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lot = LineOfText(line)
        st.accumulateCounts(lot)
        wft.accumulateFrequency(lot)
      


#st.accumulateCounts(lot)
#wft.accumulateFrequency(lot)

st.printStats()
wft.writeWordFreqList()