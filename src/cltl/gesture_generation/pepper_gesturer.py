from cltl.gesture_generation.api import Gesturer
import random

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
        """
        Matches the emotion to a gesture.
        The current emotions supported are:
            "neutral"
            "joy"
            "surprise"
            "anger"
            "sadness"
            "disgust"
            "fear"
        """
        gesture_dic = {
            "neutral" : ["animations/Stand/Gestures/Explain_1"]
            "joy" : ["animations/Stand/Emotions/Positive/Happy_4"]
            "surprise" : ["animations/Stand/Emotions/Positive/Hysterical_1", "animations/Stand/Gestures/Excited_1"]
            "anger" : ["animations/Stand//Gestures/CalmDown_" + str(x) for x in [1, 5, 6]]
            "sadness" : ["animations/Stand/Gestures/Desperate_" + str(x) for x in [1, 2, 4, 5]]
            "disgust" : ["animations/Stand/Emotions/Negative/Bored_1"]
            "fear" : ["animations/Stand//Gestures/CalmDown_" + str(x) for x in [1, 5, 6]]
        }
        gesture = random.choice(gesture_dic[emotion])

        return gesture
