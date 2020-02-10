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
