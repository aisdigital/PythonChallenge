[![Build Status](https://travis-ci.org/akafael/PythonChallenge.svg?branch=feature/rafael_lima)](https://travis-ci.org/akafael/PythonChallenge)

# Python Challenge

AIS Python Challenge

Hey, whats up? Are you ready to start the challenge? We would like to remember that this step will help us evaluate your performance. Take a deep breath and let’s go!
We’re rooting for you. 😁

## Some Rules

1 - **DO NOT** share your answer with others.

2 - Remember that this challenge it's meant to evaluate your skills, you don't necessarily have to finish **all** the challenge code implementation, we just want to get know you better. 😁

## Steps

- Fork the repository.
- Create a branch (from master branch) with the following pattern:
  Use your name as branch name, eg:
  Considering that my name is José da Silva the branch name should be: "feature/jose_silva"
- Work **only** on your branch, and after you finish, create a Pull Request targeting "master" branch on this repository.
- **DO NOT** change the reviewers of your Pull Request.

# Requirements 

* Python 3 installed

## Instructions
To run the project use basic python command

*  `python -m main`

After set it all up, let's go to the challenge \o/

## Challenge 

Given a csv input file `./input/property_sales_transactions.csv` what you have to do is:

Create a command line application where you will:
* Read the CSV file and store the data in memory(data don't need to be ordered). The application will do actions based on the arguments provided. 

1. Search by SCHOOLDESC: `python -m main --filter-school-desc abc` will seach by all the entries that contains and show the PAIRID and `SCHOOLDESC` of each one.

2. Search by PARID: `python -m main --find-pair-id 0028S00066000000` will find an entry by PARID and output the full entry in JSON format on the screen. 

* Extra flags.
If the command has an argument `--output`or `-o` which receives a path to a directory where we should instead of presenting on the screen, dump the resultins in a txt file called results-{timestamp-iso}.txt.
Example: `python -m main --find-pair-id 0028S00066000000 --output /path/to/dir/`

If the command has a flag `--sale-summary` it should output on the console a JSON summary of how many sales for each `SALEDESC`.
Example:
```
{
    "VALID SALE": 23,
    "ESTATE SALE": 45
}
```

* Please provide unit tests for all you think is necessary to be tested. 

* The tests should be on a directory called `tests` and you should edit the this file [Instructions](Instructions) section to describe how to run them.
* All the code except for the `main.py` should be on the `src` directory.

Happy Coding!
