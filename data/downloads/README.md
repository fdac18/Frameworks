# Development Environment
- Open a terminal, command prompt, or Anaconda Prompt and navigate to `/Frameworks/data/downloads`
- Python:
  - [Create a python virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
  - Activate the virtual environment and run `pip install -r requirements.txt`
- Anaconda:
  - Create an Anaconda env with `conda env create -f downloads.yml`

# Getting Download Data
- `python get_downloads.py [packages]`
- By default it will get the download data from the table below unless other `packages` are specified.

# Download Data
| framework | npm | download data |
|:-:|:-:|:-:|
| [jQuery](https://github.com/jquery/jquery) | [jquery](https://www.npmjs.com/package/jquery) | `jquery.json` |
| [React](https://github.com/facebook/react) | [react](https://www.npmjs.com/package/react) | `react.json` |
| [Angular](https://github.com/angular/angular/) | [angular](https://www.npmjs.com/package/angular) | `angular.json` |
| [Vue](https://github.com/vuejs/vue) | [vue](https://www.npmjs.com/package/vue) | `vue.json` |
| [Backbone](https://github.com/jashkenas/backbone) | [backbone](https://www.npmjs.com/package/backbone) | `backbone.json` |
| [Ember](https://github.com/emberjs/ember.js) | [ember-source](https://www.npmjs.com/package/ember-source) | `ember-source.json` |
