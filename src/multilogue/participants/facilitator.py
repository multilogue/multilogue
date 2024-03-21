# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


class Facilitator():
    """ Multilogue facilitator

        Entity.  # from multilogue
            name: str
            role: str  # role in the multilogue, not an API role
            instructions: str
            functions: List
            python_code: str
        Position.  # from multilectic
            thesis: str
            antithesis: str
            facts: List
            presuppositions: List[str]
            conversation: List[Dict]
    """
    utterance: str = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.utterance = "I am a facilitator of this conversation."
        super(Facilitator, self).__init__()

    def suggest(self):
        return self.utterance

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def guide(self, *args, **kwargs):
        guidance = 'You decide it yourself.'
        return guidance

    def __repr__(self):
        return f"{self.name}, {self.role}"

