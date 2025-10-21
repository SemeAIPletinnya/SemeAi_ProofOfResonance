
"""Event bus facade. Generated 2025-10-21 22:57:30Z."""

class EventBus:
    subscribers: dict[str, list] = {}  # topic -> callbacks

    @classmethod
    def subscribe(cls, topic: str, fn) -> None:
        cls.subscribers.setdefault(topic, []).append(fn)

    @classmethod
    def publish(cls, topic: str, payload: dict) -> None:
        for fn in cls.subscribers.get(topic, []):
            fn(payload)
