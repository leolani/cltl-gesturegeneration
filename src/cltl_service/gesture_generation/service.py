import logging
from typing import List

from cltl.combot.infra.config import ConfigurationManager
from cltl.combot.infra.event import Event, EventBus
from cltl.combot.infra.resource import ResourceManager
from cltl.combot.infra.topic_worker import TopicWorker

from cltl.gesture_generation.api import Gesturer

logger = logging.getLogger(__name__)

CONTENT_TYPE_SEPARATOR = ';'


class GestureGenerationService:
    @classmethod
    def from_config(cls, gesturer: Gesturer, event_bus: EventBus, resource_manager: ResourceManager,
                    config_manager: ConfigurationManager):
        config = config_manager.get_config("cltl.gesture_generation")

        return cls(config.get("topic_input"), config.get("topic_output"), gesturer, event_bus, resource_manager)

    def __init__(self, input_topic: str, output_topic: str, gesturer: Gesturer,
                 event_bus: EventBus, resource_manager: ResourceManager):
        self._gesturer = gesturer

        self._event_bus = event_bus
        self._resource_manager = resource_manager

        self._input_topic = input_topic
        self._output_topic = output_topic

        self._topic_worker = None

    @property
    def app(self):
        return None

    def start(self, timeout=30):
        self._topic_worker = TopicWorker([self._input_topic], self._event_bus, provides=[self._output_topic],
                                         resource_manager=self._resource_manager, processor=self._process,
                                         name=self.__class__.__name__)
        self._topic_worker.start().wait()

    def stop(self):
        if not self._topic_worker:
            pass

        self._topic_worker.stop()
        self._topic_worker.await_stop()
        self._topic_worker = None

    def _process(self, event: Event):
        response = self._gesturer.generate_gesture(event.payload)

        if response:
            # TODO: transform brain responses into proper EMISSOR annotations (what to do about thoughts?)
            self._event_bus.publish(self._output_topic, Event.for_payload(response))
