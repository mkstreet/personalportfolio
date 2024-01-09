#!/bin/bash

# Check for untracked and modified files
if git status --porcelain | grep -qE '^\?\?|^ M '; then
    echo "There are modified files that are not added or committed."
fi
