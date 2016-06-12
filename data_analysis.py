import re
from sklearn.ensemble import RandomForestClassifier
#import pickle
from sklearn.externals import joblib

def readCSV(fname):
    with open(fname,'rb') as file:
        data = []
        classes = [];
        for line in file:
            row = [x for x in re.split("[,\n]", line) if x];
            data_row = [];
            for r in range(len(row)):
                if r != len(row)-1:
                    if row[r] == 'no':
                        data_row = data_row + [0];
                    else:
                        data_row = data_row + [1];
                else:
                    if row[r] == 'no':
                        classes = classes + [0];
                    else:
                        classes = classes + [1];
            data_row[0] = float(row[0]);
            data = data + [data_row];
    return [data, classes];


def predictData(X,Y,testX):
    clf = RandomForestClassifier(n_estimators=20);
    clf = clf.fit(X, Y);
    res = RandomForestClassifier.predict(clf, testX);

    return(res[0]);

def loocv(X,Y):
    cm = [0,0,0,0]; # 1=TP 2=FP 3=FN 4=TN
    for i in range(len(Y)):
        testY = Y[i];
        testX = X[i];
        trainingX = X[0:i] + X[i+1:len(Y)];
        trainingY = Y[0:1] + Y[i+1:len(Y)];
        predY = predictData(X,Y,testX);
        if (predY == testY and testY == 0):
            cm[3] += 1;
        elif (predY == testY and testY == 1):
            cm[0] += 1;
        elif (predY != testY and testY == 0):
            cm[2] += 1;
        else:
            cm[1] += 1;
    return cm;


[X, Y] = readCSV('urinary_inf_data.csv');

cm = loocv(X,Y);
print cm

clf = RandomForestClassifier(n_estimators=20exit()
    );
clf = clf.fit(X, Y);
sco = RandomForestClassifier.score(clf, X, Y)
print sco
joblib.dump(clf, "classifier/classifier.pk1")