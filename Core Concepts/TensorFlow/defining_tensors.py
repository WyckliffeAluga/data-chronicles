import tensorflow as tf

# OD Tensor
d0 = tf.ones((1,))

#1D Tensor
d1 = tf.ones((2,))

# 2D Tensor
d2 = tf.ones((2,2))

# 3D tensor
d3 = tf.ones((2,2,2))

print(d3.numpy)
