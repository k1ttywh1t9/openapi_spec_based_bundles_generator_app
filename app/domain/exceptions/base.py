from dataclasses import dataclass


@dataclass
class ApplicationException(Exception):
    @property
    def message(self):
        return "An application error occured"
