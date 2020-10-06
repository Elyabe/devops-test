#!/bin/bash

# Parse env vars

fromDt="01-03-2011"
toDt="01-10-2019"
endpoint="http://localhost:5000/sales-gender?fromDt=${fromDt}&toDt=${toDt}"

if [ -f .env ]
then
    export $(cat .env | sed 's/#.*//g' | xargs)

    echo "**RESTORING DATABASE**"

    # docker exec -i "${CONTAINER_DB}" pg_restore --no-owner -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" < "${LOCAL_DUMP_PATH}"

    echo "**DATABASE RESTORED**"
    
    echo "${endpoint}"
fi




curl -s $endpoint -o "gender-${fromDt}-to-${toDt}.png"

