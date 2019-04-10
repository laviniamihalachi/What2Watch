import numpy as np
import cv2
import pafy


def start_video(url):
    vpafy = pafy.new(url)
    play = vpafy.getbest(preftype="webm")
    cap = cv2.VideoCapture(play.url)

    while True:
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow('frame', frame)
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
