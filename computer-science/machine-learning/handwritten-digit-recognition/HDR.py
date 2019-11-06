import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from random import randint

# Read the file into a matrix. Each row corresponds to an image.
# The first column is the label and the rest are pixels in the image.
data = pd.read_csv("datasets/train.csv").as_matrix()

# create a decision classifier object
clf = DecisionTreeClassifier()

# print the matrix
#print(data)

# split the data into training data and validation data
# training data set
train_data = data[0:21000, 1:] # use the first 21000 images
train_label = data[0:21000, 0] # get the labels for those images

# train our model
clf.fit(train_data, train_label)

# validation data set
test_data = data[21000:, 1:]
test_label = data[21000:, 0]
num_test = test_data.shape[0]

# predict a random image
random_image = randint(0, num_test - 1)
d = test_data[random_image]
d.shape = (28, 28)
pt.imshow(255 - d, cmap = 'gray') # reverse the color
print(clf.predict( [test_data[random_image]] )) # predict a new picture
pt.show() # show the image

# calculate the accuracy with our validation set
predict = clf.predict(test_data) # predict all test data
count = 0
for i in xrange(num_test):
    if predict[i] == test_label[i]:
        count += 1
print "Accuracy =", (float(count) / num_test * 100)
