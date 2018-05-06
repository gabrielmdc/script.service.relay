#!/usr/bin/env bash
# Execute this script as superuser

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -d "/usr/lib/gcr-server" ]; then
    cp -r ${DIR}/. /usr/lib/gcr-server
else
    cp -r ${DIR} /usr/lib/gcr-server
fi

cp /usr/lib/gcr-server/gcr-server.service /etc/systemd/system/
systemctl daemon-reload
systemctl start gcr-server
systemctl status gcr-server
echo "Installation done!"