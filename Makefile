default:
	echo "No default rule; read Makefile"

.PHONY: run
run:
	vagrant up

.PHONY: clean
clean:
	rm -Rf run
	find . -name '*~' -and -print0 |xargs -0 rm -f

.PHONY:
distclean: clean
	vagrant destroy --force
	rm -Rf .cache .vagant
