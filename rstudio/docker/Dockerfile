FROM rocker/tidyverse:3.6.1

ENV TZ JST-9

RUN \
  yes Y | sudo apt-get install \
    libxt-dev  \
    libcairo2-dev \
    fonts-noto-cjk \
    libc6-dev-i386 && \
  wget -O OpenBUGS-3.2.3.tar.gz "http://www.openbugs.net/w/OpenBUGS_3_2_3?action=AttachFile&do=get&target=OpenBUGS-3.2.3.tar.gz" && \
  tar xzvf OpenBUGS-3.2.3.tar.gz && \
  cd OpenBUGS-3.2.3 && \
  ./configure && \
  make -j4 && make -j4 install && \
  install2.r -n4 --error --deps TRUE \
    -r https://cran.r-project.org/ \
    BRugs \
    ConfigParser \
    R2OpenBUGS \
    Rcpp \
    coda \
    future \
    ggmcmc \
    logging \
    loggit \
    promises \
    rstan \
    shiny \
    shinydashboard \
    tidybayes
