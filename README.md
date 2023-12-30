# Refactoring Example

This is a sample project for practicing/demoing refactoring. It is adapted to
Python from the example in Chapter 1 of Martin Fowler's book
*Refactoring: Improving the Design of Existing Code, 2nd Edition*.


## Usage

Clone this project and follow along with the refactoring steps described in
Chapter 1 of the *Refactoring* book.

To see a walkthrough of the steps, switch to the `solution` branch and follow
along with the commits there.

Before running tests, first install the dependencies:

```sh
pip install -r requirements.txt
```

Then use the [hatch](https://hatch.pypa.io/latest/) tool to run tests.

```sh
hatch run test
```

Alternatively, you can run a watch script to re-run tests any time you change the python source.

```sh
hatch run watch
```
