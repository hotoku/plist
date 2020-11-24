.PHONY: all image rebuild stop push


all: image


image: Dockerfile
	docker build -t $(HOTOKU_PLIST_RSTUDIO_IMAGE_NAME):$(RSTUDIO_TAG) .


rebuild:
	docker build --no-cache -t $(HOTOKU_PLIST_RSTUDIO_IMAGE_NAME) .


stop:
	docker stop plist-jupyter || true


push:
	docker push $(HOTOKU_PLIST_RSTUDIO_IMAGE_NAME)


%: %.jinja
	jinja2 -D RSTUDIO_TAG=$(RSTUDIO_TAG) $< > $@
