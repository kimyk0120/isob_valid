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
                print(int(i/4), "X: ", x, end=" / ")
                print("Y: ", y, end=" / ")
                print("Class: ", cls, end=" / ")
                print("Confidence: ", conf)

            self.keypoints_cnt += 1

        print("\nTotal Key-points count: ", self.keypoints_cnt)

    def draw_points(self):

        self.draw_hlines()

        for xy in self.xy_list:
            x = xy[0]
            y = xy[1]
            cv2.circle(self.image, (int(x), int(y)), radius=5, color=(0, 0, 255), thickness=-1)

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

        nose_x, nose_y = self.xy_list[0][0], self.xy_list[0][1]
        leye_x, leye_y = self.xy_list[1][0], self.xy_list[1][1]
        reye_x, reye_y = self.xy_list[2][0], self.xy_list[2][1]
        lear_x, lear_y = self.xy_list[3][0], self.xy_list[3][1]
        rear_x, rear_y = self.xy_list[4][0], self.xy_list[4][1]
        lshoulder_x, lshoulder_y = self.xy_list[5][0], self.xy_list[5][1]
        rshoulder_x, rshoulder_y = self.xy_list[6][0], self.xy_list[6][1]
        lelbow_x, lelbow_y = self.xy_list[7][0], self.xy_list[7][1]
        relbow_x, relbow_y = self.xy_list[8][0], self.xy_list[8][1]
        lwrist_x, lwrist_y = self.xy_list[9][0], self.xy_list[9][1]
        rwrist_x, rwrist_y = self.xy_list[10][0], self.xy_list[10][1]
        lhip_x, lhip_y = self.xy_list[11][0], self.xy_list[11][1]
        rhip_x, rhip_y = self.xy_list[12][0], self.xy_list[12][1]
        lknee_x, lknee_y = self.xy_list[13][0], self.xy_list[13][1]
        rknee_x, rknee_y = self.xy_list[14][0], self.xy_list[14][1]
        lankle_x, lankle_y = self.xy_list[15][0], self.xy_list[15][1]
        rankle_x, rankle_y = self.xy_list[16][0], self.xy_list[16][1]

        cv2.line(self.image, (int(leye_x), int(leye_y)), (int(nose_x), int(nose_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(reye_x), int(reye_y)), (int(nose_x), int(nose_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(leye_x), int(leye_y)), (int(lear_x), int(lear_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(reye_x), int(reye_y)), (int(rear_x), int(rear_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(lshoulder_x), int(lshoulder_y)), (int(rshoulder_x), int(rshoulder_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(lshoulder_x), int(lshoulder_y)), (int(lelbow_x), int(lelbow_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(rshoulder_x), int(rshoulder_y)), (int(relbow_x), int(relbow_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(lelbow_x), int(lelbow_y)), (int(lwrist_x), int(lwrist_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(relbow_x), int(relbow_y)), (int(rwrist_x), int(rwrist_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(lshoulder_x), int(lshoulder_y)), (int(lhip_x), int(lhip_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(rshoulder_x), int(rshoulder_y)), (int(rhip_x), int(rhip_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(lhip_x), int(lhip_y)), (int(lknee_x), int(lknee_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(rhip_x), int(rhip_y)), (int(rknee_x), int(rknee_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(lknee_x), int(lknee_y)), (int(lankle_x), int(lankle_y)), (0, 255, 0), 3)
        cv2.line(self.image, (int(rknee_x), int(rknee_y)), (int(rankle_x), int(rankle_y)), (0, 255, 0), 3)

