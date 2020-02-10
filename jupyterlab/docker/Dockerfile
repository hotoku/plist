FROM python



RUN mkdir -p /root/build                                                              &&\
  cd /root/build                                                                      &&\
  wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0.tar.gz &&\
  tar xzvf cmake-3.16.0.tar.gz                                                        &&\
  cd cmake-3.16.0                                                                     &&\
  ./bootstrap --parallel=4                                                            &&\
  make -j4                                                                            &&\
  make install                                                                        &&\
  mkdir -p /root/work                                                                 &&\
  apt update                                                                          &&\
  apt-get install -y nodejs                                                           &&\
  apt-get install -y npm




RUN pip install Cython \
  folium               \
  geojson              \
  h3                   \
  jismesh              \
  jupyterlab           \
  jupyterlab-git       \
  lightgbm             \
  matplotlib           \
  nodejs               \
  numpy                \
  optuna               \
  pandas               \
  plotly               \
  pystan               \
  python-dateutil      \
  scikit-learn         \
  scipy                \
  seaborn              \
  statsmodels          \
  xgboost              \
  gensim             &&\
  jupyter labextension install @jupyterlab/toc &&\
  jupyter lab build                            &&\
  jupyter labextension install @jupyterlab/git &&\
  jupyter serverextension enable --py jupyterlab_git &&\
  pip install colormath




WORKDIR /root/work


COPY run-lab /usr/local/bin/run-lab
RUN chmod u+x /usr/local/bin/run-lab


ENTRYPOINT run-lab
