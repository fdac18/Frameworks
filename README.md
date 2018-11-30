# [Our website](https://fdac-frameworks.herokuapp.com/)

# Goal – predict which JavaScript front end framework will be the most popular

## Background
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Choosing from amongst even the most popular JavaScript frameworks for a new project can be a challenging process. There seems to be a new handful gaining popularity every year or so, and the previous ones don’t seem to lose steam either! It's very interesting to predict which framework will take over the market in future.

### Here is a couple of popular and competitive frameworks:
  - React.js (created and maintained by Facebook)
  - Angular.js (supported by Google)
  - Ember.js (opinionated best practices, rapidly getting your application into production)
  - Backbone.js (old, mature, solid community resource and support)
  - More?

## Objective – predict the popularity of frameworks in the future  
  1. Collect framework related resources (time information must be included):  
    a. Identify projects that uses these frameworks, collect commits, and the authors of these projects  
    b. Collect package dependencies and dependents of each framework  
    c. Collect related questions and answers of each framework on StackOverflow  
    d. Retrieve issues and responses of each framework  
    e. ~~Downloads of each framework~~
  2. Derive predictors based on collected data and train a model to make predictions
  3. Build a website to show our collected data, results of model, spread trend of each framework, etc.
