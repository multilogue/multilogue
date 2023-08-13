# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict


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
            print(f"{message['role']}: {message['content']}\n\n")

