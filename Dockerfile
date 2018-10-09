FROM python:3-alpine

# Build information
ARG GIT_OWNER
LABEL git_owner=$GIT_OWNER
ENV GIT_OWNER=$GIT_OWNER

ARG GIT_REPO
LABEL git_repo=$GIT_REPO
ENV GIT_REPO=$GIT_REPO

ARG GIT_BRANCH
LABEL git_branch=$GIT_BRANCH
ENV GIT_BRANCH=$GIT_BRANCH

ARG GIT_COMMIT
LABEL git_commit=$GIT_COMMIT
ENV GIT_COMMIT=$GIT_COMMIT

ARG BUILD_TIME
LABEL build_time=$BUILD_TIME
ENV BUILD_TIME=$BUILD_TIME

ARG CCS_VERSION
LABEL ccs_version=$CCS_VERSION
ENV CCS_VERSION=$CCS_VERSION

##_PARAMETER_STORE_MARKER_##

# Update and install base packages
RUN apk update && apk upgrade && apk add build-base linux-headers

# Create app directory
WORKDIR /usr/src/app

RUN pip install -U pip flask psutil

COPY . .

EXPOSE 8080

ENV FLASK_APP ccsexampleapi2/main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]