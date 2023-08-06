# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from .chatgpt import answer, fill_in, complete
from .githublog import (creupdate_repo,
                        creupdate_file)

__all__ = [
    "answer",
    "fill_in",
    "complete",
    'creupdate_repo',
    'creupdate_file'
]