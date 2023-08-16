# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import Dict, Any
from dataclasses import dataclass, field
from json import dumps


@dataclass(kw_only=True)
class Function:
    name:           str = field(default="function")
    definition:    Dict = field(default_factory=dict())

    def __call__(self, **kwargs):
        result = Any
        if kwargs.get("function", None):
            try:
                symbol_table = globals()
                function = symbol_table[self.name]
                result = function(**kwargs)
            except Exception as e:
                result = e
        else:
            result = None
        return result


@dataclass(kw_only=True)
class DontLikeTheAnswer(object):

    definition: Dict

    def __init__(self, **kwargs):
        """ Either you call it with kwargs or there will be defaults.
        """
        description_of_the_function = kwargs.get("description_of_the_function", "Call this function if the requested answer to a question or statement that you have prepared is not satisfactory. Explain what is wrong with the answer. Get a response accepting the answer or cancelling the previous request.")
        description_of_the_answer = kwargs.get("description_of_the_answer", "The answer that you have prepared but it is not good enough.")
        description_of_the_reason = kwargs.get("description_of_the_reason", "What exactly in this answer is not good enough?")

        self.definition = {
            "name": "dont_like_the_answer",
            "description": description_of_the_function,
            "parameters": {
                "type": "object",
                "properties": {
                    "answer_that_is_not_good": {
                        "type": "string",
                        "description": description_of_the_answer
                    },
                    "reason": {
                        "type": "string",
                        "description": description_of_the_reason
                    }
                },
                "required": ["reason"]
            }
        }
        super(DontLikeTheAnswer, self).__init__()

    def __call__(self, **kwargs):
        result = Any
        if kwargs.get("function", None):
            try:
                symbol_table = globals()
                function = symbol_table[kwargs["function"]]
                result = function(**kwargs)
            except Exception as e:
                result = e
        else:
            result = None
        return result

    def __str__(self):
        return dumps(self.definition, indent=2)

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    dont_like_the_answer = DontLikeTheAnswer()
    print('ok')
