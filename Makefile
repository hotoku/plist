subdirs := jupyterlab

.PHONY: all $(subdirs)

all: $(subdirs)
$(subdirs):
	@echo building $@
	$(MAKE) -C $@
