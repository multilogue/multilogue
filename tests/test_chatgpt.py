# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from unittest import TestCase
from src.multilogue.utilities.chatgpt import (answer,
                                              fill_in,
                                              complete)


class TestChatGPT(TestCase):
    prompt1 = 'Say this is a test.'
    kwa = {
        "temperature": 0.5,
        "top_p": 0.95,
        "max_tokens": 30,
        "n": 3,
        "best_of": 4,
        "frequency_penalty": 2.0,
        "presence_penalty": 2.0
    }
    msgs = [
        {
            "role": "user",
            "content": prompt1
        }
    ]

    def test_answer(self):
        actual = answer(messages=self.msgs)
        self.fail()

    def test_fill_in(self):
        answers1 = fill_in(prompt=self.prompt1,
                           suffix='',
                           **self.kwa)
        self.fail()

    def text_complete(self):
        answers2 = complete(prompt=self.prompt1,
                            **self.kwa)
        self.fail()
