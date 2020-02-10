subdirs := jupyterlab rstudio

.PHONY: all $(subdirs)

all: $(subdirs)
$(subdirs):
	@echo building $@
	$(MAKE) PYTHONPATH=$(shell pwd)/lib -C $@

clean:
	for d in $(subdirs); do $(MAKE) -C $$d clean; done
