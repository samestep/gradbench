FROM python:3.11-slim
RUN pip install numpy
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
WORKDIR /home/gradbench
COPY tools/pytorch/functions.py .
COPY tools/pytorch/run.py .
ENTRYPOINT ["python", "/home/gradbench/run.py"]
LABEL org.opencontainers.image.source https://github.com/gradbench/gradbench
