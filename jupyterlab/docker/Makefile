.PHONY: all image rebuild load unload clean


all: image

image:
	docker build -t hotoku/python .

rebuild:
	docker build --no-cache -t hotoku/python .

stop: 
	docker stop plist-jupyter || true

