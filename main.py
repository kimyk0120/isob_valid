import sys
import cv2
import json
import validator as v


def start(image_path, image_number, json_path, output_path):
    print("========================================"*2)
    print("Image path: ", image_path)
    print("Image number: ", image_number)
    print("Json path: ", json_path)
    print("Output path: ", output_path)
    print("========================================"*2)

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

    # validation process
    #  - draw key points and lines on image, calculate degrees and save image
    v.Validator(image=image, keypoints=keypoints, output_path=output_path, json_data=json_data).valid()


if __name__ == '__main__':
    # get command line arguments
    # - image path, image number (front 0, left 1, right 2, back 3), json path, output path
    args = sys.argv
    if len(args) >= 4:
        image_path, image_number, json_path, output_path = args[1], int(args[2]), args[3], args[4]  # argv[0] is main.py
    else:
        image_path = "./data/35/image1.jpg"
        image_number = int(image_path.split('/')[-1].split('.')[0][-1])
        json_path = 'data/35/key_points.json'
        output_path = './output/'

    start(image_path, image_number, json_path, output_path)
