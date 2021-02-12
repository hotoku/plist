.PHONY: all load docker unload clean

PLIST_NAME := info.hotoku.rstudio
subdirs := docker

all: load $(subdirs)

$(subdirs):
	@echo building $@
	$(MAKE) -C $@

clean: unload
	rm  $(PLIST_NAME).plist || true

load: $(PLIST_NAME).plist unload
	cp -f $(PLIST_NAME).plist $(HOTOKU_PLIST_DESTPATH)
	launchctl load $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist

unload: stop
	launchctl unload $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true
	rm $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true

stop:
	docker stop $(HOTOKU_PLIST_RSTUDIO_CONTAINER_NAME) || true

%.plist: %.jinja.plist
	../lib/plist.py -e ../.envrc $< > $@
