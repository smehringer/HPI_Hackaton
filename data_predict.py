from sklearn.ensemble import RandomForestClassifier
import re
from sklearn.externals import joblib

def testData(Xtest):
    clf2 = joblib.load("classifier/classifier.pk1");
    res = RandomForestClassifier.predict(clf2, Xtest);
    return res
