FROM python:3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev
RUN pip install h5py
RUN pip install tensorflow

WORKDIR /home/gradbench
COPY tools/tensorflow/tensor_functions.py .
COPY tools/tensorflow/tensor_run.py .
ENTRYPOINT ["python", "/home/gradbench/tensor_run.py"]
LABEL org.opencontainers.image.source https://github.com/gradbench/gradbench
