#!/bin/bash

# GPIO Control with Raspberry Pi

GPIOPORT=$1

echo $GPIOPORT > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$GPIOPORT/direction
