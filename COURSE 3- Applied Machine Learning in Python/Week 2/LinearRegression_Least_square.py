# Linear Regression with Least Square (Ordinary Square)(RSS)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

X_R1, y_R1 = make_regression(n_samples = 100, n_features=1,
                             n_informative = 1, bias = 150.0,
                             noise = 30, random_state= 0)
X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1, random_state=0)
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print('linear model coeff (w):{}'.format(linreg.coef_))
print('linear model intercept (b):{:.3f}'.format(linreg.intercept_))
print('R-Squared score (training): {:.3f}'.format(linreg.score(X_train, y_train)))
print('R-Squared score (testing) : {:.3f}'.format(linreg.score(X_test, y_test)))
