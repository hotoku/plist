subdirs := jupyterlab rstudio
R_VERSION := 4.0.3
RSTUDIO_VERSION := 1.3.1093
export RSTUDIO_TAG := $(R_VERSION)_$(RSTUDIO_VERSION)


.PHONY: all $(subdirs)


all: $(subdirs)


$(subdirs):
	@echo building $@
	$(MAKE) PYTHONPATH=$(shell pwd)/lib -C $@


clean:
	for d in $(subdirs); do $(MAKE) -C $$d clean; done
