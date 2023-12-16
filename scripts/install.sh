#!/bin/bash

MYSQL=mysql-dbapis-dai
POSTGRES=pg-dbapis-dai

sudo docker stop $POSTGRES &>/dev/null
sudo docker rm -f $POSTGRES &>/dev/null
sudo docker volume rm -f $POSTGRES &>/dev/null

sudo docker stop $MYSQL &>/dev/null
sudo docker rm -f $MYSQL &>/dev/null
sudo docker volume rm -f $MYSQL &>/dev/null

sudo docker run -d -p 5432:5432 \
 	--name $POSTGRES \
	-e POSTGRES_PASSWORD=admin \
	--mount src=$POSTGRES,dst=/var/lib/postgresql/data \
	postgres

until sudo docker exec $POSTGRES pg_isready &>/dev/null; do
    echo 'Waiting for PostgreSQL to be ready...'
    sleep 5
done

sudo docker exec -i $POSTGRES psql -h localhost -U postgres < sql/html.pg.sql &>/dev/null

sudo docker run -d -p 3306:3306 \
	--name $MYSQL \
	-e MYSQL_ROOT_PASSWORD=admin \
	--mount src=$MYSQL,dst=/var/lib/mysql \
	mysql

until sudo docker exec $MYSQL mysql -padmin -e "SELECT 1" &>/dev/null; do
	echo 'Waiting for MySQL to be ready...'
	sleep 5
done

sudo docker exec -i $MYSQL mysql -padmin < sql/html.mysql.sql
