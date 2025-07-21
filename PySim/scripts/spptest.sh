#!/bin/bash

cd /h/u13/c3/01/djayamax/Documents/Quoridor/PySim
{ echo "n";
 echo 10;
 echo y;
 echo "logs/$1"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .9;
 echo p;
 echo p;
 echo 4;
 echo 4;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py
