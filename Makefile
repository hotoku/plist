subdirs := jupyterlab

.PHONY: all $(subdirs)
PWD := $(shell pwd)

all: $(subdirs)
$(subdirs):
	@echo building $@
	$(MAKE) PYTHONPATH=$(PWD)/lib -C $@
