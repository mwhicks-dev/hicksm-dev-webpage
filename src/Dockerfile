# start from python src
FROM python:3.10.13-bookworm

# set up working dir
RUN mkdir /tmp/api
WORKDIR /tmp/api

# install server code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run pyinstaller compile script and copy executeable to bin
RUN apt-get update && apt-get install dos2unix
RUN dos2unix compile.sh
RUN ./compile.sh api
RUN cp bin/api /bin/api

# remove src
WORKDIR /
RUN rm -r /tmp/api

# set up runtime
ENTRYPOINT api
