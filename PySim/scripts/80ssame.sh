#!/bin/bash

cd /h/u13/c3/01/djayamax/Documents/Quoridor/PySim
{ echo "n";
 echo 2;
 echo y;
 echo "logs/80ssame/log$1"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .5;
 echo p;
 echo p;
 echo 80;
 echo 80;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py
