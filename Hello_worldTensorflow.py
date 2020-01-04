from __future__ import print_function

import tensorflow as tf

#Create op ,
#start session 
#print the op in the String format 
hello = tf.constant('Hello World, TensorFlow! Here')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))
