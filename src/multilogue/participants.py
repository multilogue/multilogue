# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from json import loads, dumps
from multilectic import Position, Opinion
from .entities import Entity, Human


class Facilitator(Human):
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
        self.utterance = "I am a facilitator"
        super(Facilitator, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def guide(self, *args, **kwargs):
        guidance = 'You decide it yourself.'
        return guidance

    def __repr__(self):
        return f"{self.name}, {self.role}"


class Expert(Entity, Opinion):
    """ Expert on a subject

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
    competence: str = 'human nature'
    utterance: str = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.utterance = "I am an expert"
        super(Expert, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        content = kwargs.get('content', '')
        arguments = loads(kwargs.get('arguments', ''))
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"


class HumanExpert(Human):
    """ Expert on a subject"""
    competence: str             = 'human nature'  # expert in:
    level_of_competence: str    = 'hignest'  # high, medium, average, low
    utterance: str              = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.utterance = "I am an expert"
        super(HumanExpert, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        content = kwargs.get('content', '')
        arguments = loads(kwargs.get('arguments', ''))
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"


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


class Antagonist(Entity, Position):
    """ multilogue antagonist """

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'antagonist'
        self.thesis = kwargs['thesis']
        super(Antagonist, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"


class Interlocutor(Entity, Position):
    """ multilogue interlocutor """

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'interlocutor'
        self.thesis = kwargs['thesis']
        super(Interlocutor, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"
