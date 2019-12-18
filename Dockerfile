# streamlit "Uber Pickups in NYC" demo, Docker build & run    # -*-conf-*-

# Reference: https://streamlit.io/docs/

# docker build -t streamlit_sirselim .
# docker run -it -p 8052:8052 --name demo-uber  streamlit_sirselim

FROM python:3.7-slim-stretch

ENV PROJECT /usr/src/app

# Where 'pipenv' installs Py packages & 'streamlit' script ($PYUB/bin)
ENV PYUB /usr/local

RUN mkdir -p $PROJECT
WORKDIR $PROJECT
COPY . $PROJECT

# Install requirements
RUN pip install --no-cache-dir pipenv

RUN PIP_USER=1 PYTHONUSERBASE=$PYUB  pipenv install --clear --verbose --system --deploy

# set-up 'streamlit' user
RUN mkdir $HOME/.streamlit
COPY config/*.toml $HOME/.streamlit/

EXPOSE 8051
CMD ["streamlit", "run", "demo-uber-nyc-pickups-app.py"]
