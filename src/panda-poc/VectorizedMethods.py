#import pandas as pd
from pandas import DataFrame, Series
import numpy as np

data = {'one': Series([1,2,3], index=['a','b','c']),
        'two': Series([1,2,3,4], index=['a','b','c','d'])}

if False:
    df = DataFrame(data)
    print df
    print df.apply(np.mean)

# Lambada
if False:
    df = DataFrame(data)
    print df
    print df['one'].map(lambda x : x> 1)
    print df.applymap(lambda x : x > 1)


'''
You might find using "boolean indexing" helpful for this problem.
Here is a link to the pandas documentation.
Here's also an excellent series of tutorials as IPython notebooks
'''


def avg_bronze_medal_count():
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medal_counts = {'country_name': Series(countries),
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    df = DataFrame(olympic_medal_counts)

    avg_bronze_at_least_one_gold =np.mean(df[df.gold>=1].bronze)

    return avg_bronze_at_least_one_gold

print avg_bronze_medal_count()