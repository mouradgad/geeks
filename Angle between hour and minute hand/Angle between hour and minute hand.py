
class Solution:
    def getAngle(self, H , M):
        # code here
        angle = (abs( 0.5 * (60*H-11*M)))

        if angle > 180:

            return int(360-angle)

        else:

            return int(angle)