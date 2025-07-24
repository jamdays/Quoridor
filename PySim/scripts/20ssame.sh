#!/bin/bash

cd /h/u13/c3/01/djayamax/Documents/Quoridor/PySim
{ echo "n";
 echo 8;
 echo y;
 echo "logs/20ssame/log$1"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .5;
 echo p;
 echo p;
 echo 20;
 echo 20;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py
