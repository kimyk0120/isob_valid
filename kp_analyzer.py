# pose landmark index
import math


class PoseLandmark:
    NOSE = 0
    LEFT_EYE = 1
    RIGHT_EYE = 2
    LEFT_EAR = 3
    RIGHT_EAR = 4
    LEFT_SHOULDER = 5
    RIGHT_SHOULDER = 6
    LEFT_ELBOW = 7
    RIGHT_ELBOW = 8
    LEFT_WRIST = 9
    RIGHT_WRIST = 10
    LEFT_HIP = 11
    RIGHT_HIP = 12
    LEFT_KNEE = 13
    RIGHT_KNEE = 14
    LEFT_ANKLE = 15
    RIGHT_ANKLE = 16


# pose landmark Unit List
# x, y, class, confidence

class CamType:
    FRONT = 0
    LEFT = 1
    RIGHT = 2
    BACK = 3


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def subtract(a, b):
        return Coordinate(a.x - b.x, a.y - b.y)

    @staticmethod
    def distance(a, b):
        dx = a.x - b.x
        dy = a.y - b.y
        return (dx ** 2 + dy ** 2) ** 0.5

    @staticmethod
    def dot(a, b):
        ddx = a.x * b.x
        ddy = a.y * b.y
        return Coordinate(ddx, ddy)


def _get_angle(a, b, c):
    AB = Coordinate.distance(a, b)
    BC = Coordinate.distance(b, c)
    CA = Coordinate.distance(c, a)
    cosB = ((AB ** 2 + BC ** 2 - CA ** 2) / (2 * AB * BC))
    return math.acos(cosB) * (180 / math.pi)


class BodyShapeAnalyzer:
    def __init__(self, key_points_list):
        self.key_points_list = key_points_list

        # 각 항목의 각도 산출 호출
        self.turtle_neck_anal_angle = self.check_turtle_neck()
        self.shoulder_balance_anal_angle = self.check_shoulder_balance()

        self.l_pelvis_anal_angle, self.r_pelvis_anal_angle = self.check_pelvis()
        self.l_ox_leg_anal_angle, self.r_ox_leg_anal_angle = self.check_ox_leg()

    def check_pelvis(self):
        front_key_points = next(kp for kp in self.key_points_list if int(kp['id']) == CamType.FRONT)['keyPoints']
        origin = Coordinate(0, 0)
        LEar = Coordinate(front_key_points[3 * 4], front_key_points[3 * 4 + 1])
        REar = Coordinate(front_key_points[4 * 4], front_key_points[4 * 4 + 1])
        LHip = Coordinate(front_key_points[11 * 4], front_key_points[11 * 4 + 1])
        RHip = Coordinate(front_key_points[12 * 4], front_key_points[12 * 4 + 1])

        std_line = Coordinate.subtract(REar, LEar)
        target_line = Coordinate.subtract(RHip, LHip)
        l_pelvis_angle = _get_angle(std_line, origin, target_line)

        std_line = Coordinate.subtract(LEar, REar)
        target_line = Coordinate.subtract(LHip, RHip)
        r_pelvis_angle = _get_angle(std_line, origin, target_line)

        return l_pelvis_angle, r_pelvis_angle

    def check_ox_leg(self):
        front_key_points = next(kp for kp in self.key_points_list if int(kp['id']) == CamType.FRONT)['keyPoints']
        LHip = Coordinate(front_key_points[11 * 4], front_key_points[11 * 4 + 1])
        LKnee = Coordinate(front_key_points[13 * 4], front_key_points[13 * 4 + 1])
        LAnkle = Coordinate(front_key_points[15 * 4], front_key_points[15 * 4 + 1])

        RHip = Coordinate(front_key_points[12 * 4], front_key_points[12 * 4 + 1])
        RKnee = Coordinate(front_key_points[14 * 4], front_key_points[14 * 4 + 1])
        RAnkle = Coordinate(front_key_points[16 * 4], front_key_points[16 * 4 + 1])

        l_angle = _get_angle(LHip, LKnee, LAnkle)
        r_angle = _get_angle(RHip, RKnee, RAnkle)

        return l_angle, r_angle

    def check_turtle_neck(self):
        left_key_points = next(kp for kp in self.key_points_list if int(kp['id']) == CamType.LEFT)['keyPoints']
        right_key_points = next(kp for kp in self.key_points_list if int(kp['id']) == CamType.RIGHT)['keyPoints']

        LEar = Coordinate(left_key_points[3 * 4], left_key_points[3 * 4 + 1])
        LShoulder = Coordinate(left_key_points[5 * 4], left_key_points[5 * 4 + 1])
        LAnkle = Coordinate(left_key_points[15 * 4], left_key_points[15 * 4 + 1])

        REar = Coordinate(right_key_points[4 * 4], right_key_points[4 * 4 + 1])
        RShoulder = Coordinate(right_key_points[6 * 4], right_key_points[6 * 4 + 1])
        RAnkle = Coordinate(right_key_points[16 * 4], right_key_points[16 * 4 + 1])

        l_angle = _get_angle(LEar, LShoulder, LAnkle)
        r_angle = _get_angle(REar, RShoulder, RAnkle)

        avg_angle = (l_angle + r_angle) / 2

        return avg_angle

    def check_shoulder_balance(self):
        front_key_points = next(kp for kp in self.key_points_list if int(kp['id']) == CamType.FRONT)['keyPoints']
        LEar = Coordinate(front_key_points[3 * 4], front_key_points[3 * 4 + 1])
        REar = Coordinate(front_key_points[4 * 4], front_key_points[4 * 4 + 1])
        LShoulder = Coordinate(front_key_points[5 * 4], front_key_points[5 * 4 + 1])
        RShoulder = Coordinate(front_key_points[6 * 4], front_key_points[6 * 4 + 1])

        std_line = Coordinate.subtract(LEar, REar)
        target_line = Coordinate.subtract(LShoulder, RShoulder)
        angle = _get_angle(std_line, Coordinate(0, 0), target_line)

        return angle
