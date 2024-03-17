# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


class Attendee():
    """ multilogue attendee """
    name: str = ''
    role: str = ''

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'attendee'
        self.thesis = kwargs['thesis']
        super(Attendee, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"
