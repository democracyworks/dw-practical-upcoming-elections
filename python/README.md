# Democracy Works Practical: Upcoming Elections

A [Flask](https://flask.palletsprojects.com/en/2.0.x/) web application that
serves as a starting point for the Democracy Works hiring practical.

## Installation

### Requirements

- Python 3.6 or higher. If you don't have it, [follow the instructions for your
  platform](https://realpython.com/installing-python/).

### Dependencies

To install the dependencies, run the following commands:

```sh
## Create a virtual Python environment in the `.venv` directory
python3 -m venv .venv

## Ensure you have pip installed. For help see:
## https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
python3 -m pip install --user --upgrade pip

## Enter the virtual environment: you'll need to do this in your environment to
## run commands at command line.
source .venv/bin/activate

## Install the requirements
pip install -r requirements.txt
```

When you are done with the virtual environment, use `deactivate` to exit it and
return to your normal shell, or quit your terminal program.

## Usage

### Running

To run the application, use the following commands:

```sh
## OPTIONAL: If you haven't done this yet
source .venv/bin/activate

export FLASK_APP=elections
export FLASK_ENV=development
flask run
```

### Tests

To run the test suite, use the following command:

```
## OPTIONAL: If you haven't done this yet
source .venv/bin/activate

pytest
```

## Troubleshooting

If you need any help or notice something wrong with these instructions, let your
contact at Democracy Works know! Help getting started is not part of the
evaluation and you reaching out will not impact your score.
