import os
WTF_CSRF_ENABLED = True
SECRET_KEY = "sshhh"
#to prevent cross site request forgery,, which is where if you log in
# and go to a malicious site, now the bad guy can explot your logged in session
# now you're missing £1000
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True   

#this configures sqlite and gives us the directory name