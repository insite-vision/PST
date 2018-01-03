import os
import numpy as np
import tensorflow as tf
import pickle

from matplotlib import pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from tensorflow.examples.tutorials.mnist import input_data

##Decode and put in a dataset the images
TRAIN_DIR = 'Examples/train/'
TEST_DIR = 'Examples/test/'

train_image_filenames = [TRAIN_DIR+i for i in os.listdir(TRAIN_DIR)][0:1500]
test_image_filenames = [TEST_DIR+i for i in os.listdir(TEST_DIR)][0:500]

def getImages(image_Filename, labels):
    images = []

    for image in image_Filename:
        ImageArray = io.imread(image, as_grey=True)
        imageArray = np.array(ImageArray)
        imageArray = rgb2gray(imageArray)
        images.append(ImageArray.flatten())
        if "_G" in image:
            labels.append([1,0])
        else:
            labels.append([0,1])

    return images



trainLabel = []
testLabel = []

train_image = getImages(train_image_filenames, trainLabel)
test_image= getImages(test_image_filenames, testLabel)



print "Size of training dataset : "+ str(len(train_image))
print "Size of test dataset : "+ str(len(test_image))

print (np.shape(train_image))
print (np.shape(test_image))


##Start of the Neural Net part

saver = tf.train.Saver()
sess = tf.InteractiveSession()


x  = tf.placeholder(tf.float32, shape=[None, 2500])#Will be 2500 
y_ = tf.placeholder(tf.float32, shape=[None, 2])#Will be 2

W = tf.Variable(tf.zeros([2500, 2])) #Weigth (2500 inputs and 2 outputs)
b = tf.Variable(tf.zeros([2])) #Bias (2 classes)

sess.run(tf.global_variables_initializer()) #Init all Variables

y = tf.matmul(x, W) + b #regression and output

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

for i in range(15):
    #batch = mnist.train.next_batch(100)
    print i
    batch = train_image[i*100:i*100+100]
    batchLabel = trainLabel[i*100:i*100+100]
    train_step.run(feed_dict={x: batch, y_: batchLabel})
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    print (accuracy.eval(feed_dict={x: test_image, y_: testLabel}))

saver.save(sess, 'Simple_NN', global_step = 1000)
