FROM python:2.7
COPY . /app
WORKDIR /app
ENV http_proxy  http://165.225.104.32:10223
ENV https_proxy http://165.225.104.32:10223
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["welcome.py"]
~                         
