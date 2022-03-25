# Library to read online text files
import urllib.request as urllib
from collections import Counter
from matplotlib import pyplot

# Download he text file
file = urllib.urlopen('https://www.apache.org/licenses/LICENSE-2.0.txt')

#Read file contents
fileContents = file.read().decode('utf-8').lower()
# print(type(fileContents))

#Counter for the text's characters
vowels = ['a', 'e', 'i', 'o', 'u']
vowelFrequencyDict = {}
characterFrequency = Counter(fileContents)

for v in vowels:
    vowelFrequency = characterFrequency.pop(v)
    vowelFrequencyDict[v] = vowelFrequency
# Frequency Data
print('\n\nVOWEL FREQUENCY DATA\n')
print('\n===============================================================================\n')
print(vowelFrequencyDict)
print('\n===============================================================================\n')
#Configure visualization

vowels = list(vowelFrequencyDict.keys())
frequency = list(vowelFrequencyDict.values())

#Show visualizations

pyplot.bar(range(len(vowelFrequencyDict)), frequency, tick_label = vowels)
pyplot.title('Vowel Frequency bar chart')
pyplot.xlabel('Vowels')
pyplot.ylabel('Frequency')
print('Plot being created please wait ...\n\n\n')
pyplot.show()


