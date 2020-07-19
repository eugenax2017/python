import pandas as pd
import matplotlib.pyplot as plt #Before need to do: pip install matplotlib
#Series
my_series = pd.Series([5, 6, 7, 8, 9, 10])
print("My series is ",my_series)
print(my_series.index)
print(my_series.values)
print("Value[4] is ",my_series[4])
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print("Value[f] is ",my_series2['f'])
print("My series2['a', 'b', 'f'] is ",my_series2[['a', 'b', 'f']])
my_series2[['a', 'b', 'f']] = 0
print("My series2 is ",my_series2)
print("My series2 > 0 is ",my_series2[my_series2 > 0])
print("My series2 * 2 > 0 is ",my_series2[my_series2 > 0] * 2)
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print("My series3 is ",my_series3)
print("'d' in My series3 ",'d' in my_series3)
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print("My series3 is ",my_series3)
my_series3.index = ['A', 'B', 'C', 'D']
print("My series3 is ",my_series3)
#DataFrame
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
	'population': [17.04, 143.5, 9.5, 45.5],
	'square': [2724902, 17125191, 207600, 603628]})
print("Df is ",df)
print("Df['country'] is ",df['country'])
print("df.columns is ",df.columns)
print("df.index is ",df.index)
df2 = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
	'population': [17.04, 143.5, 9.5, 45.5],
	'square': [2724902, 17125191, 207600, 603628]}, 
	index = ['KZ', 'RU', 'BY', 'UA'])
print("Df2 is ",df2)
df2.index = ['KZ', 'RU', 'BY', 'UA']
df2.index.name = 'Country Code'
print("Df2 is ",df2)
print("Df2['country'] is ",df2['country'])
print("Df2.loc['KZ'] is ",df2.loc['KZ'])
print("Df2.iloc[0] is ",df2.iloc[0])
print("Df2.loc[['KZ', 'RU'], 'population'] is ",df2.loc[['KZ', 'RU'], 'population'])
print("Df2.loc['KZ':'BY', :] is ",df2.loc['KZ':'BY', :])
print("Df2[df.population > 10][['country', 'square']]",df[df.population > 10][['country', 'square']])
print("Df2.reset_index()", df2.reset_index())
df2['density'] = df2['population'] / df2['square'] * 1000000
print("Df2 after insert a column is ",df2)
print("Df2 after delete a column is ",df2.drop(['density'], axis='columns')) #or del df['density']
df2 = df2.rename(columns={'Country Code': 'country_code'})
print("Df2 after rename a column is ",df2)
#df2.to_csv('country.csv')
#Groupby
titanic_df = pd.read_csv('titanic.csv')
print(titanic_df.head())
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())
print(titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count())
titanic_df = pd.read_csv('titanic.csv')
pvt = titanic_df.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
print(pvt)
print(pvt.loc['female', ['1st', '2nd', '3rd']])
pvt2 = titanic_df.pivot_table(index=['Age'], columns=['PClass', 'Survived', 'Sex'], values='Name', aggfunc='count')
print(pvt2.loc[39, ['1st', '2nd', '3rd', 0, 1, 'male', 'female']])
print(pvt2.loc[40, ['1st', '2nd', '3rd', 0, 1, 'male', 'female']])
print(pvt2.loc[41, ['1st', '2nd', '3rd', 0, 1, 'male', 'female']])
df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
df = df.sort_index()
print(df.info())
print("df.loc['2012-Feb', 'Close'].mean()", df.loc['2012-Feb', 'Close'].mean())
print("df.loc['2012-Feb':'2015-Feb', 'Close'].mean()", df.loc['2012-Feb':'2015-Feb', 'Close'].mean())
print("df.resample('W')['Close'].mean()", df.resample('W')['Close'].mean())
new_sample_df = df.loc['2012-Feb':'2017-Feb', ['Close']]
new_sample_df.plot()
plt.show()


input()