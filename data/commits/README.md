# Commit Histories

All commit data is on `da2.eecs.utk.edu` under `/data/NPMDependencies`

`p2mJS` maps project names to the packages they depend on
```
zcat /data/NPMDependencies/p2mJS | head -1
uncaughtxcptn_feed;express;nunjucks
```
is in the format
```
owner_repo;list of dependencies
```
e.g. `uncaughtxcptn_feed` is hosted on `github.com/uncaughtxcptn/feed`
and it depends on two packages: `express` and `nunjucks`

`b2cPtaPkgBJJS.XX.gz` maps the exact time the dependance was observed
```
zcat /data/NPMDependencies/b2cPtaPkgBJJS.0.gz | head -1
000000266aceae74861812a11d20c8f4ef4fc7b6;a08b37e99dadbf62b0a551863d1b6618c9aa355c;greduan_domain-container;1461984667;greduan <me@greduan.com>;bluebird;lodash;neon;krypton-orm
```
is in the format
```
blob;commit;owner_repo;time (seconds from 1970);author;list of dependencies
```
