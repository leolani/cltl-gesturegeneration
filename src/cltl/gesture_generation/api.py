from cltl.gesture_generation import logger


class Gesturer(object):

    def __init__(self):
        # type: () -> None
        """
        Generate a gesture an agent

        Parameters
        ----------
        """

        self._log = logger.getChild(self.__class__.__name__)
        self._log.info("Booted")

    def generate_gesture(self, emotion):
        raise NotImplementedError()
