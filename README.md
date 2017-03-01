The function score_rent performs the following tasks:

1) Download the housing data from the provided URL and stores it as a pandas dataframe
2) Drop the feature columns related to occupants and not apartments
3) Drop the feature columns that are related to properties occupied by their owners
4) Drop rows for which the "Monthly Contract Rent" column (the response variable) has a missing value
5) Drop any rows with missing values
6) Perform one hot encoding on the remaining columns that contain categorical features
7) Separate the response variable "Monthly Contract Rent" from the test data
8) Create a pipeline and perform standard scaling and grid search for the best ridge regression alpha parameter in the range 1-50
9) score_rent(): Return the R^2 score achieved using the best alpha value found by grid search
10) predict_rent(): Returns the test data, true labels, and predicted labels used to score the model
