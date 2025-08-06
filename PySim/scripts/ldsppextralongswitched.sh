#!/bin/bash

cd /h/u13/c3/01/djayamax/Documents/Quoridor/PySim
{ echo "n";
 echo 2;
 echo y;
 echo "logs/ldsppextralongswitched/log$1"
 echo y;
 echo .9;
 echo .9;
 echo .1;
 echo .9;
 echo p;
 echo p;
 echo 100;
 echo 100;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py
