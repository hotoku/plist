.PHONY: image
image: Dockerfile
	docker build -t $(IMAGE_NAME):$(HOTOKU_PLIST_RSTUDIO_IMAGE_TAG) .


%: %.jinja
	../../lib/plist.py -e ../../.envrc $< > $@

clean:
	rm -f Dockerfile
