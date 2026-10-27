# Coverage for Existing Codebase

Another quick _Lunch & Learn_ topic: **how to introduce test coverage for an existing codebase**!

This is a fiddly one to demo, as it will require the user to check out various commits.

Imagine the first commit in this repository to be the initial, inherited codebase that has a small amount of unit tests already.

## Getting Started

1. Create your virtual environment:

    ```shell
    python -m venv .venv
    source ./.venv/Scripts/activate
    ```

1. Install libraries

    ```shell
    pip install --requirement requirements.txt
    ```

1. Run the app

    ```shell
    python ./app/main.py
    ```

1. Run the tests (and view the coverage)

    ```shell
    pytest
    ```

## Initial Coverage

Results from running coverage (well, `pytest-cov`):

```text
Name                     Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------
app\ghouls\__init__.py       3      3      0      0     0%
app\ghouls\base.py          22     22      0      0     0%
app\ghouls\ghost.py          6      6      0      0     0%
app\ghouls\zombie.py        11     11      0      0     0%
app\main.py                  9      9      2      0     0%
app\utils.py                 4      1      0      0    75%
----------------------------------------------------------
TOTAL                       55     52      2      0     5%
```

5% test coverage isn't much 😒.
