from sklearn.ensemble import RandomForestClassifier
import re
from sklearn.externals import joblib
import numpy

def testData(Xtest):
    clf2 = joblib.load("classifier/classifier.pk1");
    res = RandomForestClassifier.predict(clf2, Xtest);
    probs = RandomForestClassifier.predict_proba(clf2, Xtest);
    prob = numpy.mean(probs[0])
    return [res[0], prob];
