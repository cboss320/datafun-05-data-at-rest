import pandas as pd 

titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 'Rdatasets/csv/carData/TitanicSurvival.csv')

pd.set_option('precision', 2) # format for the floating-point values 
titanic.head()





titanic.tail()





titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

titanic.head()



titanic.describe()

