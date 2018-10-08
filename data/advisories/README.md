# How to get the NPM advisory data
 - Install [nodejs](https://nodejs.org/en/download/)
 - Open up a terminal or command prompt and navigate to `/Dependencies/`
 - run `npm install nsp` then `nsp gather`

# Getting development environment up and running
- Install [python 3](https://www.python.org/downloads/) or setup [Anaconda](https://www.anaconda.com/download/) (Preferred)
- Open a terminal, command prompt, or Anaconda Prompt and navigate to `/Frameworks/data/advisories`
- Python:
  - [Create a python virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
  - Activate the virtual environment and run `pip install -r requirements.txt`
- Anaconda:
  - Create an Anaconda env with `conda env create -f dependencies.yml`

# Patching ```advisory.json``` with version information
- Open a terminal, command prompt, or Anaconda prompt
- Run `python patch_advisories.py advisories.json`
  - This step will take a while, npmjs.com rate limits connections to ~100 requests every so often
  - It should be able to overcome the rate limit, but it is possible that the script will need to be rerun
  - If it needs to be rerun then copy/rename `patched_advisories.json` to `advisories.json` and then rerun it
