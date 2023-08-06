# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
import requests

api_key             = environ.get("OPENAI_API_KEY")
api_key_path        = environ.get("OPENAI_API_KEY_PATH")

organization        = environ.get("OPENAI_ORGANIZATION")
organization_id     = environ.get("OPENAI_ORGANIZATION_ID")
api_base            = environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
api_type            = environ.get("OPENAI_API_TYPE", "open_ai")
default_model       = environ.get("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo-0613")
completion_model    = environ.get("OPENAI_COMPLETION_MODEL",'text-davinci-003')

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key,
    "Organization": organization
}


def answer(messages,
           functions=None,
           function_call=None,
           model=default_model,
           **kwargs):

    """A simple requests call to ChatGPT.
        kwargs:
            temperature     = 0 to 1.0
            top_p           = 0.0 to 1.0
            n               = 1 to ...
            frequency_penalty = -2.0 to 2.0
            presence_penalty = -2.0 to 2.0
            max_tokens      = number of tokens
    """
    responses = []
    json_data = {"model": model, "messages": messages} | kwargs
    if functions is not None: json_data = json_data | {"functions": functions}
    if function_call is not None: json_data = json_data | {"function_call": function_call}
    try:
        response = requests.post(
            f"{api_base}/chat/completions",
            headers=headers,
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            for choice in response.json()['choices']:
                obj = choice.to_dict_recursive()
                responses.append(obj)
        else:
            print(f"Request status code: {response.status_code}")
        return responses

    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return responses


def fill_in(prompt,
            suffix,
            model=completion_model,
            **kwargs):
    """A completion call through requests.
        kwargs:
            temperature     = 0 to 1.0
            top_p           = 0.0 to 1.0
            n               = 1 to ...
            best_of         = 4
            frequency_penalty = -2.0 to 2.0
            presence_penalty = -2.0 to 2.0
            max_tokens      = number of tokens
            stop = ["stop"]  # array of up to 4 sequences
    """
    responses = []
    json_data = {"model": model, "prompt": prompt, "suffix": suffix} | kwargs
    try:
        response = requests.post(
            f"{api_base}/completions",
            headers=headers,
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            for choice in response.json()['choices']:
                responses.append(choice)
        else:
            print(f"Request status code: {response.status_code}")
        return responses
    except Exception as e:
        print("Unable to generate Insertion response")
        print(f"Exception: {e}")
        return responses


def complete(prompt,
             model=completion_model,
             **kwargs):

    """A completion call through requests.
        kwargs:
            temperature     = 0 to 1.0
            top_p           = 0.0 to 1.0
            n               = 1 to ...
            best_of         = 4
            frequency_penalty = -2.0 to 2.0
            presence_penalty = -2.0 to 2.0
            max_tokens      = number of tokens
            stop = ["stop"]  # array of up to 4 sequences
    """
    responses = []
    json_data = {"model": model, "prompt": prompt} | kwargs
    try:
        response = requests.post(
            f"{api_base}/completions",
            headers=headers,
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            for choice in response.json()['choices']:
                responses.append(choice)
        else:
            print(f"Request status code: {response.status_code}")
        return responses
    except Exception as e:
        print("Unable to generate Completion response")
        print(f"Exception: {e}")
        return responses


if __name__ == '__main__':
    prompt1 = 'Say this is a test.'
    suffix1 = 'That is why it does nothing.'
    kwa = {
        "temperature":      0.5,
        "top_p":            0.95,
        "max_tokens":       30,
        "n":                3,
        "best_of":          4,
        "frequency_penalty": 2.0,
        "presence_penalty": 2.0
    }
    msgs = [
        {
            "role": "user",
            "content": prompt1
        }
    ]
    answers1 = fill_in(prompt=prompt1,
                       suffix='',
                       **kwa)

    answers2 = complete(prompt=prompt1,
                        **kwa)

    answers3 = answer(messages=msgs)
    print('ok')