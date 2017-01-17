jk_pwdinput
===========

Introduction
------------

This python module provides the capability to read a passwords from STDIN. In contrast to typical password input
in this case for every character pressed an asterisk is displayed.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-pwdinput)
* [pypi.python.org](https://pypi.python.org/pypi?name=jk_pwdinput)

How to use this module
----------------------

### Requirements

This module will require the following python module(s) to operate:

* [readchar](https://pypi.python.org/pypi/readchar) - License: MIT

### Import

To import this module use the following statement:

```python
import jk_pwdinput
```

### Reading a password

In order to read a password from STDIN use the following code:

```python
userPwd = jk_pwdinput.readpwd("Please enter a password: ")
if userPwd is None:
	# no password given
	....
else:
	# user provided the password
	....
```

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



