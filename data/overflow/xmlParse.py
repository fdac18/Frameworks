import re
import untangle

from bs4 import BeautifulSoup
from pymongo import MongoClient


class TagDocument:
    def __init__(self, xmltag: untangle.Element) -> 'Creates a .json doc from an XML' \
                                                    ' element to insert in the tag collection':
        assert isinstance(xmltag, untangle.Element)
        self.insertable = {}
        if xmltag['Id']:
            self.insertable['Id'] = xmltag['Id']
        if xmltag['TagName']:
            self.insertable['TagName'] = xmltag['TagName']
        if xmltag['Count']:
            self.insertable['Count'] = xmltag['Count']
        if xmltag['ExcerptPostId']:
            self.insertable['ExcerptPostId'] = xmltag['ExcerptPostId']
        if xmltag['WikiPostId']:
            self.insertable['WikiPostId'] = xmltag['WikiPostId']


class PostDocument:
    def __init__(self, xmlpost: untangle.Element) -> 'Creates a .json doc from an XML' \
                                                    ' element to insert in the post collection':
        assert isinstance(xmlpost, untangle.Element)
        self.insertable = {}
        if xmlpost['Id']:
            self.insertable['Id'] = xmlpost['Id']
        if xmlpost['Id']:
            self.insertable['PostTypeId'] = xmlpost['PostTypeId']
        if xmlpost['CreationDate']:
            self.insertable['CreationDate'] = xmlpost['CreationDate']
        if xmlpost['Score']:
            self.insertable['Score'] = xmlpost['Score']
        if xmlpost['ViewCount']:
            self.insertable['ViewCount'] = xmlpost['ViewCount']
        if xmlpost['Body']:
            self.insertable['Body'] = BeautifulSoup(xmlpost['Body'], features="html.parser").get_text()
        if xmlpost['Title']:
            self.insertable['Title'] = xmlpost['Title']
        if xmlpost['Tags']:
            self.insertable['Tags'] = []
            tags = re.findall(r'\<(.*?)\>', xmlpost['Tags'])
            for striptag in tags:
                self.insertable['Tags'].append(striptag)
        else:
            self.insertable['Tags'] = []
        if xmlpost['AnswerCount']:
            self.insertable['AnswerCount'] = xmlpost['AnswerCount']
        if xmlpost['CommentCount']:
            self.insertable['CommentCount'] = xmlpost['CommentCount']


class CommentDocument:
    def __init__(self, xmlcomment: untangle.Element) -> 'Creates a.json doc from an XML element to insert into the ' \
                                                        'Comment collection':
        assert isinstance(xmlcomment, untangle.Element)
        self.insertable = {}
        if xmlcomment['Id']:
            self.insertable['Id'] = xmlcomment['Id']
        if xmlcomment['PostId']:
            self.insertable['PostId'] = xmlcomment['PostId']
        if xmlcomment['Score']:
            self.insertable['Score'] = xmlcomment['Score']
        if xmlcomment['Text']:
            self.insertable['Text'] = BeautifulSoup(xmlcomment['Text'], features="html.parser").get_text()
        if xmlcomment['CreationDate']:
            self.insertable['CreationDate'] = xmlcomment['CreationDate']


activeclient = MongoClient(host='da1')
sodatadb = activeclient.fdac18stackoverflow
tagcol = sodatadb.tags
postcol = sodatadb.posts
commentcol = sodatadb.comments

neededtags = ['reactjs', 'angularjs', 'vue.js', 'vuejs2', 'ember.js', 'jquery', 'backbone.js']
neededtagset = set(neededtags)

xmldir = '/data/NPMDependencies/stackoverflowdata/'
tagfile = xmldir + 'Tags.xml'
postfile = xmldir + 'Posts.xml'
commentfile = xmldir + 'Comments.xml'

tagXML = untangle.parse(tagfile)
for tag in tagXML.tags.children:
    mongotag = TagDocument(tag)
    tagcol.insert_one(mongotag.insertable)

postXML = untangle.parse(postfile)
for post in postXML.posts.children:
    mongopost = PostDocument(post)
    posttags = set(mongopost.insertable['Tags'])
    if neededtagset.intersection(posttags):
        postcol.insert_one(mongopost.insertable)

commentXML = untangle.parse(commentfile)
for comment in commentXML.comments.children:
    mongocomment = CommentDocument(comment)
    commentcol.insert_one(mongocomment.insertable)
