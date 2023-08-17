# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict
from dataclasses import dataclass, field, asdict


@dataclass
class Message:
    role:       str = field(default="user")
    content:    str = field(default="This is a content of a message.")
    name:       str = field(default="")

    def to_dict(self):
        return asdict(self)


@dataclass
class SystemMessage:
    role:       str = field(default="system")
    content:    str = field(default="This is a system message.")

    def to_dict(self):
        return asdict(self)


class Sentence(object):
    """ A phrase in a conversation """
    name: str
    whole_phrase: str

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Sentence, self).__init__()


class Thread(Sentence):
    """ A thread in a conversation.
        A thread can be temporarily 'tabled' until it's declared
        to be ended.
    """
    thread_name: str
    thread_description: str
    beginning: Dict[str, str]
    ending: Dict[str, str]
    put_forward: bool = False

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Thread, self).__init__()


class Conversation(Thread):

    sequence: List

    def __init__(self):
        self.conversation_history = []
        super(Conversation, self).__init__()

    def add_message(self, **kwargs):
        if kwargs:
            message = Message(kwargs)
            self.conversation_history.append(message)
        else:
            pass

    def display_conversation(self, detailed=False):
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
            "function": "magenta",
        }
        for message in self.conversation_history:
            print(f"{message['role']}: {message['content']}\n\n")


if __name__ == "__main__":
    message = Message(content="noncontent", name="Alex")
    print(message.to_dict())