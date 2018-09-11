# Dependencies
GitHub Project Relationships and NPM Dependencies

# How to get the NPM advisory data
 - Install [nodejs](https://nodejs.org/en/download/)
 - Open up a terminal and navigate to `/Dependencies/`
 - run `npm install nsp` then `nsp gather`

# Patching ```advisory.json``` with version information
- Install [python 3](https://www.python.org/downloads/) or setup [Anaconda](https://www.anaconda.com/download/) (Preferred)
- Python:
  - Open a terminal or command prompt and navigate to `/Dependencies/`
  - [Create a python virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
  - Activate the virtual environment and run `pip install -r requirements.txt`
- Anaconda:
  - Open a terminal or Anaconda Prompt and navigate to `/Dependencies/`
  - Create an Anaconda env with `conda env create -f dependencies.yml`

# Patching ```advisory.json``` with version information
- Open a terminal, command prompt, or Anaconda prompt
- Run `python patch_advisories.py advisories.json`