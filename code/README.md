# testing-final-project

# Setting Up

After clonning the repository we will need a virtual enviroment set up and runingin.
Run the commands at the root of the folder. 
To install the the virtual enviroment:

$ pip install virtualenv

After this, we need to set it up:

$ virtualenv venv --python=python3.7

You should see a folder nameve venv being generated.

Now we need to start our virtual enviorment:

For Windows:

$ .venv/Scripts/activate.bat

For Linux/macOS:

$ source venv/bin/activate

This should start your virtual - you should see a (venv) at your terminal.

To get all the required packages, run:

$ pip install -r requirments.txt

That's it.
To quit the virtual enviroment, write:
$ deactivate

# Running the project

You need to have your veirtual enviroment running:

For Windows:

$ .venv/Scripts/activate.bat

For Linux/macOS:

$ source venv/bin/activate

To run the server on your local machine:

$ python code/app.py

The server should automatically update every time you make a change, so you don't need to restart it.

In case you want to terminate it, press CTRL + C

# Additional

The database is already generated (it's in code/data.db)
There is alread a single user, with name "test" and a password "test".
There is an image with id=1, that you can test.