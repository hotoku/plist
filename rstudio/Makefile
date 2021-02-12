.PHONY: all load docker unload clean


PLIST_NAME := info.hotoku.rstudio
subdirs := docker
IMAGE_NAME := hotoku/rstudio

all: load $(subdirs)

$(subdirs):
	@echo building $@
	$(MAKE) IMAGE_NAME=$(IMAGE_NAME) -C $@

clean: unload
	rm  $(PLIST_NAME).plist || true
	for d in $(subdirs); do $(MAKE) -C $$d clean; done

load: $(PLIST_NAME).plist unload
	cp -f $(PLIST_NAME).plist $(HOTOKU_PLIST_DESTPATH)
	launchctl load $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist

unload: stop
	launchctl unload $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true
	rm $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true

stop:
	docker stop $(HOTOKU_PLIST_RSTUDIO_CONTAINER_NAME) || true

$(PLIST_NAME).plist: $(PLIST_NAME).plist.jinja
	../lib/plist.py -e ../.envrc -D IMAGE_NAME=$(IMAGE_NAME) $< > $@
