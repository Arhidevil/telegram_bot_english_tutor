#!/bin/sh
new_tag=$1
project_id=exploring-ml-in-education

echo "Start building testbot:${new_tag}"
docker build -t testbot:$new_tag .
echo "Build finished"

docker tag testbot:$new_tag europe-central2-docker.pkg.dev/${project_id}/english-bot-tutor/testbot:$new_tag
echo "Added tag testbot:${new_tag}"

echo "Push started: europe-central2-docker.pkg.dev/${project_id}/english-bot-tutor/testbot:${new_tag}"
docker push europe-central2-docker.pkg.dev/${project_id}/english-bot-tutor/testbot:$new_tag
echo "Push finished"
