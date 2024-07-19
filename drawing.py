import cv2


def draw_points(image, keypoints, degug=False):

    keypoints_cnt = 0

    for i in range(0, len(keypoints), 4):
        x = float(keypoints[i])
        y = float(keypoints[i + 1])
        cls = int(keypoints[i + 2])
        conf = keypoints[i + 3]

        x = x * image.shape[1]
        y = y * image.shape[0]

        if degug:
            print("X: ", x, end=" / ")
            print("Y: ", y, end=" / ")
            print("Class: ", cls, end=" / ")
            print("Confidence: ", conf)

        keypoints_cnt += 1

        # draw circle on image
        cv2.circle(image, (int(x), int(y)), radius=7, color=(0, 0, 255), thickness=-1)

    print("\nDrawn Key-points count: ", keypoints_cnt)

