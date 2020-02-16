.PHONY: all image rebuild stop push


all: image

image:
	docker build -t $(HOTOKU_PLIST_RSTUDIO_IMAGE_NAME) .

rebuild:
	docker build --no-cache -t $(HOTOKU_PLIST_RSTUDIO_IMAGE_NAME) .

stop: 
	docker stop plist-jupyter || true

push:
	docker push $(HOTOKU_PLIST_RSTUDIO_IMAGE_NAME)
