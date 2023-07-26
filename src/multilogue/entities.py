# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


class Entity(object):
    """ Human or other entity, participating in the multilogue """

    name:           str = ''
    role:           str = ''
    instructions:   str = ''
    functions:      str = ''
    python_code:    str = ''

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Entity, self).__init__()

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def answer(self, *args, **kwargs):
        """ Answer the last statement """
        pass

    def listen(self, *args, **kwargs):
        """ Listen to the last statement """
        pass

    def __repr__(self, *args, **kwargs):
        return f"""     Entity:
            instructions - {self.instructions},
            functions - {self.functions},
            python_code - {self.python_code},
            name - {self.name},
            role - {self.role},
            """
