#!/bin/bash -eux

# Usage: adduser-jupyter.sh username
#
#     Adds a user to the jupyterusers group.
#     Creates the jupyterusers if it doesn't exist already.

# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
thisdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

username=$1

jupyter_user_group=jupyterusers
getent group ${jupyter_user_group} || groupadd ${jupyter_user_group}

${thisdir}/adduser.sh ${username} -G ${jupyter_user_group}
