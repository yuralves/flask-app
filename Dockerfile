FROM python:3.8.5 as build

# Before Build Dependencies
ENV PYTHONUNBUFFERED=1

WORKDIR /opt

COPY requirements.txt /opt
RUN pip install -r requirements.txt
COPY . /opt

# After Build
FROM build
WORKDIR /opt

EXPOSE 5000
RUN chmod +x ./run.sh
CMD ["./run.sh"]
