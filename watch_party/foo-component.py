from jivago.lang.runnable import Runnable
from jivago.scheduling.annotations import Scheduled, Duration
from jivago.inject.annotation import Component


@Scheduled(every=Duration.SECOND)
@Component
class Foo(Runnable):

    def run(self):
        print("hello!")
