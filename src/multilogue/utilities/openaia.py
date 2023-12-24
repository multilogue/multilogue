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
# from openai import OpenAI

api_key             = environ.get("OPENAI_API_KEY")
api_key_path        = environ.get("OPENAI_API_KEY_PATH")

organization        = environ.get("OPENAI_ORGANIZATION")
organization_id     = environ.get("OPENAI_ORGANIZATION_ID")
api_base            = environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
api_type            = environ.get("OPENAI_API_TYPE", "open_ai")
default_model       = environ.get("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo-0613")
completion_model    = environ.get("OPENAI_COMPLETION_MODEL",'text-davinci-003')
embedding_model     = environ.get("OPENAI_EMBEDDING_MODEL",'text-embedding-ada-002')  # text-similarity-davinci-001

headers = {
    "Authorization": "Bearer " + api_key,
    "Organization": organization
}

headers_assistants = headers | {"OpenAI-Beta": "assistants=v1", "Content-Type": "application/json"}
parameters_assistants = {"order":"desc", "limit":20}


def list_assistants() -> List:
    """Returns the list of stored assistants."""
    try:
        response = requests.get(f"{api_base}/assistants",
                                headers=headers_assistants,
                                params=parameters_assistants)
        if response.status_code == requests.codes.ok:
            return response.json()['data']
        else:
            print(f"Request status code: {response.status_code}")
    except Exception as e:
        print("Unable to list Assistants. ")
        print(f"Exception: {e}")
        return []


def create_assistant(model='gpt-3.5-turbo-0613',
                     name='machina',
                     description='',
                     instructions='',
                     **kwargs):
    """Creates a new assistant.
        kwargs:
            model = gpt-4
            name = machina
            description = ...maximum length 512
            instructions = ...maximum lengthe 32768
            tools=[{"type":"..."}], code_interpreter, retrieval, or function.
            file_ids = [file_id_1, file_id_2, ...]
            metadata = {"...": "..."} Set of 16 key-value pairs that can be
                attached to an object. This can be useful for storing additional
                information about the object in a structured format. Keys can be
                a maximum of 64 characters long and values can be a maxium of
                512 characters long.

    """
    json_data = {
                    "model": model,
                    "name": name,
                    "description": description,
                    "instructions": instructions
                } | kwargs
    try:
        response = requests.post(
            f"{api_base}/assistants",
            headers=headers_assistants,
            json=json_data
        )
        if response.status_code == requests.codes.ok:
            return response.json()['id']
        else:
            print(f"Request status code: {response.status_code}")
            raise RuntimeError

    except Exception as e:
        print("Unable to create Assistant. ")
        print(f"Exception: {e}")
        return ''


def delete_assistant(assistant_id: str):
    """ Deletes a assistant.
    """
    try:
        response = requests.delete(
            f"{api_base}/assistants/{assistant_id}",
            headers=headers_assistants
        )
        if response.status_code == requests.codes.ok:
            return response.json()['deleted']
        else:
            print(f"Request status code: {response.status_code}")
    except Exception as e:
        print("Unable to create assistant. ")
        print(f"Exception: {e}")
        return False


def upload_file(file_name: str, file_path: str) -> str:
    """ Upfile load.
    """
    try:
        response = requests.post(
            url=f"{api_base}/files",
            headers=headers,
            data={"purpose": "assistants"},
            files={"file":(file_name, open(file_path, "rb"))}
        )
        if response.status_code == requests.codes.ok:
            id = response.json()['id']
            return id
        else:
            print(f"Request status code: {response.status_code}")
            return ''


    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return ''


def delete_file(file_id: str):
    """ Delete file.
    """
    try:
        response = requests.delete(
            url=f"{api_base}/files/{file_id}",
            headers=headers
        )
        if response.status_code == requests.codes.ok:
            return
        else:
            print(f"Request status code: {response.status_code}")
            return

    except Exception as e:
        print("Unable to Delete file. ")
        print(f"Exception: {e}")


def create_thread(**kwargs):
    """ Creates a thread with "messages" and "metadata".
    """
    try:
        response = requests.post(
            f"{api_base}/threads",
            headers=headers_assistants,
            json=kwargs
        )
        if response.status_code == requests.codes.ok:
            return response.json()['id']
        else:
            print(f"Request status code: {response.status_code}")
    except Exception as e:
        print("Unable to create thread. ")
        print(f"Exception: {e}")
        return ''


def delete_thread(thread_id: str):
    """ Deletes a thread.
    """
    try:
        response = requests.delete(
            f"{api_base}/threads/{thread_id}",
            headers=headers_assistants
        )
        if response.status_code == requests.codes.ok:
            return response.json()['deleted']
        else:
            print(f"Request status code: {response.status_code}")
    except Exception as e:
        print("Unable to create thread. ")
        print(f"Exception: {e}")
        return False


def add_message_to_thread(message, thread_id: str, **kwargs):
    """ Adds a message to a thread."""
    try:
        response = requests.post(
            f"{api_base}/threads/{thread_id}/messages",
            headers=headers_assistants,
            json=message
        )
        if response.status_code == requests.codes.ok:
            return response.json()['id']
        else:
            print(f"Request status code: {response.status_code}")
    except Exception as e:
        print("Unable to create thread. ")
        print(f"Exception: {e}")
        return ''


def list_threads() -> List:
    """ Returns the list of stored threads.
    """
    try:
        response = requests.get(
            f"{api_base}/threads",
            headers=headers_assistants
        )
        if response.status_code == requests.codes.ok:
            return response.json()['data']
        else:
            print(f"Request status code: {response.status_code}")

    except Exception as e:
        print("Unable to list threads. ")
        print(f"Exception: {e}")
        return []


def create_run(thread_id: str, assistant_id: str, **kwargs):
    """ Creates a run with "messages" and "metadata".
    """
    json_data = {
        "assistant_id": assistant_id,
    }
    try:
        response = requests.post(
            f"{api_base}/threads/{thread_id}/runs",
            headers=headers_assistants,
            json=json_data
        )
        if response.status_code == requests.codes.ok:
            return response.json()['id']
        else:
            raise RuntimeError(f'Request status code: {response.status_code}')

    except Exception as e:
        print("Unable to create run. ")
        print(f"Exception: {e}")
        return ''


def list_messages(thread_id: str) -> List:
    """ Returns the list of stored messages.
    """
    try:
        response = requests.get(
            f"{api_base}/threads/{thread_id}/messages",
            headers=headers_assistants
        )
        if response.status_code == requests.codes.ok:
            return response.json()['data']
        else:
            raise RuntimeError(f"Request status code: {response.status_code}")

    except Exception as e:
        print("Unable to list messages. ")
        print(f"Exception: {e}")
        return []


if __name__ == '__main__':
    """
    https://openai.com/blog/gpt-4-api-general-availability
    text-similarity-ada-001
    text-similarity-babbage-001
    text-similarity-curie-001
    text-similarity-davinci-001
    """
    kwa = {
        "model": "gpt-3.5-turbo-1106",
        "name": "Machina Ratiocinatrix",
        "description": "Reasoning machine executing metaphilosophical tasks.",
        "instructions": "You are speaking in succinct sentences and phrases without long introductions and conclusions.",
        "tools": [],
        "metadata": {
            "thesis": "Human nature can be changed.",
            "antithesis": "Human nature can not be changed.",
        }
    }

    thre = {
        "messages": [
            {
                "role": "user",
                "content": "Antagonist: I think that human nature can not be changed.",
                "metadata": {},
            }, {
                "role": "user",
                "content": "Protagonist: I think that human nature can be changed.",
                "metadata": {},
            }
        ],
        "metadata": {
            "topic": "Human nature",
            "participants": "protagonist,antagonist,expert"
        },
    }
    # threads_list = list_threads()
    thread_id = create_thread(**thre)
    mes = {
        "role": "user",
        "content": "Human: Please tell me what you think?",
        "metadata": {
            "topic": "Human nature",
            "participants": "protagonist,antagonist,expert",
            "name": "Alex"
        }
    }
    msg = add_message_to_thread(message=mes, thread_id=thread_id)

    # threads_list = list_threads()
    messages = list_messages(thread_id=thread_id)
    dele = delete_thread(thread_id=thread_id)

    assistant_id = create_assistant(**kwa)
    # ass_list = list_assistants()
    run_id = create_run(thread_id=thread_id, assistant_id=assistant_id)

    dele = delete_assistant(assistant_id)
    # model = 'text-search-davinci-doc-001' # 'text-search-davinci-doc-001'
    inp = ["existence"]
    # emb = embeddings(inp, model=model)
    print('ok')