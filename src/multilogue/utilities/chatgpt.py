# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict
from os import environ
import requests
import tiktoken
import openai

api_key             = environ.get("OPENAI_API_KEY")
api_key_path        = environ.get("OPENAI_API_KEY_PATH")

organization        = environ.get("OPENAI_ORGANIZATION")
organization_id     = environ.get("OPENAI_ORGANIZATION_ID")
api_base            = environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
api_type            = environ.get("OPENAI_API_TYPE", "open_ai")
default_model       = environ.get("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo-0613")
completion_model    = environ.get("OPENAI_COMPLETION_MODEL",'text-davinci-003')
embedding_model     = environ.get("OPENAI_EMBEDDING_MODEL",'text-embedding-ada-002')

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

    """A simple requests call to ChatGPT chat completions endpoint.
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
                responses.append(choice)
        else:
            print(f"Request status code: {response.status_code}")
        return responses

    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return responses


def fill_in(text_before,
            text_after,
            model=completion_model,
            **kwargs):

    """A completions endpoint call through requests.
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
    json_data = {"model": model, "prompt": text_before, "suffix": text_after} | kwargs
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


def continuations(text_before,
                 model=completion_model,
                 **kwargs) -> List:

    """A completions endpoint call through requests.
        kwargs:
            temperature     = 0 to 1.0
            top_p           = 0.0 to 1.0
            n               = 1 to ...
            best_of         = 4
            frequency_penalty = -2.0 to 2.0
            presence_penalty = -2.0 to 2.0
            max_tokens      = number of tokens
            logprobs        = number up to 5
            stop            = ["stop"]  array of up to 4 sequences
            logit_bias      = map token: bias -1.0 to 1.0 (restrictive -100 to 100)
    """
    responses = []
    json_data = {"model": model, "prompt": text_before} | kwargs
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
        print("Unable to generate Completions response")
        print(f"Exception: {e}")
        return responses


def count_tokens(string: str, model=default_model) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def embeddings(input_list: List[str], model=embedding_model, **kwargs) -> List[Dict]:
    """Returns the embedding of a text string.
        kwargs:
        user = string
    """
    embeddings_list = []
    json_data = {"model": model, "input": input_list} | kwargs
    try:
        response = requests.post(
            f"{api_base}/embeddings",
            headers=headers,
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            embeddings_list = response.json()['data']
        else:
            print(f"Request status code: {response.status_code}")
        return embeddings_list
    except Exception as e:
        print("Unable to generate Embeddings response")
        print(f"Exception: {e}")
        return embeddings_list


if __name__ == '__main__':
    the_text_before = 'Can human nature be changed?'
    the_text_after = 'That is why human nature can not be changed.'
    # bias the words "Yes" and "No" or the new line "\n".
    bias = {
        # 5297: 1.0,          # Yes
        # 2949: -100.0,     # No
        # 198: -1.0         # /n
    }
    kwa = {
        "temperature":      1.0,  # up to 2.0
        # "top_p":            0.5,  # up to 1.0
        "max_tokens":       256,
        "n":                3,
        "best_of":          4,
        "frequency_penalty": 2.0,
        "presence_penalty": 2.0,
        # "logprobs":         3,  # up to 5
        # "logit_bias":       bias
        "stop": ["stop"]
    }

    msgs = [
        {
            "role": "system",
            "content": "You are an eloquent assistant. Give concise but substantive answers without introduction and conclusion."
        },
        {
            "role": "user",
            "content": the_text_before
        }
    ]
    # inp = [the_text_after, the_text_after]
    # emb = embeddings(inp, model='text-similarity-davinci-001')
    #
    # num = count_tokens(prompt1)
    #
    # connections = fill_in(text_before=text_before,
    #                       text_after=text_after,
    #                       **kwa)

    continuations = continuations(text_before=the_text_before,
                                  # model='gpt-3.5-turbo-instruct',
                                  **kwa)

    answers = answer(messages=msgs, **kwa)
    print('ok')