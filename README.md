## streamlit "Uber Pickups in NYC" demo

### Reference(s)

* See  https://streamlit.io/docs/

* Example of *streamlit* run, on Youtube: https://youtu.be/B2iAodr0fOo


### Docker: building

```shell
docker build -t streamlit_sirselim .
```

### Docker: running

```shell
docker run -it -p 8052:8052 --name demo-uber  streamlit_sirselim

# OR
docker run -d -p 8052:8052 --name demo-uber  streamlit_sirselim
docker logs demo-uber

xdg-open http://172.17.0.2:8501/  # browse to "Network URL", in log-output

```
