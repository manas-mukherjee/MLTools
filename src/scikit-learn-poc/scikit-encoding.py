''' http://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing '''

from sklearn import preprocessing
import pandas as pd

if True:
    # creating sample data
    sample_data = {'name': ['Ray', 'Adam', 'Jason', 'Varun', 'Xiao'],
                   'health': ['fit', 'slim', 'obese', 'fit', 'slim']}
    # storing sample data in the form of a dataframe
    data = pd.DataFrame(sample_data, columns=['name', 'health'])


# Label Encoder
if False:
    print data.head(5)

    # Categories: slim, fit, obese

    label_encoder = preprocessing.LabelEncoder()
    label_encoder.fit(data['health'])
    print label_encoder.transform(data['health'])

    # fit and transform
    print label_encoder.fit_transform(data['health'])

# One-hot encoder. Ref - http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html
# Ref - https://stackoverflow.com/questions/43588679/issue-with-onehotencoder-for-categorical-features
if True:
    # using pandas
    print pd.get_dummies(data['health'])

    # TODO: Didn't understand it well. Need to revisit
    # using scikit-learn

    ohe = preprocessing.OneHotEncoder(sparse=False)  # creating OneHotEncoder object
    label_encoder = preprocessing.LabelEncoder()
    label_encoded_data = label_encoder.fit_transform(data['health'])
    print label_encoded_data.reshape(-1, 1)
    print ohe.fit_transform(label_encoded_data.reshape(-1, 1))
