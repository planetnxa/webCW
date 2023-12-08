#this is our start up script...
#so when this file is ran then it starts a development server?
# this is like the power on button, and the init file is like the "load dependencies section"

from app import app
if __name__ == "__main__":
    app.run(debug=True)
