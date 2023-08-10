# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict


class Phrase(object):
    """ A phrase in a conversation """
    name: str
    whole_phrase: str

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Phrase, self).__init__()


class Thread(Phrase):
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

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    def display_conversation(self, detailed=False):
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
            "function": "magenta",
        }
        for message in self.conversation_history:
            print(
                colored(
                    f"{message['role']}: {message['content']}\n\n",
                    role_to_color[message["role"]],
                )
            )

