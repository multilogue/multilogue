# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
from json import dumps, loads
from github import Github, InputGitAuthor, UnknownObjectException, AuthenticatedUser
from urllib3 import disable_warnings


organization    = environ.get('GITHUB_ORGANIZATION')
github_token    = environ.get('GITHUB_TOKEN', '')
github_name     = environ.get('GITHUB_NAME', '')
github_email    = environ.get('GITHUB_EMAIL', '')

# The useless urllib3 warning is too maddening for a human being.
disable_warnings()

# Author
author = InputGitAuthor(
    name=github_name,
    email=github_email
)


# Repo
def creupdate_repo(repository_name,
                   description=None,
                   private=False):
    """
    https://pygithub.readthedocs.io/en/latest/github_objects/AuthenticatedUser.html?highlight=get_user#github.AuthenticatedUser.AuthenticatedUser.create_repo_from_template
    """
    gh = Github(github_token, verify=False)
    if organization:
        org = gh.get_organization(organization)
        try:
            repo = org.get_repo(f'{repository_name}')
        except UnknownObjectException:
            template_repo = gh.get_repo(f'multilogue/multilogue-template')
            repo = org.create_repo_from_template(repository_name,
                                                 template_repo,
                                                 description,
                                                 private=private)
        return repo
    else:
        try:
            repo = gh.get_repo(repository_name)
        except UnknownObjectException:
            template_repo = gh.get_repo(f'multilogue/multilogue-template')
            user = gh.get_user()
            repo = user.create_repo_from_template(repository_name,
                                                  description,
                                                  template_repo,
                                                  private=private)
        return repo


def creupdate_file(repository,
                   file_path,
                   file_content,
                   branch='main'):
    """ Create or update a file in a repository
        file_path: path to the file formatted as
    """
    try:
        # Get the file if it exists
        file = repository.get_contents(file_path)

        # Update the file content
        repository.update_file(
            path=file.path,
            message='Update file',
            content=file_content,
            sha=file.sha,
            branch=branch,
            committer=author,
            author=author
        )

    except UnknownObjectException:
        # Create a new file if it doesn't exist
        repository.create_file(
            path=file_path,
            message='Create file',
            content=file_content,
            branch=branch,
            committer=author,
            author=author,
        )
    return True


def read_file(repository,
              file_path,
              branch='main'):
    """ Read a file in a repository
        file_path: path to the file formatted as
    """
    try:
        # Get the file if it exists
        ingested_file = repository.get_contents(file_path)
        content = ingested_file.decoded_content.decode("utf-8")

    except UnknownObjectException:
        # The file doesn't exist
        print('The file does not exist')
        content = ''

    return content


if __name__ == "__main__":
    """ Simple debug example 
    """
    example_json_file_content = {
        "role": "user",
        "name": "test",
        "content": "Test content for a test file",
        "function_call": None
    }

    repository_object = creupdate_repo(repository_name='test-multilogue',
                                       description='test repository description',
                                       private=False)

    try:
        result = creupdate_file(repository=repository_object,
                                file_path='notes/log_round_1.json',
                                file_content=dumps(example_json_file_content),
                                branch='main')
    except Exception as e:
        print('failed ', e)

    try:
        file = read_file(repository=repository_object,
                         file_path='notes/log_round_1.json',
                         branch='main')

    except UnknownObjectException:
        print('No such file')

    print('ok')