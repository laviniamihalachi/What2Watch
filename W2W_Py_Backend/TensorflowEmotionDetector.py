import time

import cv2
import numpy as np
import skimage
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import tensorflow as tf
from skimage.color import rgb2gray


class TensorflowEmotionDector(object):
    emotion_table = {0: 'neutral',
                     1: 'happiness',
                     2: 'surprise',
                     3: 'sadness',
                     4: 'anger',
                     5: 'disgust',
                     6: 'fear',
                     7: 'contempt'}

    def __init__(self, PATH):
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        with self.detection_graph.as_default():
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.Session(graph=self.detection_graph, config=config)
            self.windowNotSet = True

    def to_grayscale(self, images):
        grayScaleImages = rgb2gray(images)
        grayScaleImages = np.array(grayScaleImages)
        return grayScaleImages

    def run(self, image, faces_coordinates):
        image_tensor = self.detection_graph.get_tensor_by_name('input:0')
        prediction = self.detection_graph.get_tensor_by_name('output:0')
        keep_prob1 = self.detection_graph.get_tensor_by_name('keep_prob1:0')
        keep_prob2 = self.detection_graph.get_tensor_by_name('keep_prob2:0')
        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        emotions = []
        for (x1, y1, x2, y2) in faces_coordinates:
            face_image = image_np[y1:y2, x1:x2, :]
            resized_image = skimage.transform.resize(face_image, (64, 64))
            data_image = self.to_grayscale(resized_image)
            data_image = data_image.flatten()

            start_time = time.time()
            rez = self.sess.run([prediction],
                                feed_dict={image_tensor: data_image, keep_prob1: 1, keep_prob2: 1})
            elapsed_time = time.time() - start_time
            #print('inference time cost for emotion detection: {}'.format(elapsed_time))

            # debug
            #if str(self.emotion_table[np.argmax(np.squeeze(rez))]) != "neutral":
            #    plt.imshow(face_image)
            #    plt.xlabel(str(self.emotion_table[np.argmax(np.squeeze(rez))]))
            #    plt.show()

            np.squeeze(rez)
            emotions.append(rez)

        return emotions
