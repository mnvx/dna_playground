PATH_THIS:=$(realpath $(dir $(lastword ${MAKEFILE_LIST})))

help:
	@echo "    install"
	@echo "        Initialise virtualenv with dev requirements"
	@echo "    execute"
	@echo "        Run command. Example: make execute command=\"skew_gc.py\""
	@echo "    watch"
	@echo "        Run command with hot reload. Example: make watch command=\"skew_gc.py\""
	@echo ""
	@echo "    Examples:"
	@echo "    ---------"
	@echo "    Run with hot reload"
	@echo "        make watch command=\"skew_gc.py\""

.PHONY: install
install:
	python3 -m venv venv
	PYTHONPATH=$$PYTHONPATH:`realpath $(PATH_THIS)` \
	&& printf '#!/bin/bash\n%s/venv/bin/pip3 "$$@"' $(PATH_THIS) > $(PATH_THIS)/pip3 \
	&& printf '#!/bin/bash\n%s/venv/bin/python3 "$$@"' $(PATH_THIS) > $(PATH_THIS)/python3 \
	&& chmod +x $(PATH_THIS)/pip3 \
	&& chmod +x $(PATH_THIS)/python3 \
	&& $(PATH_THIS)/pip3 install --upgrade pip \
	&& $(PATH_THIS)/pip3 install -Ur $(PATH_THIS)/requirements.txt


.PHONY: execute
execute:
	PYTHONPATH=$$PYTHONPATH:`realpath $(PATH_THIS)` \
	&& export PYTHONPATH \
	&& $(PATH_THIS)/python3 $(command)

.PHONY: watch
watch:
	$(PATH_THIS)/venv/bin/watchmedo auto-restart -p '*.py' --recursive -- \
	make execute command=$(command)
