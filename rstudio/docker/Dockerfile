FROM rocker/tidyverse:3.6.1

ENV TZ JST-9

RUN \
  sudo apt-get install libcairo2-dev && \
  yes Y | sudo apt-get install libxt-dev && \
  apt install fonts-noto-cjk && \
  install2.r -n4 --error --deps TRUE \
    -r https://cran.r-project.org/ \
    ConfigParser \
    rstan \
    shiny \
    future \
    promises \
    loggit \
    ggmcmc \
    future \
    shinydashboard

RUN \
  install2.r -n4 --error --deps TRUE \
    -r https://cran.r-project.org/ \
    logging

RUN install2.r --error --deps TRUE shiny future promises
RUN install2.r --error loggit
RUN install2.r --error ggmcmc
RUN install2.r --error future
RUN install2.r --error shinydashboard

RUN \
  install2.r -n4 --error --deps TRUE \
    -r https://cran.r-project.org/ \
    tidybayes

RUN \
  yes Y | apt-get install libc6-dev-i386 && \
  wget -O OpenBUGS-3.2.3.tar.gz "http://www.openbugs.net/w/OpenBUGS_3_2_3?action=AttachFile&do=get&target=OpenBUGS-3.2.3.tar.gz" && \
  tar xzvf OpenBUGS-3.2.3.tar.gz && \
  cd OpenBUGS-3.2.3 && \
  ./configure && \
  make && make install && \
  install2.r -n4 --error --deps TRUE \
  -r https://cran.r-project.org/ \
  BRugs coda R2OpenBUGS Rcpp
