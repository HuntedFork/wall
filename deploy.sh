#!/bin/bash
# Used to set the page branch for deployment
set -e

DEPLOY_BRANCH="gh-pages"
BUILD_DIR="./website/build"

# Ensure the build directory exists
if [ ! -d "$BUILD_DIR" ]; then
  echo "Error: Build directory '$BUILD_DIR' does not exist."
  exit 1
fi

# Delete the existing deploy branch if it exists locally
git branch -D $DEPLOY_BRANCH 2>/dev/null || true

# Create a new branch from the build directory
git subtree split --prefix $BUILD_DIR -b $DEPLOY_BRANCH

echo "Branch '$DEPLOY_BRANCH' now contains only the contents of '$BUILD_DIR'."
