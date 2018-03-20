#!/usr/bin/env bash

source "$(dirname ${BASH_SOURCE[0]})/utils.sh"

ensure ">>> killing existing services" /home/linhanqiu/anaconda3/bin/docker-compose kill db server
ensure ">>> removing existing services" /home/linhanqiu/anaconda3/bin/docker-compose rm -f -v

if [ -n "${BUILD}" ]
then
    ensure "building services" /home/linhanqiu/anaconda3/bin/docker-compose build
fi

if [ -n "${PULL}" ]
then
    ensure "pulling images" /home/linhanqiu/anaconda3/bin/docker-compose pull
fi

PGDATABASE=postgres
export PGDATABASE
ensure ">>> starting db" /home/linhanqiu/anaconda3/bin/docker-compose up -d db
waituntil 10 ">>> connect postgres" /home/linhanqiu/anaconda3/bin/docker-compose exec db pg_isready
ensure ">>> starting services" /home/linhanqiu/anaconda3/bin/docker-compose up -d
ensure ">>> create tables" /home/linhanqiu/anaconda3/bin/docker-compose run --rm server python -m migrations
