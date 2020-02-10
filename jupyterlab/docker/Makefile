.PHONY: all image rebuild load unload clean

PLIST_NAME=info.hotoku.jupyterlab
PLIST_DIR=~/Library/LaunchAgents

all: load

load: $(PLIST_NAME).plist image stop
	cp -f $(PLIST_NAME).plist $(PLIST_DIR) && \
		cd $(PLIST_DIR)                   && \
		launchctl load $(PLIST_NAME).plist

image: unload
	docker build -t hotoku/python .

rebuild: unload
	docker build --no-cache -t hotoku/python .

clean: unload
	cd $(PLIST_DIR) && \
		rm $(PLIST_NAME).plist

unload: stop
	cd $(PLIST_DIR)                   && \
		launchctl unload $(PLIST_NAME).plist

stop: 
	docker stop plist-jupyter || true

