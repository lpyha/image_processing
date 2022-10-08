import sys

import cv2

VIDEO_PATH = 0
WINDOW_NAME = "frame"

def init_video():
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("cant open video")
        sys.exit()
    return cap

def get_frame_binary(gray): 
    ret, frame_binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    return frame_binary

def get_canny_edge_detection(gray):
    edges = cv2.Canny(gray, 100, 200)
    return edges

if __name__ == '__main__':
    cap = init_video()
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = get_canny_edge_detection(gray)
        frame_binary = get_frame_binary(gray)
        cv2.imshow(f"{WINDOW_NAME}", frame_binary)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
