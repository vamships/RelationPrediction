#!/usr/bin/env bash

DATASET="FB-Toutanova"
SETTINGS=$1

SCRIPT_DIR="`pwd`"

TRAIN_PATH=$SCRIPT_DIR"/code/train.py"
DATASET_PATH=$SCRIPT_DIR"/data/"$DATASET
SETTINGS_PATH=$SCRIPT_DIR"/"$SETTINGS

ARGUMENT_STRING="--settings "$SETTINGS_PATH" --dataset "$DATASET_PATH

python -u $TRAIN_PATH $ARGUMENT_STRING

