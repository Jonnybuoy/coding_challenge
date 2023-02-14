# Coding Challenge - Python

This is a coding challenge that writes an algorithm that given an M X N  matrix, returns all numbers that are the maximum value in its row but the minimum in its column.

## Prerequisites

Make sure you have the following before beginning:

```bash
python3-dev
git
virtualenv
pytest
```

## Cloning from Github

From your terminal, go to the directory you want to clone your project into.

```bash
$ cd path/to/your/directory
```
Clone the project
```bash
$ git clone git@github.com:Jonnybuoy/coding_challenge
```

## Setting up the dependencies

Navigate into the projects directory from the terminal.
```bash
$ cd path/to/your/directory/coding_challenge
```
Create a virtual environment for your project
```bash
$ python3 -m venv name-of-your-virtualenv
```
Activate your virtual environment.
```bash
$ source name-of-your-virtualenv/bin/activate
```
Install pytest
```bash
(name-of-your-virtualenv)$ pip3 install pytest
```

## Running the program

On the project's directory, run:
```bash
$ python matrix_algorithm.py
```

Enter your matrix input eg. [[5, 16, 20], [9, 11, 18], [15, 16, 17]]

To run the test, run:
```bash
$ pytest test_matrix_algorithm.py
```
