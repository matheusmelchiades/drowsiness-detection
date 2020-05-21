from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48
COUNTER = 0
FRAME_SIZE = 600


def size_closed_eye(eye=[]):
    p1, p2, p3, p4, p5, p6 = eye

    distance_a = dist.euclidean(p2, p6)
    distance_b = dist.euclidean(p3, p5)
    distance_c = dist.euclidean(p1, p4)

    ear = (distance_a + distance_b) / (2.0 * distance_c)

    return ear


def log(log_type='INFO', content=''):
    print(f'### [{log_type}] - {content}')


if __name__ == "__main__":

    log(content="loading facial landmark predictor...")

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('face_landmarks.dat')

    log(content="facial landmark predictor loaded with success...")

    (left_start, left_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (right_start, right_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    log(content="starting video stream thread...")

    vs = VideoStream().start()
    time.sleep(1.0)

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=FRAME_SIZE)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            left_eye = shape[left_start:left_end]
            right_eye = shape[right_start:right_end]

            left_ear = size_closed_eye(left_eye)
            right_ear = size_closed_eye(right_eye)

            ear = (left_ear + right_ear) / 2.0

            left_eye_hull = cv2.convexHull(left_eye)
            right_eye_hull = cv2.convexHull(right_eye)

            cv2.drawContours(frame, [left_eye_hull], -1, (116, 26, 172), 1)
            cv2.drawContours(frame, [right_eye_hull], -1, (116, 26, 172), 1)

            if ear < EYE_AR_THRESH:
                COUNTER += 1

                if COUNTER >= EYE_AR_CONSEC_FRAMES:

                    cv2.putText(frame, "DROWSINESS DETECTED!", (10, 30),
                                cv2.FONT_HERSHEY_PLAIN, 1.9, (0, 255, 0), 2)

            else:
                COUNTER = 0

            cv2.putText(frame, "OPEN: {:.2f}".format(ear), (30, 400),
                        cv2.FONT_HERSHEY_PLAIN, 1.9, (255, 0, 0), 2)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    vs.stop()
