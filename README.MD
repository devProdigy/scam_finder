# Scam finder - tool to find scam-like texts

## Table of content
  - [About](#about)
  - [Installation guide](#installation-guide)
    - [Preparation step](#preparation-step)
    - [Install poetry](#install-poetry)
    - [Install dependencies](#install-dependencies)
  - [How to run](#how-to-run)
  - [TODOs](#todos)

## About
This app tries to find scam-like text from the difference sources of the input.
App looks for first scam-like "match" among finders. 

For now only `.csv` files and `console` are supported as input/output.  
To add more - simply implement additional input/output classes and 
add them to the factory.  

App uses following `scam-finders`:
- bot finder (looks for Telegram-like bots mentioning in text);
- bank cards finder (works with most of the possible combination of 16 and 19
  numbers cards and any symbols between them);
- fake domain finder (looks for attempt to fake some domains with sensitive data
  via subdomains);
- words finder (looks for forbidden words/phrases that most likely that are 
  used for scams).

You can add any needed finders without code changing, only implementing new 
finder and adding it to the factory is required.

## Installation guide

### Preparation step
If you  have more then one Python version in your system -for your convenience 
you can create `.python-version` with `3.10.5` or higher version.  

Some env variables are required before running the app.
You can create `.env` file with following variables 
(it'll be automatically picked up by the app):
```text
INPUT_TYPE=csv
# OR
# INPUT_TYPE=console

# bot names that will be ignored on scam search.
ALLOWED_BOT_NAMES=["MyBot", "OtherBot"]
# domains that will be checked for possible scam.
DOMAINS_USUALLY_FAKED=["bank1", "bank2"]
# words that will be considered as scam-like.
FORBIDDEN_WORDS=["bad word", "forbidden phrase"]

# Logger section
DAYS_TILL_NEW_LOG_FILE=1
BACKUP_LOGS_AMOUNT=7
```

### Install poetry
This project uses [poetry](https://python-poetry.org/) for packages management.  

You need to install it only once.  
The simplest way to install [poetry](https://python-poetry.org/) 
with the officially recommended way:
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

(Or check out alternative instructions for `poetry` installation 
[here](https://python-poetry.org/docs/#installation))

### Install dependencies
Execute in terminal: 
```shell
poetry install
```

## How to run
Choose needed `INPUT_TYPE` in `.env` file and run `main.py`.  
Supported `INPUT_TYPE`:
- `csv`;
- `console`.

If `INPUT_TYPE=csv`: add `.csv` file with one column of text-data with no header 
to the `input` directory. Text in that file will be used for scam finding.
Result will be written to the `output` directory.

## TODOs
- add more tests.
