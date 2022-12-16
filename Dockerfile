FROM --platform=arm64 python:3.9-slim-buster 
LABEL Author=kirklimushin@gmail.com 

WORKDIR /project/dir/ 
COPY . .

RUN echo "Upgrading the PIP Version of the Application..."
RUN pip install --upgrade pip 

RUN echo "Freezing the Project Dependencies into the File"
RUN pip freeze > requirements.txt 
ADD ./requirements.txt ./requirements.txt

RUN echo "Installing the Dependencies into the Project Container"
RUN pip install -r requirements.txt 

RUN echo "Running the Shell Script..."
ENTRYPOINT ["sh", "entrypoint.sh"]