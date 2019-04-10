import os

import numpy as np
from PIL import Image
import tensorflow as tf
from skimage.color import rgb2gray
from tensorflow.python.tools import freeze_graph, optimize_for_inference_lib

from ReadLables import get_labels

MODEL_NAME = 'EmotionDetectionVGG_ferplus_8classes_100_with_filter'
NUM_EPOCHS = 100
BATCH_SIZE = 128

def to_grayscale(images):
    grayScaleImages = rgb2gray(images)
    grayScaleImages = np.array(grayScaleImages)
    return grayScaleImages

def load_data(data_directory,test_directory):
    print('Loading images...')

    train_images = []
    train_classes = []
    test_images = []
    test_classes = []

    labels = get_labels("FER2013Train")

    file_names = [os.path.join(data_directory, f)
                  for f in os.listdir(data_directory)
                  if f.endswith(".png") or f.endswith(".jpg")]

    for i, f in enumerate(file_names):
        if os.listdir(data_directory)[i] in labels:
            train_classes.append(labels[os.listdir(data_directory)[i]])
            aux_image = Image.open(f)
            aux_image = aux_image.resize([64, 64])
            aux_image = aux_image.convert('RGB')
            data_image = to_grayscale(np.array(aux_image))
            data_image = np.array(data_image).flatten()
            train_images.append(data_image)

    labels = get_labels("FER2013Test")

    file_names = [os.path.join(test_directory, f)
                  for f in os.listdir(test_directory)
                  if f.endswith(".png") or f.endswith(".jpg")]

    for i, f in enumerate(file_names):
        if os.listdir(test_directory)[i] in labels:
            aux_image = Image.open(f)
            aux_image = aux_image.resize([64, 64])
            aux_image = aux_image.convert('RGB')
            data_image = to_grayscale(np.array(aux_image))
            data_image = np.array(data_image).flatten()
            test_images.append(data_image)
            test_classes.append(labels[os.listdir(test_directory)[i]])

    train_images = np.array(train_images)
    train_classes = np.array(train_classes)
    test_images = np.array(test_images)
    test_classes = np.array(test_classes)

    idx = np.random.permutation(len(train_images))
    train_images, train_classes = train_images[idx], train_classes[idx]

    idx = np.random.permutation(len(test_images))
    test_images, test_classes = test_images[idx], test_classes[idx]

    return train_images, train_classes, test_images, test_classes


def export_model(input_node_names, output_node_name):
    freeze_graph.freeze_graph('out/' + MODEL_NAME + '.pbtxt', None, False,
                              'out/' + MODEL_NAME + '.chkp', output_node_name, "save/restore_all",
                              "save/Const:0", 'out/frozen_' + MODEL_NAME + '.pb', True, "")

    input_graph_def = tf.GraphDef()
    with tf.gfile.Open('out/frozen_' + MODEL_NAME + '.pb', "rb") as f:
        input_graph_def.ParseFromString(f.read())

    output_graph_def = optimize_for_inference_lib.optimize_for_inference(
        input_graph_def, input_node_names, [output_node_name],
        tf.float32.as_datatype_enum)

    with tf.gfile.FastGFile('out/opt_' + MODEL_NAME + '.pb', "wb") as f:
        f.write(output_graph_def.SerializeToString())

    print("graph saved!")


def model_input(input_node_name):
    x = tf.placeholder(tf.float32, shape=[None, 64 * 64], name=input_node_name)
    y = tf.placeholder(tf.int32, shape=[None])
    keep_prob1 = tf.placeholder(tf.float32, name='keep_prob1')
    keep_prob2 = tf.placeholder(tf.float32, name='keep_prob2')
    return x, y, keep_prob1, keep_prob2


def build_model(x, y, keep_prob1, keep_prob2, output_node_name):

    x_image = tf.reshape(x, [-1, 64, 64, 1])
    # 64*64*1

    # Convolutional Layer #1 and Pooling Layer #1
    conv1_1 = tf.layers.conv2d(x_image, 64, 3, 1, 'same', activation=tf.nn.relu)
    conv1_2 = tf.layers.conv2d(conv1_1, 64, 3, 1, 'same', activation=tf.nn.relu)
    # 64*64*64
    pool1 = tf.layers.max_pooling2d(conv1_2, 2, 2, 'same')
    # 32*32*64
    dropout1 = tf.nn.dropout(pool1, keep_prob1)

    # Convolutional Layer #2 and Pooling Layer #2
    conv2_1 = tf.layers.conv2d(dropout1, 128, 3, 1, 'same', activation=tf.nn.relu)
    conv2_2 = tf.layers.conv2d(conv2_1, 128, 3, 1, 'same', activation=tf.nn.relu)
    # 32*32*128
    pool2 = tf.layers.max_pooling2d(conv2_2, 2, 2, 'same')
    # 16*16*128
    dropout2 = tf.nn.dropout(pool2, keep_prob1)

    # Convolutional Layer #3 and Pooling Layer #3
    conv3_1 = tf.layers.conv2d(dropout2, 256, 3, 1, 'same', activation=tf.nn.relu)
    conv3_2 = tf.layers.conv2d(conv3_1, 256, 3, 1, 'same', activation=tf.nn.relu)
    conv3_3 = tf.layers.conv2d(conv3_2, 256, 3, 1, 'same', activation=tf.nn.relu)
    # 16*16*256
    pool3 = tf.layers.max_pooling2d(conv3_3, 2, 2, 'same')
    # 8*8*256
    dropout3 = tf.nn.dropout(pool3, keep_prob1)

    # Convolutional Layer #4 and Pooling Layer #4
    conv4_1 = tf.layers.conv2d(dropout3, 256, 3, 1, 'same', activation=tf.nn.relu)
    conv4_2 = tf.layers.conv2d(conv4_1, 256, 3, 1, 'same', activation=tf.nn.relu)
    conv4_3 = tf.layers.conv2d(conv4_2, 256, 3, 1, 'same', activation=tf.nn.relu)
    # 8*8*256
    pool4 = tf.layers.max_pooling2d(conv4_3, 2, 2, 'same')
    # 4*4*256
    dropout4 = tf.nn.dropout(pool4, keep_prob1)

    # FC Layers
    flatten = tf.contrib.layers.flatten(dropout4)
    FC1 = tf.layers.dense(flatten, 1024, activation=tf.nn.relu)
    dropout5 = tf.nn.dropout(FC1, keep_prob2)
    FC2 = tf.layers.dense(dropout5, 1024, activation=tf.nn.relu)
    dropout6 = tf.nn.dropout(FC2, keep_prob2)

    logits = tf.layers.dense(dropout6, 8, activation=tf.nn.relu)
    outputs = tf.nn.softmax(logits, name=output_node_name)

    loss = tf.reduce_mean(
        tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

    # accuracy
    correct_prediction = tf.equal(tf.argmax(outputs, 1), tf.cast(y, tf.int64))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    tf.summary.scalar("loss", loss)
    tf.summary.scalar("accuracy", accuracy)
    merged_summary_op = tf.summary.merge_all()

    return train_step, loss, accuracy, merged_summary_op, outputs


def train(x, y, train_step, loss, accuracy,
          merged_summary_op, saver, keep_prob1, keep_prob2):
    print("training start...")

    init_op = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init_op)
        #saver.restore(sess, "./out/EmotionDetectionVGG_ferplus_8classes_100_with_filter.chkp")
        tf.train.write_graph(sess.graph_def, 'out',
                             MODEL_NAME + '.pbtxt', True)

        summary_writer = tf.summary.FileWriter('logs/',
                                               graph=tf.get_default_graph())

        lastindex = 0
        NUM_STEPS = int(trian_classes.size * NUM_EPOCHS / BATCH_SIZE)
        print("-------------trian-------------size")
        print(trian_classes.size)
        print("-------------test-------------size")
        print(test_classes.size)
        for step in range(NUM_STEPS):
            finalindex = lastindex + BATCH_SIZE
            end = False
            if finalindex > np.size(train_images, axis=0):
                finalindex = np.size(train_images, axis=0)
                end = True
                if finalindex == lastindex:
                    lastindex = 0
                    continue
            x_batch = np.take(train_images, range(lastindex, finalindex), axis=0)
            y_batch = np.take(trian_classes, range(lastindex, finalindex), axis=0)

            if end:
                lastindex = 0
            else:
                lastindex = finalindex

            if step % 5 == 0:
                train_accuracy = accuracy.eval(feed_dict={
                    x: x_batch, y: y_batch, keep_prob1: 1, keep_prob2: 1})
                print('step %d, training accuracy %f' % (step, train_accuracy))
            _, summary, loss_ = sess.run([train_step, merged_summary_op, loss],
                                         feed_dict={x: x_batch, y: y_batch, keep_prob1: 0.25, keep_prob2: 0.5})
            # summary_writer.add_summary(summary, step)
            print('step %d, LOSS %f' % (step, loss_))

        loop = True
        lastindex = 0
        acc = 0
        nr = 0
        while loop:
            finalindex = lastindex + BATCH_SIZE
            if finalindex > np.size(test_images, axis=0):
                finalindex = np.size(test_images, axis=0)
                loop = False
                if finalindex == lastindex:
                    lastindex = 0
                    continue
            x_batch = np.take(test_images, range(lastindex, finalindex), axis=0)
            y_batch = np.take(test_classes, range(lastindex, finalindex), axis=0)

            test_accuracy = accuracy.eval(feed_dict={x: x_batch,
                                                     y: y_batch,
                                                     keep_prob1: 1,
                                                     keep_prob2: 1})
            acc = acc + test_accuracy
            nr = nr + 1
            lastindex = finalindex

        print('TEST accuracy %f' % (acc/nr))
        saver.save(sess, 'out/' + MODEL_NAME + '.chkp')

    print("training finished!")


def main():
    input_node_name = 'input'
    output_node_name = 'output'

    print('Builing model...')
    x, y, keep_prob1, keep_prob2 = model_input(input_node_name)

    train_step, loss, accuracy, merged_summary_op, outputs = build_model(x, y, keep_prob1, keep_prob2, output_node_name)
    saver = tf.train.Saver()

    print('Start training...')
    train(x, y, train_step, loss, accuracy,
          merged_summary_op, saver, keep_prob1, keep_prob2)

    export_model([input_node_name], output_node_name)


train_images, trian_classes, test_images, test_classes = load_data('.\\FERPlus\\FER2013Train', '.\\FERPlus\\FER2013Test')
main()
