.PHONY: all image rebuild load unload clean


all: image

image: pull
	docker build -t $(HOTOKU_PLIST_JUPYTERLAB_IMAGE_NAME) .

pull:
	docker pull $(HOTOKU_PLIST_JUPYTERLAB_IMAGE_NAME)

rebuild:
	docker build --no-cache -t $(HOTOKU_PLIST_JUPYTERLAB_IMAGE_NAME) .

stop: 
	docker stop plist-jupyter || true
