import cv2


class Validator:

    def __init__(self, keypoints=None, image=None):
        self.xy_list = []
        self.keypoints = keypoints
        self.keypoints_cnt = 0
        self.image = image
        self.set_xy(degug=True)

    def set_xy(self, degug=False):
        for i in range(0, len(self.keypoints), 4):
            x = float(self.keypoints[i])
            y = float(self.keypoints[i + 1])
            cls = int(self.keypoints[i + 2])
            conf = self.keypoints[i + 3]

            x = x * self.image.shape[1]
            y = y * self.image.shape[0]

            # set into xy_list
            self.xy_list.append([x, y])

            if degug:
                print("X: ", x, end=" / ")
                print("Y: ", y, end=" / ")
                print("Class: ", cls, end=" / ")
                print("Confidence: ", conf)

            self.keypoints_cnt += 1

            print("\nTotal Key-points count: ", self.keypoints_cnt)

    def draw_points(self):
        for xy in self.xy_list:
            x = xy[0]
            y = xy[1]
            cv2.circle(self.image, (int(x), int(y)), radius=7, color=(0, 0, 255), thickness=-1)

    '''
        pose landmark index
        0 PoseLandmark.NOSE,
        1 PoseLandmark.LEFT_EYE,
        2 PoseLandmark.RIGHT_EYE,
        3 PoseLandmark.LEFT_EAR,
        4 PoseLandmark.RIGHT_EAR,
        5 PoseLandmark.LEFT_SHOULDER,
        6 PoseLandmark.RIGHT_SHOULDER,
        7 PoseLandmark.LEFT_ELBOW,
        8 PoseLandmark.RIGHT_ELBOW,
        9 PoseLandmark.LEFT_WRIST,
        10 PoseLandmark.RIGHT_WRIST,
        11 PoseLandmark.LEFT_HIP,
        12 PoseLandmark.RIGHT_HIP,
        13 PoseLandmark.LEFT_KNEE,
        14 PoseLandmark.RIGHT_KNEE,
        15 PoseLandmark.LEFT_ANKLE,
        16 PoseLandmark.RIGHT_ANKLE
    '''

    def draw_hlines(self):
        for xy in self.xy_list:
            x = xy[0]
            y = xy[1]

