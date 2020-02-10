.PHONY: all load docker unload

PLIST_NAME=info.hotoku.jupyterlab


all: load

load: $(PLIST_NAME).plist docker
	cp -f $(PLIST_NAME).plist $(HOTOKU_PLIST_DESTPATH)
	launchctl load $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist

docker: unload
	make -C docker

unload:
	launchctl unload $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true
	rm $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true

%.plist: %.py %.jinja.plist
	python $< > $@
