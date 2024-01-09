# word frequency counter

from lineoftext import LineOfText
from wordfrequencytable import WordFrequencyTable
from stats import Stats

lot = LineOfText("ក្រោយចេញពីសាលា ខ្ញុំទៅហាត់ប្រដាល់ថៃ។ ខ្ញុំរីករាយនឹងកីឡានេះណាស់។")

st = Stats()
wft = WordFrequencyTable()

st.accumulateCounts(lot)
wft.accumulateFrequency(lot)

st.printStats()
wft.printWordFreqList()