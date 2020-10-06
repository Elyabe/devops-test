#!/bin/bash


OPTION=$1

# Parse env vars
fromDt="01-03-2019"
toDt="01-10-2019"
endpoint="http://localhost:5000/sales-gender?fromDt=${fromDt}&toDt=${toDt}"

case $OPTION in 
init)
    if [ -f .env ]
    then
        export $(cat .env | sed 's/#.*//g' | xargs)

        echo "**RESTORING DATABASE**"

        docker exec -i "${CONTAINER_DB}" pg_restore --no-owner -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" < "${LOCAL_DUMP_PATH}"

        echo "**DATABASE RESTORED**"
        
    fi
;;
test)
    echo "${endpoint}"
    curl -s $endpoint -o "gender-${fromDt}-to-${toDt}.png"
    echo "saved image in local directory"
;;
*)
    echo "option not informed"
esac