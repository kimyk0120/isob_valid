import sys
import cv2
import matplotlib.pyplot as plt
import json


def start(image_path, image_number, json_path, output_path):
    print("====================================")
    print("Image path: ", image_path)
    print("Image number: ", image_number)
    print("Json path: ", json_path)
    print("Output path: ", output_path)
    print("====================================")

    # read image
    image = cv2.imread(image_path)

    # rotate image 90 degree
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # read json file from json path
    with open(json_path) as f:
        data = f.read()
        json_data = json.loads(data)
        keypoints_data = json_data[image_number]
        keypoints = keypoints_data['keyPoints']

    keypoints_cnt = 0

    # draw key points on image
    for i in range(0, len(keypoints), 4):
        x = float(keypoints[i])
        y = float(keypoints[i + 1])
        cls = int(keypoints[i + 2])
        conf = keypoints[i + 3]

        x = x * image.shape[1]
        y = y * image.shape[0]

        print("X: ", x, end=" / ")
        print("Y: ", y, end=" / ")
        print("Class: ", cls, end=" / ")
        print("Confidence: ", conf)

        keypoints_cnt += 1

        # draw circle on image
        cv2.circle(image, (int(x), int(y)), radius=7, color=(0, 0, 255), thickness=-1)

    print("\nKey points count: ", keypoints_cnt)

    # TODO draw lines between key points
    



    cv2.imwrite(output_path + 'modified_image.jpg', image)


if __name__ == '__main__':
    # get command line arguments
    args = sys.argv

    # image path
    image_path = "./data/35/image1.jpg"

    # image number (front 0, left 1, right 2, back 3)
    image_number = int(image_path.split('/')[-1].split('.')[0][-1])

    # json path
    json_path = 'data/35/key_points.json'

    # output path
    output_path = './output/'

    start(image_path, image_number, json_path, output_path)
