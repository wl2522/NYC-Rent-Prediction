This project aims to predict the monthly rent cost for vacant properties based on data from the 2014 New York City Housing and Vacancy Survey.

Feature selection was done by manually reviewing the list of features described in occ_14_long.xls and removing features for one of the following reasons:

1) the feature related to the occupants of the property rather than the property itself (for example, those concerning household demographics or government assistance elegibility)

2) the feature only applies to properties that are being occupied rent-free or by the owner

3) the feature directly relates to the monthly rent and would cause information leakage if left in the model (for example, features relating to utilities costs and whether or not a specific utility cost is included in the monthly rent)

4) the feature is an indicator variable that relates to another feature that was already taken into account

This program is written in Python 3 and uses the pandas, NumPy, and scikit-learn packages. The data is loaded and preprocessed using pandas. This consists of dropping columns containing features that were selected for removal during feature selection. Afterward, one-hot encoding is performed on the categorical variables (highlighted in yellow in occ_14_long.xls) so that the numerical encodings used for these categories in the original data aren't mistakenly interpreted as indicating a natural ordering to the categories.

Afterward, the data is converted into NumPy arrays and split into training and test sets using scikit-learn. A pipeline is created to automatically normalize the data using StandardScaler() and fit the data to a ridge regression model. A grid search is then performed to test prediction accuracy for all values of the ridge regression penalty term "alpha" from 1 to 50. The test data is then applied to the model using the alpha value with the best test accuracy.

The score_rent() function returns the prediction accuracy score achieved using this alpha value and the predict_rent() function returns the test set data, test values, and the model predictions.

This program will be expanded upon in the future to incorporate the following steps:

1) F-score analysis of the features to detect and remove features that are correlated, which would presumably increase test prediction accuracy

2) Imputing missing values rather than dropping all rows with missing values and seeing if prediction accuracy is improved

3) Examining rows with missing values to see if there could be some underlying reason for why certain properties contain missing values (for example, missing values for features related to the exterior condition of a property might be due to the fact that the property is in a wealthy gated community, meaning that visual inspection of the property was not possible)
