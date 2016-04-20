Property.Works coding assignment
================================

# Description

This assignment is based on a real problems, 
that our team encounters every day. It is expected to take no more than 1 hour to complete. 

There are four files included - two fixtures containing html snippets to be parsed,
one test file and the parser file:

    fixtures/fixture1.html
    fixtures/fixture2.html
    src/parser.py
    tests/test.py


`Parser.parse()` method takes a string containing html content as a parameter, 
and returns `address`, `suite`, `postcode` and `description`. 
Your task is to implement it any way you like, providing that it produces expected result and the tests pass.

Tests only validate `address`, `suite` and `postcode` variables.
There are two, commented out, _bonus_ tests in the suite that verify the `description` field.
They are aimed at senior developers and candidates applying for junior developer position
can ignore them. 

Use any means you see fit (regex, libxml2, ElementTree, lxml etc.).

We will assess all aspects of the provided implementation, from the overall coding style, readability and 
documentation/comments to extensibility, reusability and perfomance.


# Setup

To run unit test suite, install `nose`, eg. using `pip`: 

    pip install -r ./requirements.txt
    
Run tests:

    nosetests
    

# Submitting the solution

Please include all the libraries and dependecies needed to run the code in `requirements.txt` file.

Either pack all the files using zip/tar or send a link to github/bitbucket repository.
Please don't create a pull request if you cloned/forked it from one of our repositories 
(as other candidates will be completing the same assignment).

