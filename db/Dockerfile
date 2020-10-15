FROM mysql

COPY /init /docker-entrypoint-initdb.d/

RUN mysql -u MYSQL_USER -p MYSQL_ROOT_PASSWORD