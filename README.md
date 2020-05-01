My Python to Javascript rendering pipeline
==========================================

Installation
------------

```sh
python3 -m venv env
env/bin/pip install pscript jsmin fire
env/bin/pip install git+https://github.com/maxdoom-com/tinypreprocessor
```

Usage
-----

```sh
make # makes all

make whenevery-something-changes # will wait for changes to the *.py - files and `make all` then

make clean # cleans up
make re # make clean all
```

Requirements
------------

Install `inotify-tools` for using `make whenevery-something-changes`.
