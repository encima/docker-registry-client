from requests.auth import HTTPBasicAuth
import requests
import config

from clint.textui import prompt, puts, colored, validators
from clint.arguments import Args
from terminaltables import AsciiTable

endpoints = {
        'repos': '_catalog',
        'tags': '/tags/list'
        }

def create_options(arr):
    inst_options = []
    for k, r in enumerate(arr):
        inst_options.append({'selector':k, 'prompt': r, 'return': r})
    return inst_options


repos_req = requests.get(config.BASE_URL + endpoints['repos'], auth=(config.USER, config.PWD))
repos = repos_req.json()['repositories']
repo_options = create_options(repos)
inst = prompt.options("Choose a repo", repo_options)
tags = requests.get("{}{}{}".format(config.BASE_URL, inst, endpoints['tags']), auth=(config.USER, config.PWD))
tags = tags.json()['tags']
tag_options = create_options(tags)
inst = prompt.options("Choose a tag", tag_options)


