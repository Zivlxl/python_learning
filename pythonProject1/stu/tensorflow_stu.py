import tensorflow
import tensorflow as tf

a = tf.constant([[3.,3.]])
b = tf.constant([[2.],[2.]])

y = tf.matmul(a, b)

with tf.Session() as se:
    result = se.run(y)
    print(result)

print(tf.operation.device)