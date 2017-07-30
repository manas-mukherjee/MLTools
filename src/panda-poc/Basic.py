import pandas as pd

'''

You can think of Series as an one-dimensional object that is similar to
an array, list, or column in a database. By default, it will assign an
index label to each item in the Series ranging from 0 to N, where N is
the number of items in the Series minus one.

http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''
# POC
if False:
    data = {'name': pd.Series(['Manas', 'Teddy', 'Deepti', 'Raju'], index=['a', 'b', 'c', 'd']),
            'age':  pd.Series([31,28,30], index=['a', 'b', 'd']),
            'inUS': pd.Series([True, True, False, False], index=['a','b','c','d'])}

    df = pd.DataFrame(data)
    print df

# Change False to True to create a Series object
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print series

'''
You can also manually assign indices to the items in the Series when
creating the series
'''

# Change False to True to see custom index in action
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print series

'''
You can use index to select specific items from the Series
'''
# Change False to True to see Series indexing in action
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print series['Instructor']
    print ""
    print series[['Instructor', 'Curriculum Manager', 'Course Number']]

'''
You can also use boolean operators to select specific items from the Series
'''
# Change False to True to see boolean indexing in action
if True:
    cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
    print cuteness > 3
    print ""
    print cuteness[cuteness > 3]
