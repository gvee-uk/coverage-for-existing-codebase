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

## Extending the Existing Code

This codebase is now ~~our problem~~ ours to own! 🎉

How are we going to handle test coverage going forward?

### Make Coverage Drop Cause Failure

Coverage (via the `pytest-cov` plugin) has a `--fail-under` option 👀

Why don't we just set our coverage to fail if it drops under 5% and be done with it?

GOTO [.coveragerc](.coveragerc)...

#### Updated Coverage

We get a wee bit more output now:

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

1 empty file skipped.
Coverage XML written to file coverage.xml
Required test coverage of 5.0% reached. Total coverage: 5.26%
```

#### Pros & Cons

The biggest plus is that this is super easy to add: only one config option is required! 🥳

Unfortunately it hides some gotchas that are important to be aware of which centre around the fact that adopting an existing tide-line leaves gaps... 🥸

For example: coverage goes up when I delete a file!

```shell
rm -f ./app/main.py
pytest
```

Results in:

```text
Name                     Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------
app\ghouls\__init__.py       3      3      0      0     0%
app\ghouls\base.py          22     22      0      0     0%
app\ghouls\ghost.py          6      6      0      0     0%
app\ghouls\zombie.py        11     11      0      0     0%
app\utils.py                 4      1      0      0    75%
----------------------------------------------------------
TOTAL                       46     43      0      0     7%

1 empty file skipped.
Coverage XML written to file coverage.xml
Required test coverage of 5.0% reached. Total coverage: 6.52%
```

Which leaves room for me to add some code that doesn't "require" tests...

```shell
rm -f ./app/new_code.py
touch ./app/new_code.py
for i in $(seq 1 7);
do
    echo -e "def untested_$i():\n    return $i\n\n" >> ./app/new_code.py
done
pytest
```

Results:

```text
Name                     Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------
app\__init__.py              0      0      0      0   100%
app\ghouls\__init__.py       3      3      0      0     0%
app\ghouls\base.py          22     22      0      0     0%
app\ghouls\ghost.py          6      6      0      0     0%
app\ghouls\zombie.py        11     11      0      0     0%
app\new_code.py             14     14      0      0     0%
app\utils.py                 4      1      0      0    75%
----------------------------------------------------------
TOTAL                       60     57      0      0     5%
Coverage XML written to file coverage.xml
Required test coverage of 5.0% reached. Total coverage: 5.00%
```

That's after adding 14 new lines of code without any tests 🤬
