#!/bin/bash

cd /h/u13/c3/01/djayamax/Documents/Quoridor/PySim
{ echo "n";
 echo 1;
 echo y;
 echo "logs/long_spp/log$1.txt"
 echo y;
 echo .9;
 echo .9;
 echo .9;
 echo .5;
 echo p;
 echo p;
 echo 40;
 echo 40;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py
