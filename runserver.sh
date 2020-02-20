#!/bin/sh

while true;
do
    rc=`nc -z ${DB_HOST} 5432 &> /dev/null; echo $?`

    if [[ ${rc} -eq 0 ]];
    then
        echo "PostgresDB available!"
        break
    fi

    echo "Waiting PostgresDB... Status is ${rc}"
    sleep 2
done

#python manage.py flush --noinput
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py create_superuser
#python manage.py fill_menu /var/app/fill/Pizza -rus True

python manage.py runserver 0.0.0.0:${PORT}
