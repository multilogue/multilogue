# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from multilogue.participants import Facilitator


class Conversation(Facilitator):
    """ Conversation class.
    Conversation is managed by a facilitator.
    The main function of the conversation is to arrange the individual threads and their records for participants, then combine them into a main protocol and
    record of the conversation.
    """
    facilitator = None
    issue = None

    def __init__(self, **kwargs):
        """Conversation can be initiated by a human or a machine."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        theme = {
            'issue': 'Can human nature be changed?',
        }
        super(Conversation, self).__init__(**theme)
        suggestion = self.suggest()


if __name__ == '__main__':
    kwargs = {
        'theme': 'Can human nature be changed?'
    }
    conv = Conversation(**kwargs)
    print(conv)