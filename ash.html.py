from flask import Flask,redirect,url_for
app=Flask(__name__)
# .....create default web page.....
@app.route('/')
def home():
    return "welcome to all"
# # run
# # ......any one content add in app...
@app.route('/home1/<name>')
def home1(name):
    return "Happy Birth Day"+" "+name
# # run..url /home1/ashika->enter
# # .....create more page...
@app.route('/homepage')
def HomePage():
    return "This is Home Page"
@app.route('/aboutpage')
def AboutPage():
    return "This is About Page"
@app.route('/copage')
def ContactPage():
    return "This is Contact Page"
# # run
# # ....url building
@app.route('/main/<name>')
def main(name):
    if name=='homepage':
        return redirect(url_for('HomePage'))
    if name=='aboutpage':
        return redirect(url_for('AboutPage'))
    if name=='copage':
        return redirect(url_for('ContactPage'))
# # run
if __name__=='__main__':
    app.run(debug=True)
#
# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def home():
#     return "Welcome"
# if __name__=='__main__':
#     app.run(debug=True)