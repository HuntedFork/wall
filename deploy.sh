#!/bin/bash
# Used to set the page branch for deployment
# Run this and push to deploy the site
set -e

DEPLOY_DIR="docs"
BUILD_DIR="website/build"

rm -rf ./docs

mv website/build ./docs

