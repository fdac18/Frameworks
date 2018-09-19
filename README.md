# Dependencies
GitHub Project Relationships and NPM Dependencies

# How to get the NPM advisory data
 - Install [nodejs](https://nodejs.org/en/download/)
 - Open up a terminal or command prompt and navigate to `/Dependencies/`
 - run `npm install nsp` then `nsp gather`

# Getting development environment up and running
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
  - This step will take a while, npmjs.com rate limits connections to ~100 requests every so often
  - It should be able to overcome the rate limit, but it is possible that the script will need to be rerun
  - If it needs to be rerun then copy/rename `patched_advisories.json` to `advisories.json` and then rerun it

# New goal -- predict which Javascript front end framework will take over
## Background
Choosing from amongst even the most popular JavaScript frameworks for a new project can be a challenging process. There seems to be a new handful gaining popularity every year or so, and the previous ones don’t seem to lose steam either! It's very interesting to predict which framework will take over the market in future.

Here is a couple of popular and competitive frameworks:
  - React.js (created and maintained by Facebook)
  - Angular.js (supported by Google)
  - Ember.js (opinionated best practices, rapidly getting your application into production)
  - Backbone.js (old, mature, solid community resource and support)
  - More?

## Objective
**predict popularity of frameworks in future**  
sub-objectives:
  1. collect framework related resources (time information must be included):
    - identify projects that uses these frameworks, collect commits & authors of these projects
    - collect package dependencies and dependents of each framework
    - collect related questions and answers of each framework on StackOverflow
    - retrieve issues and responses of each framework
    - downloads of each framework
  2. calculate predictors based on collected data and train a model (choice model) to make predictions
  3. build a website to show our collected data, result of model, spread trend of each framework, etc.
