# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


class Protagonist(Entity, Position):
    """ multilogue protagonist """

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'protagonist'
        self.thesis = kwargs['thesis']
        super(Protagonist, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"
