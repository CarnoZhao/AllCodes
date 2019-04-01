import tensorflow as tf

w1 = tf.Variable(0, dtype = tf.float32)

global_step = tf.Variable(0, trainable = False)

MOVING_AVERGAE_DECAY = 0.99

ema = tf.train.ExponentialMovingAverage(MOVING_AVERGAE_DECAY, global_step)

ema_op = ema.apply(tf.trainable_variables())

with tf.Session() as se:
    init_op = tf.global_variables_initializer()
    se.run(init_op)
    print(se.run([w1, ema.average(w1)]))

    se.run(tf.assign(global_step, 100))
    se.run(tf.assign(w1, 10))
    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))

    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))

    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))
    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))
    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))
    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))
    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))
    se.run(ema_op)
    print(se.run([w1, ema.average(w1)]))
