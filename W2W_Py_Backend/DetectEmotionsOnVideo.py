from copy import deepcopy

import cv2
import numpy as np
import pafy

from TensorflowEmotionDetector import TensorflowEmotionDector
from TensorflowFaceDetector import TensorflowFaceDetector

PATH_TO_FACE_DETECTION = './models/face_detection_model_41514.pb'
PATH_TO_EMOTION_DETECTION = './models/opt_EmotionDetectionVGG_ferplus_8classes_100_with_filter.pb'

emotionDetector = TensorflowEmotionDector(PATH_TO_EMOTION_DETECTION)
faceDetector = TensorflowFaceDetector(PATH_TO_FACE_DETECTION)


class DetectEmotionsOnVideo:

    @staticmethod
    def start_video(url):
        vpafy = pafy.new(url)
        play = vpafy.getbest(preftype="webm")
        cap = cv2.VideoCapture(play.url)

        all_detected_emotions = []
        while True:
            ret, frame = cap.read()
            if frame is not None:

                image_used_for_preview, faces_coordinates = faceDetector.run(deepcopy(frame))
                emotions = emotionDetector.run(frame, faces_coordinates)

                if len(emotions) != 0:
                    all_detected_emotions.append(emotions)

                cv2.imshow('frame', image_used_for_preview)
                if cv2.waitKey(22) & 0xFF == ord('q'):
                    break
            else:
                break

        result = np.zeros(8)
        for emotion in all_detected_emotions:
            arr = np.array(emotion)
            arr = np.squeeze(arr)
            best_3_values = np.argsort(-arr)[:3]
            w = 3
            for index in best_3_values:
                result[index] = result[index] + w
                w = w - 1

        total = 5 * len(all_detected_emotions)
        result_distribution = []
        for r in result:
            x = r * 100 / total
            result_distribution.append(x)

        for index, proc in enumerate(result_distribution):
            print(str(emotionDetector.emotion_table[index] + " - " + str(proc) + " %"))

        cap.release()
        cv2.destroyAllWindows()
