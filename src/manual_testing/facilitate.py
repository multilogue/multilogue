# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import json
import jsonlines
import os
from multilogue.discussion.conversation import Conversation
from multilogue.utilities.githublog import creupdate_repo, creupdate_file
from grammateus import Grammateus
from dotenv import load_dotenv
load_dotenv()


def main():
    pass


if __name__ == '__main__':
    human_says = input(f'Do you want to start a new conversation? [y/n/continue/restart/clean/publish] ')
    if human_says == 'y':
        this_agenda = clean_up()
        delete_record(file_path=this_agenda['record_file'])
        main(agenda=this_agenda)
    elif human_says == 'n':
        print("Not going to do anything. Goodbye!")
    elif human_says == 'continue':
        main(agenda=load_agenda())
    elif human_says == 'restart':
        main(agenda=load_agenda())
    elif human_says == 'publish':
        human_says = input('Branch name? ("Enter" for "main") ')
        if human_says == '':
            branch = 'main'
        else:
            branch = human_says
        # Create the README.md file
        this_agenda = load_agenda()
        md_file = make_md_file(this_agenda)
        # Creupdate the repository
        with open('./util/config.json', 'r') as file:
            configuration = json.load(file)
        organization = configuration['organization']
        repository_object = creupdate_repo(repository_name=configuration['repository'],
                                           description='Dialogue with an AI',
                                           private=False)
        try:
            result = creupdate_file(repository=repository_object,
                                    file_path='./README.md',
                                    file_content=md_file,
                                    branch=branch)
        except Exception as e:
            print('failed ', e)
        try:
            result = creupdate_file(repository=repository_object,
                                    file_path='./agenda.json',
                                    file_content=json.dumps(this_agenda),
                                    branch=branch)
        except Exception as e:
            print('failed ', e)

    elif human_says == 'clean':
        this_agenda = clean_up()
        delete_record(file_path=this_agenda['record_file'])
        print("All have been cleaned up.")
    exit()
