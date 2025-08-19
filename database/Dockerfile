FROM postgres:latest

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=whitehorse-db

ADD init.sh /docker-entrypoint-initdb.d/
ADD ./statements /docker-entrypoint-initdb.d/