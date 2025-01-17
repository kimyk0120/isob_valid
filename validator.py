import cv2
import kp_analyzer as kp

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


class Validator:

    def __init__(self, keypoints=None, image=None, output_path=None, json_data=None):
        self.xy_list = []
        self.keypoints = keypoints
        self.json_data = json_data
        self.keypoints_cnt = 0
        self.image = image
        self.output_path = output_path
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
                print(int(i / 4), "X: ", x, end=" / ")
                print("Y: ", y, end=" / ")
                print("Class: ", cls, end=" / ")
                print("Confidence: ", conf)

            self.keypoints_cnt += 1

        print("Total Key-points count: ", self.keypoints_cnt)

    def valid(self):

        # draw lines
        self.draw_hlines()

        # draw dots
        for xy in self.xy_list:
            x = xy[0]
            y = xy[1]
            cv2.circle(self.image, (int(x), int(y)), radius=5, color=(0, 0, 255), thickness=-1)

        # calculate degrees
        self.calculate_degrees(debug=True)

        # save image
        cv2.imwrite(self.output_path + 'output_image.jpg', self.image)
        # print("Output image saved successfully!")

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

    def calculate_degrees(self, debug=False):

        kp_analyzer = kp.BodyShapeAnalyzer(self.json_data)

        turtle_neck_anal_angle = kp_analyzer.turtle_neck_anal_angle
        shoulder_balance_anal_angle = kp_analyzer.shoulder_balance_anal_angle
        l_pelvis_anal_angle, r_pelvis_anal_angle = kp_analyzer.l_pelvis_anal_angle, kp_analyzer.r_pelvis_anal_angle
        l_ox_leg_anal_angle, r_ox_leg_anal_angle = kp_analyzer.l_ox_leg_anal_angle, kp_analyzer.r_ox_leg_anal_angle

        if debug:
            print("========================================"*2)
            print("Turtle Neck Angle: ", turtle_neck_anal_angle)
            print("Shoulder Balance Angle: ", shoulder_balance_anal_angle)
            print("Left Pelvis Angle: ", l_pelvis_anal_angle)
            print("Right Pelvis Angle: ", r_pelvis_anal_angle)
            print("Left Ox Leg Angle: ", l_ox_leg_anal_angle)
            print("Right Ox Leg Angle: ", r_ox_leg_anal_angle)
            print("========================================"*2)

        # draw on image
        start_y = 30
        cv2.putText(self.image, str("Turtle Neck Angle: " + "{:.2f}".format(turtle_neck_anal_angle)), (10, start_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(self.image, str("Shoulder Balance Angle: " + "{:.2f}".format(shoulder_balance_anal_angle)), (10, start_y*2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(self.image, str("Left Pelvis Angle: " + "{:.2f}".format(l_pelvis_anal_angle)), (10, start_y*3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(self.image, str("Right Pelvis Angle: " + "{:.2f}".format(r_pelvis_anal_angle)), (10, start_y*4), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(self.image, str("Left Ox Leg Angle: " + "{:.2f}".format(l_ox_leg_anal_angle)), (10, start_y*5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(self.image, str("Right Ox Leg Angle: " + "{:.2f}".format(r_ox_leg_anal_angle)), (10, start_y*6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

