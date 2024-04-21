# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from ..participants import Interlocutor


class Thread(Interlocutor):
    """
    A Thread is a perspective of the conversation from the point of view of a particular participant.

    It is a way to organize and structure the conversation. Thread mostly does renaming and reformatting of messages according to the logicas roles of the participants in the conversation. I first wanted to put this functionality on the Symposium level, but realized that it would be better to have it on the Participant level.
    """
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Thread, self).__init__()
