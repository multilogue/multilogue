# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
import requests

api_key         = environ.get("OPENAI_API_KEY")
api_key_path    = environ.get("OPENAI_API_KEY_PATH")

organization    = environ.get("OPENAI_ORGANIZATION")
api_base        = environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
api_type        = environ.get("OPENAI_API_TYPE", "open_ai")
default_model   = environ.get("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo-0613")


def answer(messages, functions=None, function_call=None, model=default_model):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }
    json_data = {"model": model, "messages": messages}
    if functions is not None:
        json_data.update({"functions": functions})
    if function_call is not None:
        json_data.update({"function_call": function_call})
    try:
        response = requests.post(
            f"{api_base}/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
