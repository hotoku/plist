.PHONY: all load unload clean

PLIST_NAME=info.hotoku.jupyterlab
EXE_NAME=run

all: load
	@echo making $@

clean: unload
	@echo making $@
	rm $(PLIST_NAME).plist || true
	rm $(EXE_NAME)

load: $(PLIST_NAME).plist unload permission
	@echo making $@
	cp -f $(PLIST_NAME).plist $(HOTOKU_PLIST_DESTPATH)
	launchctl load $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist

unload:
	@echo making $@
	launchctl unload $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true
	rm $(HOTOKU_PLIST_DESTPATH)/$(PLIST_NAME).plist || true

permission: $(EXE_NAME)
	chmod 755 $(EXE_NAME)

%: %.jinja render.py ../.envrc
	@echo making $@
	PYTHONPATH=../lib python render.py $< ../.envrc > $@
