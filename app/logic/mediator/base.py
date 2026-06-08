from dataclasses import dataclass


@dataclass(eq=False)
class Mediator:
    events_map: dict
    commands_map: dict
    queries_map: dict

    def register_event(self, event, event_handlers): ...

    def register_command(self, command, command_handlers): ...

    def register_query(self, query, query_handler): ...

    async def publish(self, events): ...

    async def handle_command(self, command): ...

    async def handle_query(seld, query): ...
