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
    e. Downloads of each framework  
  2. Derive predictors based on collected data and train a model to make predictions
  3. Build a website to show our collected data, results of model, spread trend of each framework, etc.



# Resources

## Usage data

Folder /data/NPMDependencies contains information on the deployments of various packages

p2mJS maps project name to packages it depends on
```
zcat /data/NPMDependencies/p2mJS|head
uncaughtxcptn_feed;express;nunjucks
imlinus_MyTurn-PHP-JS-ajax-base;ejs;express;mongodb;socket.io
```
e.g., uncaughtxcptn_feed is hosted on github.com/uncaughtxcptn/feed
and depends on two packages: express and nunjucks

b2cPtaPkgBJJS.XX.gz maps the exact time the dependance was observed
```
zcat /data/NPMDependencies/b2cPtaPkgBJJS.0.gz | head -2
000000266aceae74861812a11d20c8f4ef4fc7b6;a08b37e99dadbf62b0a551863d1b6618c9aa355c;greduan_domain-container;1461984667;greduan <me@greduan.com>;bluebird;lodash;neon;krypton-orm
00000071fbb0a71ad2bec47ae66fab3405d333a5;6396bcee97dbb1cbe8434c1a914cdece217efc5c;ocirneaquilina_folkhub;1461610634;profmouse <tappiera00@gmail.com>;body-parser;passport-github;ws;express;express-session;http;url;passport-twitter;passport;jade;mongoose;stylus;passport-facebook;morgan;passport-google;socket.io;cookie-parser;node-debugger;passport-local
```

has format 
```
blob;commit;owner_repo;time (seconds from 1970);author;semicolon separated list of dependencies
```
