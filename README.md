
# Container Cloning Specification Lab

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

This assignment invites you to study, repair, and test a Python programs called
`perform-container-cloning`. You will practice the task of debugging and
testing a Python function that has defects inside of it due to aliasing.

## Learning Objectives

The learning objectives of this assignment are to:

1. Fix errors due to aliasing
2. Write a test function
3. Write clearly about the programming concepts in this assignment.

## Quick Links

- Due date: Check Discord or the
  [Course Materials Schedule](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials/blob/main/Schedule.md)
- Policy on
  [Tokens](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#tokens)
- [Token Form for Automatic Extension](https://forms.gle/y9Mz55hQKr84wzvXA)
- Policy for
  [Assignment Evaluation](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-evaluation)
- Policy for [Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-submission).
- [#data-structures Discord channel](https://discord.com/channels/877320365825749002/1274744318124359732)
- [Starter repo](https://github.com/allegheny-college-cmpsc-101-fall-2024/container-cloning-starter)

## Policy Reminders

Students are reminded to uphold the Honor Code. Cloning this assignment
repository is a commitment to the latter.

For this assignment, you may use class materials, the textbook, notes,
and the internet, including AI, for reference and learning. AI may **not** be
used to generate answers that you submit. All code and writing that are turned
in **must be your own work and your own words**. Copying or otherwise
representing ChatGTP or other AI outputs as your own work or your own words is
not permitted.

Please ask questions freely in Lab, on the #data-structures Discord channel,
TL office hours, instructor office hours, or by opening a GitHub Issue with
@emgraber tagged at least 24 hours before the deadline.

Modifications to the gatorgrade.yml file are not permitted without explicit
instruction.

## Project Details (Overview Below)

This assignment invites you to study, repair, and test a Python programs called
`perform-container-cloning`. Specifically, it affords you to opportunity to
continue to practice the task of debugging and testing a Python function that
has defects inside of it due to aliasing. After learning more about how containers
are cloned or not cloned in memory in a Python program
and why cloning is needed when a program iterates through a
collection while changing it at the same time, you will find and fix the fault in
the provided source code. Once you have fixed the defect, you will document a
provided test case that (i) creates an input for a function, (ii) passes that
input to the function under test, (iii) captures the output of the function
under test, and (iv) asserts that the captured function output equals the
expected output if the function was implemented correctly. This test case does
not use Pytest.

## Code Survey and Expected Output

If you change into the `source/` directory of your GitHub repository, you will
see one Python file called `perform-container-cloning.py`. The
`perform-container-cloning` module contains a defective function with the
signature `def remove_duplicates(list_one: List[Any], list_two: List[Any]) ->
Tuple[List[Any], List[Any]]`. Your task is to identify and fix the defects
inside of this function! To aid your debugging efforts, you should use and
extend the `def test_remove_duplicates() -> bool` function that should subject
the `remove_duplicates` function to several tests. Although it does not use
Pytest, it is possible to implement a test called `test_remove_duplicates` in
the following fashion:

```python linenums="1"
list_one = [1, 2, 3, 4]
list_two = [1, 2, 5, 6]
expected_list_one = [3, 4]
expected_list_two = [5, 6]
test_case_passed = True
(actual_list_one, actual_list_two) = remove_duplicates(list_one, list_two)
if expected_list_one == actual_list_one and expected_list_two == actual_list_two:
    print("Expected output correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]")
else:
    print("Expected output not correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]")
    print(f"   actual_list_one: {actual_list_one}")
    print(f"   actual_list_two: {actual_list_two}")
    test_case_passed = False
return test_case_passed
```

Lines `1` and `2` of this function create two lists, called `list_one` and
`list_two`, that have in common the values `1` and `2`. Lines `3` and `4` of
this function indicate that, if the `remove_duplicates` function worked
correctly, then its output should be a tuple container the lists `[3, 4]` and
`[5, 6]`. After making the assumption that the test case will pass on line `5`,
the function calls `remove_duplicates` and checks to see if the expected output
equals the actual output returned by the function. If the expected output is
correct, then line `8` displays a message indicating that is the case.
Otherwise, lines `10` through `13` signal that the test did not pass and display
diagnostic output to highlight this fact for the tester. Ultimately, if this
test case passes correctly it will help to establish a confidence in the
correctness of `remove_duplicates`. When the test case for the
`remove_duplicates` function passes, then it should produce the following
output:

``` text
Expected output correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]
The test case passed!
```

## Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage
project dependencies and virtual environments, it does not support the use of
commands like `poetry run task test`.

### Gatorgrade

After you have added functionality and checked that your code produces the
expected output, the command `gatorgrade --config config/gatorgrade.yml`
will check your work with the automatic grader. If
your work meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. All checks must pass in order to get 100% on this lab. All other
gatorgrade score are graded as 0%. Note, modifications to the gatorgrade.yml
file are not permitted without explicit instruction.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file.
Since this is a source code survey, you should provide output from running each
of the provided Python programs on your own laptop and then explain how the
program's source code produced that output. A specific goal for this project is
to ensure that you can explain the syntax and meaning of function signatures
like `def remove_duplicates(list_one: List[Any], list_two: List[Any]) ->
Tuple[List[Any], List[Any]]`. You should also be able to discuss what defect(s)
you found in the `remove_duplicates` function and how you fixed them.

## Project Overview

After cloning this repository to your computer, please take the following
steps:

- Use the `cd` command to change into the directory for this repository.
- Change into the program source code directory by typing `cd source`.
- Run the provided Python script by typing the following:
  - `python perform-container-cloning.py`: perform duplicate removal with container cloning
- The program should initially produce the following output:

```text
Expected output not correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]
  actual_list_one: [2, 3, 4]
  actual_list_two: [2, 5, 6]
At least one test case did not pass!
```

- You need to fix the defects in the program so that it produces the correct output:

```text
Expected output correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]
All of the test cases passed!
```

- After fixing the defects, confirm that the programs are producing the expected output.
- Make sure that you can explain why the programs produce the output that they do.
- Run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`.  
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code and `writing/reflection.md` file..
- Submit work to GitHub using git in the terminal
  - Open a terminal
  - `cd` to the project directory on your computer
  - type `git status` to see a list of files you have updated
  - type `git add .` to "stage" your files
  - type `git commit -m "PUT YOUR OWN SHORT MESSAGE"`
  - type `git push origin main`
  - type your ssh passphrase if requested
