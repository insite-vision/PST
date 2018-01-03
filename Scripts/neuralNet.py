import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 2500])

W = tf.Variable(tf.zeros([2500, 2]))
b = tf.Variable(tf.zeros([2]))


y = tf.nn.softmax(tf.matmul(x, W) + b)


