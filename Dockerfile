FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash newuser
USER newuser
ENV PATH=/home/newuser/.local/bin:$PATH
WORKDIR /home/newuser/code
COPY requirements.txt /home/newuser/code/
COPY .env.tpl /home/newuser/code/.env
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3.9 install --user -r /home/newuser/code/requirements.txt
COPY . /home/newuser/code/
