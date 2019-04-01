import tensorflow as tf

LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.99
LEARNING_RATE_STEP = 1

global_step = tf.Variable(0, trainable = False)

learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step,
        LEARNING_RATE_STEP, LEARNING_RATE_DECAY, staircase = True)
w = tf.Variable(tf.constant(5, dtype = tf.float32))

loss = tf.square(w + 1)

train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,
        global_step = global_step)

with tf.Session() as se:
    init_op = tf.global_variables_initializer()
    se.run(init_op)
    for i in range(40):
        se.run(train_step)
        learning_rate_val = se.run(learning_rate)
        global_step_val = se.run(global_step)
        w_val = se.run(w)
        loss_val = se.run(loss)
        print("After %s steps: global_step is %f, w is %f, learning_rate is %f, loss is %f" % (i, global_step_val, w_val, learning_rate_val, loss_val))
