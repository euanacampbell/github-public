[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

GitHub: [github.com/euanacampbell/gitprofile](https://github.com/euanacampbell/gitprofile)

PyPi: [pypi.org/project/gitprofile](https://pypi.org/project/gitprofile)

## Installation

```bash
pip install gitprofile
```

## Import

```python
from gitprofile.github import profile
```

## Setup

```python
from gitprofile.github import profile

github_user_name = 'euanacampbell'
user_profile = profile(github_user_name)
```

## Repositories

```python
from gitprofile.github import profile

github_user_name = 'euanacampbell'
user_profile = profile(github_user_name)

for repo in user_profile:
    print( repo.title )

# github-public
# octopus_energy_api
# boggle_solver
# System-Monitoring
# Pathfinding-Algorithm
# pegasus
# euanacampbell.github.io
# sqlite-editor
# reddit-client
```

## Accessible details

```python
from gitprofile.github import profile

github_user_name = 'euanacampbell'
user_profile = profile(github_user_name)

first_repo = user_profile.repositories[0]

# title
first_repo.title
#gitprofile

# url
first_repo.url
#https://github.com/euanacampbell/gitprofile

# description
first_repo.description
#Extract public repository data.
```