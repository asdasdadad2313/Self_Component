#!/usr/bin/env bash

source "$(dirname ${BASH_SOURCE[0]})/utils.sh"

PGDATABASE=test_db

ensure "build image"  /home/linhanqiu/anaconda3/bin/docker-compose build server
ensure "kill server "  /home/linhanqiu/anaconda3/bin/docker-compose kill server
ensure "rm server "  /home/linhanqiu/anaconda3/bin/docker-compose rm -f server
ensure "setup service"  /home/linhanqiu/anaconda3/bin/docker-compose up -d server db
waituntil 10 "connect postgres"  /home/linhanqiu/anaconda3/bin/docker-compose exec db pg_isready
/home/linhanqiu/anaconda3/bin/docker-compose exec db dropdb ${PGDATABASE} -U postgres
ensure "create db"  /home/linhanqiu/anaconda3/bin/docker-compose exec db createdb ${PGDATABASE} -U postgres
ensure "init db"  /home/linhanqiu/anaconda3/bin/docker-compose run --rm -e dbname=${PGDATABASE} server python -m service.migrations
ensure "running coverage erase"  /home/linhanqiu/anaconda3/bin/docker-compose run --rm -e dbname=${PGDATABASE} server coverage erase
ensure "running coverage run"  /home/linhanqiu/anaconda3/bin/docker-compose run --rm -e dbname=${PGDATABASE} server coverage run --source service -m ethicall_common service.tests
ensure "running coverage xml"  /home/linhanqiu/anaconda3/bin/docker-compose run --rm -e dbname=${PGDATABASE} server coverage xml -o reports/coverage.xml
ensure "running coverage2clover"  /home/linhanqiu/anaconda3/bin/docker-compose run --rm -e dbname=${PGDATABASE} server coverage2clover -i reports/coverage.xml -o reports/clover.xml
ensure "running coverage html"  /home/linhanqiu/anaconda3/bin/docker-compose run --rm -e dbname=${PGDATABASE} server coverage html -d reports
