.PHONY: image
image: Dockerfile
	docker build -t hotoku/rstudio .


%: %.jinja
	../../lib/plist.py -e ../../.envrc $< > $@
