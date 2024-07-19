import sys
import cv2
import matplotlib.pyplot as plt
import json
import validator as v


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


    # extract x,y
    validator = v.Validator(image=image, keypoints=keypoints)

    # draw key points on image
    validator.draw_points()

    # TODO draw lines between key points
    validator.draw_hlines()

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
