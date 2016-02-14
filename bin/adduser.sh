#!/bin/bash -eux

# Usage: adduser.sh username --any --extra --args

username=$1
echo "Creating ${username}" >>/var/log/mkuser

shift

getent group ${username} || groupadd ${username}
id -u ${username} &>/dev/null || useradd ${username} \
   -m \
   -s /bin/bash \
   -g ${username} \
   "${@}"
