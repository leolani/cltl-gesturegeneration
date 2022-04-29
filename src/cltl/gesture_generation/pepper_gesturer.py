from cltl.gesture_generation.api import Gesturer


class PepperGesturer(Gesturer):

    def __init__(self):
        """
        Create a gesture for the Pepper robot based on an incoming emotion
        The complete list of readily available gestures are available at:
        http://doc.aldebaran.com/2-5/naoqi/motion/alanimationplayer-advanced.html#animationplayer-list-behaviors-pepper

        Parameters
        ----------
        """

        super(Gesturer, self).__init__()

    def generate_gesture(self, emotion):
        # TODO: Mark magic!
        gesture = None

        return gesture
