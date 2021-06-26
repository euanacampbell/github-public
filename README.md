[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

GitHub: [github.com/euanacampbell/github_public](https://github.com/euanacampbell/octopus_energy_api)

PyPi: [pypi.org/project/github-public](https://pypi.org/project/octopus-energy-api/)

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

github-public
octopus_energy_api
boggle_solver
System-Monitoring
Pathfinding-Algorithm
pegasus
euanacampbell.github.io
sqlite-editor
reddit-client
```

## Accessible details

```python
from gitprofile.github import profile

github_user_name = 'euanacampbell'
user_profile = profile(github_user_name)

first_repo = user_profile[0]

# title
first_repo.title

# url
first_repo.url

# description
first_repo.description
```