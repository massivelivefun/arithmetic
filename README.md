# Arithmetic

A simple property based test suite covering peano arithmetic concepts.

## Setup

Create a virtual environment.

```python3 -m venv /path/to/new/virtual/environment```

Then activate the virtual environment.

On ZSH or BASH...

```source ./<venv>/bin/activate```

On FISH...

```./<venv>/bin/activate.fish```

Afterwards, install the python packages in the
requirements.txt with the venv's pip or pip3.

```pip install -r requirements.txt```

Or...

```pip3 install -r requirements.txt```

## Usage

To run coverage tests...

```coverage run -m pytest```

To get a coverage report run this 
after running coverage run.

```coverage report -m```

To run mutation tests...

```mutmut run```

The report will happen after the runtime.
