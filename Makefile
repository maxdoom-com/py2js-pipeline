PYOBJS=$(wildcard *.py)
JSOBJS=$(patsubst %.py, %.js, $(PYOBJS))
MINJSOBJS=$(patsubst %.py, %.min.js, $(PYOBJS))

.SUFFIXES:

.SUFFIXES:
%.js: %.py
	./py2js compile $<
%.min.js: %.js
	./py2js minimize $<

all: $(JSOBJS) $(MINJSOBJS)

whenevery-something-changes:
	bash -c 'while :; do inotifywait *.py; make all; done'

re: clean all

clean:
	rm -f $(JSOBJS) $(MINJSOBJS)
