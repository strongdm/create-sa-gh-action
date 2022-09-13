#!/bin/bash

export OUTPUT=$(python /main.py)
echo "::set-output name=account-id::$(python -c "import os; print(os.getenv('OUTPUT').split(':')[0])")"
echo "::set-output name=temp-token::$(python -c "import os; print(os.getenv('OUTPUT').split(':')[1])")"
