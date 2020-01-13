# Upcoming Elections Practical
Full instructions for installing Flask can be found [here](http://flask.pocoo.org/docs/1.0/installation/).

## Set up Python3 env

```
pip install --upgrade virtualenv

# Create a virtual env in Python3 called `dw_practical`
virtualenv --python=python3 dw_practical

# Enter the virtual env -- you'll need to do this every time to run anything
source ./dw_practical/bin/activate

# Install the requirements
pip3 install -r requirements.txt

# If you want to exit the virtualenv when you're done, you can use the `deactivate` command by itself.
```
If you don't have `pip` installed, follow the instructions [here](https://pip.pypa.io/en/stable/installing/)


## Running

From the `dw-practical-upcoming-elections/python` directory, run the following:

```
# If you haven't done this in this terminal yet
source ./dw_practical/bin/activate

export FLASK_APP=elections
export FLASK_ENV=development
flask run
```

## Testing

```
# If you haven't done this in this terminal yet
source ./dw_practical/bin/activate

pytest
```

## Note on Python 3
You can skip this section if you're sure your computer is configured to run Python 3 by default.

The code is set up to run with Python 3. This should take no extra configuration on your part
as long as you have Python 3 installed, even if it is not your default. You can check that your
computer has it by running `which python3`. If you don't have it, see the instructions
[here](https://realpython.com/installing-python/).

If you are familiar with Python 2 but haven't worked much with Python 3, you shouldn't notice
much of a difference. Likely the only notable difference you'll run into in this project is when
debugging - `print` has to be called like `print("Something")` rather than`print "Something"`
as was previously allowed.

If setting up or running Python 3 causes you any issues, please reach out. Getting things running
is not part of the evaluation and we'll be happy to help troubleshoot without judgement.
