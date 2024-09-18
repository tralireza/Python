# DS & Algorithms in Python

## Run
```bash
$ pytest -rP -v dp_test.py -k 322

============================= test session starts ==============================
platform darwin -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0 -- /Users/alireza/python/Code/.venv/bin/python3.12
cachedir: .pytest_cache
rootdir: /Users/alireza/python/Code
configfile: pyproject.toml
collecting ... collected 5 items / 4 deselected / 1 selected

dp_test.py::test_Solution322 PASSED                                      [100%]

==================================== PASSES ====================================
_______________________________ test_Solution322 _______________________________
----------------------------- Captured stdout call -----------------------------
11? [1, 2, 5] -> [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
3? [2] -> [0, inf, 1, inf]
0? [1] -> [0]
======================= 1 passed, 4 deselected in 0.03s ========================
```

## Setup
```bash
$ python -m venv .venv
$ pip install -r requirements.txt
```
