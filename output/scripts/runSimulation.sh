#!/bin/bash
ALGO="0"
make run ARGS="20 $ALGO"
make run ARGS="50 $ALGO"
make run ARGS="100 $ALGO"
ALGO="1"
make run ARGS="20 $ALGO"
make run ARGS="50 $ALGO"
make run ARGS="100 $ALGO"
ALGO="2"
make run ARGS="20 $ALGO"
make run ARGS="50 $ALGO"
make run ARGS="100 $ALGO"
echo -e "\a"
echo -e "\a"
echo -e "\a"


