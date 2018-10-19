# Development Environment
- Open a terminal, command prompt, or Anaconda Prompt and navigate to `/Frameworks/data/issues`
- Python:
  - [Create a python virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
  - Activate the virtual environment and run `pip install -r requirements.txt`
- Anaconda:
  - Create an Anaconda env with `conda env create -f github.yml`

# Gather Github Issues
- Create a [personal access token](https://github.com/settings/tokens/new) with no scopes selected
- Copy the token and store it somewhere
- `python get_issues.py github_username access_token`


# Clean Github Issues
- `python clean_issues.py`
- Only do this after you've collected the dirty data.

# Gathering Comments
- api url `https://api.github.com/repos/{owner}/{repo}/issues/{issue_num}`
- comments url `https://api.github.com/repos/{owner}/{repo}/issues/{issue_num}/comments`