# Import library to read the data
import pandas as pnds

# Download data and save to irisData
dataURL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
irisData = pnds.read_csv(dataURL, on_bad_lines='skip', header=None)
irisData1 = pnds.DataFrame(irisData)
irisData1.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

#Confirm data exists
headData = irisData1.head(10)
print('\n\nSAMPLE DATA \n')
print('\n===============================================================================\n')
print(headData)
print('\n===============================================================================\n')

# Statisctics summary
print('\n\n DESCRIPTIVE STATISTICS\n')
print('\n===============================================================================\n')
print(irisData1.describe())
print('\n===============================================================================\n')
