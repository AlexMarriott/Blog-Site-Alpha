"""
This file is used for replacing the environment variables during the deployment stage. The variables are held in travis-ci for the repo.

This means that the env variables are not included on the website, reducing the security risk.
"""

import os
from yaml import load, dump, Loader, YAMLError

with open("app.yaml", 'r') as stream:
    try:
        loaded = load(stream, Loader=Loader)
    except Exception as exc:
        print(exc)

# Modify the fields from the dict
for i in loaded['env_variables']:
    loaded['env_variables'][i] = os.environ[i]


# Save it again
with open("app.yaml", 'w') as stream:
    try:
        dump(loaded, stream, default_flow_style=False)
    except YAMLError as exc:
        print(exc)

with open("app.yaml", 'r') as stream:
    try:
        loaded = load(stream, Loader=Loader)
    except Exception as exc:
        print(exc)

for i in loaded['env_variables']:
    print(loaded['env_variables'][i])