import re
import untangle

from bs4 import BeautifulSoup
from pymongo import MongoClient
from xmlr import xmliter


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
    def __init__(self, xmlpost: dict) -> 'Creates a .json doc from an XML' \
                                                    ' element to insert in the post collection':
        assert isinstance(xmlpost, dict)
        self.insertable = {}
        if '@Id' in xmlpost:
            self.insertable['Id'] = xmlpost['@Id']
        if '@PostTypeId' in xmlpost:
            self.insertable['PostTypeId'] = xmlpost['@PostTypeId']
        if '@CreationDate' in xmlpost:
            self.insertable['CreationDate'] = xmlpost['@CreationDate']
        if '@Score' in xmlpost:
            self.insertable['Score'] = xmlpost['@Score']
        if '@ViewCount' in xmlpost:
            self.insertable['ViewCount'] = xmlpost['@ViewCount']
        if '@Body' in xmlpost:
            self.insertable['Body'] = BeautifulSoup(xmlpost['@Body'], features="html.parser").get_text()
        if '@Title' in xmlpost:
            self.insertable['Title'] = xmlpost['@Title']
        if '@Tags' in xmlpost:
            self.insertable['Tags'] = []
            tags = re.findall(r'\<(.*?)\>', xmlpost['@Tags'])
            for striptag in tags:
                self.insertable['Tags'].append(striptag)
        else:
            self.insertable['Tags'] = []
        if '@AnswerCount' in xmlpost:
            self.insertable['AnswerCount'] = xmlpost['@AnswerCount']
        if '@CommentCount' in xmlpost:
            self.insertable['CommentCount'] = xmlpost['@CommentCount']


class CommentDocument:
    def __init__(self, xmlcomment: dict) -> 'Creates a.json doc from an XML element to insert into the ' \
                                                        'Comment collection':
        assert isinstance(xmlcomment, dict)
        self.insertable = {}
        if '@Id' in xmlcomment:
            self.insertable['Id'] = xmlcomment['@Id']
        if '@PostId' in xmlcomment:
            self.insertable['PostId'] = xmlcomment['@PostId']
        if '@Score' in xmlcomment:
            self.insertable['Score'] = xmlcomment['@Score']
        if '@Text' in xmlcomment:
            self.insertable['Text'] = BeautifulSoup(xmlcomment['@Text'], features="html.parser").get_text()
        if '@CreationDate' in xmlcomment:
            self.insertable['CreationDate'] = xmlcomment['@CreationDate']


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

for post in xmliter(postfile, "row"):
    mongopost = PostDocument(post)
    posttags = set(mongopost.insertable['Tags'])
    if neededtagset.intersection(posttags):
        postcol.insert_one(mongopost.insertable)

for comment in xmliter(commentfile, "row"):
    mongocomment = CommentDocument(comment)
    commentcol.insert_one(mongocomment.insertable)
