#from __future__ import print incase of python2
import requests
import sys
import json
from flask import Flask, render_template, request, make_response, jsonify
from logging import DEBUG
app=Flask(__name__)
app.logger.setLevel(DEBUG)
def dict_extract(author,posts):
    ap_dict={}
    for i in author:
        count=0
        for k in posts:
            if i['id']== k['userId']:
                count +=1
        ap_dict[i['name']]=count
    return render_template('I1_authors.html',dict=ap_dict)
@app.route('/')
def helloworld():
    return 'Hello World - Prasanth'
@app.route('/authors')
def author_post():
    URL1='https://jsonplaceholder.typicode.com/users'
    URL2='https://jsonplaceholder.typicode.com/posts'
    author_info=requests.get(URL1)
    posts_info=requests.get(URL2)
    author_data=json.loads(author_info.text)
    posts_data=json.loads(posts_info.text)
    return dict_extract(author_data, posts_data)
@app.route('/setcookie')
def setcookie():
        res=make_response('cookies are set')
        res.set_cookie('name','Prasanth')
        res.set_cookie('age','18')
        return res
@app.route('/getcookie')
def getcookie():
    keyvalue= request.cookies
    return render_template('I1_cookie.html',keyvalue=keyvalue)

@app.route('/robots.txt')
def denyrequest():
    return render_template('I1_deny.html')
@app.route('/html',methods=['POST','GET'])
def renderhtml():
    return render_template('I1_renderhtml.html')
@app.route('/input',methods=['POST','GET'])
def displayform():
    return render_template('I1_input.html')
@app.route('/display',methods=['POST','GET'])
def display():
    logged_data=request.form['from_disp']
    app.logger.debug(logged_data)
    return jsonify(request.form.to_dict())
if __name__=='__main__':
    app.run(debug=True)
