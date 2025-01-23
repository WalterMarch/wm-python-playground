# Python

![xkcd Python comic](https://imgs.xkcd.com/comics/python.png)

Python is a hugely popular general purpose high-level language. I use it extensively at work. In particular, my team uses PySpark for data processing.

## File Extension

`.py`

## Execute

```bash
cd <path/to/file>
python <filename>.py
```

## configit.sh

This repository's *devcontainer.json* uses a `postCreateCommand` to run `configit.sh`.

This script uses information particular to the user of the repository.

```shell
#!/bin/bash

git config --global user.email "yourEmail@mail.com"
git config --global user.name "yourGitUserName"
git config --global push.autoSetupRemote true
git config --global push.default current
git config --global init.defaultBranch main
git config --global --add safe.directory $1
```
