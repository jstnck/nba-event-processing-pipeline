#!/bin/bash

sudo chown -R think:think pgadmin-vol

current_time=$(date "+%Y.%m.%d-%H.%M")
filename=pgadmin-backup

# note to maybe not include the /sessions folder in the archive
# do we only need /storage and pgadmin4.db ?
tar -czvf ./archive/${filename}-${current_time}.tar.gz pgadmin-vol

sudo chown -R 5050:5050 pgadmin-vol