import time
import cv2
import numpy as np
import tensorflow as tf
from utils import visualization_utils_color as vis_util, label_map_util

PATH_TO_LABELS = './protos/face_label_map.pbtxt'
NUM_CLASSES = 2

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


class TensorflowFaceDetector(object):

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

    def run(self, image):
        [h, w] = image.shape[:2]
        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)

        image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
        scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')

        start_time = time.time()
        (boxes, scores, classes, num_detections) = self.sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})
        elapsed_time = time.time() - start_time
        #print('inference time cost: {}'.format(elapsed_time))

        boxes = boxes.reshape(100, 4)
        classes = classes.reshape(100)
        scores = scores.reshape(100)

        valid_faces_coordinates = []
        for idx, coordinates in enumerate(boxes):
            if scores[idx] > 0.6 and classes[idx] == 1:
                y1 = int(coordinates[0] * h)
                x1 = int(coordinates[1] * w)
                y2 = int(coordinates[2] * h)
                x2 = int(coordinates[3] * w)
                if y2 - y1 > x2 - x1:
                    dif = ((y2 - y1) - (x2 - x1)) / 2
                    x1 = int(x1 - dif)
                    if x1 < 0:
                        x1 = 0
                    x2 = int(x2 + dif)
                    if x2 > w:
                        x2 = w
                else:
                    dif = ((x2 - x1) - (y2 - y1)) / 2
                    y1 = int(y1 - dif)
                    if y1 < 0:
                        y1 = 0
                    y2 = int(y2 + dif)
                    if y2 > h:
                        y2 = h
                valid_faces_coordinates.append((x1, y1, x2, y2))

        # Visualization of the results of a detection.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=4)

        return image, valid_faces_coordinates
