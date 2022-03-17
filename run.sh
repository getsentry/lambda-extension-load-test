#!/usr/bin/env bash

# exit on first error
set -e

echo "Creating virtual env ..."
python -m venv .venv
source .venv/bin/activate

echo "Installing requirements ..."
pip install -r requirements.txt

echo "Running locust ..."
locust
