subdirs := jupyterlab rstudio
R_VERSION := 3.6.3
RSTUDIO_VERSION := 1.3.1093
export RSTUDIO_TAG := $(R_VERSION)_$(RSTUDIO_VERSION)


.PHONY: all $(subdirs) rstudio-image tidyverse-image


all: $(subdirs)


rstudio: tidyverse-image


$(subdirs):
	@echo building $@
	$(MAKE) PYTHONPATH=$(shell pwd)/lib -C $@


clean:
	for d in $(subdirs); do $(MAKE) -C $$d clean; done


rstudio-image:
	cd rocker-versioned/rstudio &&\
    docker build -t hotoku/rstudio:${RSTUDIO_TAG} -f $(R_VERSION).Dockerfile --build-arg RSTUDIO_VERSION=$(RSTUDIO_VERSION) .


tidyverse-image: rstudio-image
	rm -rf temp
	mkdir temp
	cat rocker-versioned/tidyverse/3.6.3.Dockerfile | awk 'NR==1{print "FROM hotoku/rstudio:$(RSTUDIO_TAG)"} NR>1{print $0}' > temp/Dockerfile
	cd temp && docker build -t hotoku/tidyverse:$(RSTUDIO_TAG) .
