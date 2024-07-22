##
**Dignity Programming Language**
Dignity is a new programming language designed for large, complex projects that need simpler ways to write source code. Its simple and intuitive syntax allows you to define styles, click events, and perform arithmetic operations with ease.

*Table of Contents*
Features
Getting Started
Syntax Reference
Examples
Contributing
License
Features
Simple syntax for defining styles and click events.
Support for variables and arithmetic operations.
Easy-to-read structure for defining sections and runners.
Commenting system using the ``$`` symbol.

##
**Installation**
To install Dignity, clone the repository:

``
git clone https://github.com/Weno-Inc/Dignity
cd dignity
``

##
**Writting Dignity code**
create a ``.dig`` file with some Dignity code like this:

``
A: header: | style: 1: #6278 2:#2827 | click: on-time |
var x = 10
var y = 20
var result = x + y $ Add x and y $
B: h1: | style: must(1: #6278 2:#2827) | click: on-time | $ This is a comment $
C: body: | style: 1: #6278 2:#2827 | click: on-time |
D: messages: | style: 1: #6278 2:#2827 | click: on-time |
Runner: A 1,2,3 | B 1,2,3 | C 1,2,3 | D 1,2,3 |
``

##
**Running Dignity Code**
Run the Dignity code using the provided script:

``
python run_dignity.py example.dig
``

##
**Syntax Reference**
Sections
Sections are defined using capital letters followed by a colon (:). Each section can contain various elements like styles, click events, and variables.

``
A: header: | style: 1: #6278 2:#2827 | click: on-time |
``

##
**Variables**
Variables are declared using the var keyword followed by the variable name, the = symbol, and the value.

``
var x = 10
var y = 20
var result = x + y $ Add x and y $
``

##
**Comments**
Comments are added using the $ symbol and are enclosed within dollar signs.

``
$ This is a comment $
``

##
**Styles**
Styles are defined within a section using the style keyword followed by style definitions.

``
style: 1: #6278 2:#2827
``

##
**Click Events**
Click events are defined within a section using the click keyword followed by the event type.

``
click: on-time
``

##
**Runners**
Runners define the sequence of sections to be executed.

``
Runner: A 1,2,3 | B 1,2,3 | C 1,2,3 | D 1,2,3 |
``

##
**Examples**

Example 1: Basic Style and Click Events

``
A: header: | style: 1: #6278 2:#2827 | click: on-time |
``

Example 2: Variable and Arithmetic Operation

``
var x = 10
var y = 20
var result = x + y $ Add x and y $
``

Example 3: Full Example with Sections and Runner

``
A: header: | style: 1: #6278 2:#2827 | click: on-time |
var x = 10
var y = 20
var result = x + y $ Add x and y $
B: h1: | style: must(1: #6278 2:#2827) | click: on-time | $ This is a comment $
C: body: | style: 1: #6278 2:#2827 | click: on-time |
D: messages: | style: 1: #6278 2:#2827 | click: on-time |
Runner: A 1,2,3 | B 1,2,3 | C 1,2,3 | D 1,2,3 |
``

##
**Contributing**
We welcome contributions to the Dignity programming language! Please follow these guidelines:

Fork the Repository:

Fork the repository on GitHub.
Create a Branch:

Create a new branch for your feature or bugfix.

``
git checkout -b feature-name
``
Make Changes:

Make your changes in the new branch.
Commit and Push:

Commit your changes with a descriptive message.

``
git add .
git commit -m "Add new feature"
git push origin feature-name
``

Create a Pull Request:

Create a pull request from your branch to the main repository.
Code of Conduct
Please adhere to our Code of Conduct in all your interactions with the project.

##
**License**
This project is licensed under the Apache 2.0 License - see the LICENSE.md file for details.

By following this documentation, users can get started with Dignity, understand its syntax, and contribute to its development.
