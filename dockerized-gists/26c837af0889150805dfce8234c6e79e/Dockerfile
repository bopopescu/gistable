FROM python:2.7.13
ADD snippet.py snippet.py
RUN ["pip", "install", "os"]
RUN ["pip", "install", "googlemaps"]
CMD ["python", "snippet.py"]