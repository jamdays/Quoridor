#!/bin/bash

cd /h/u13/c3/01/djayamax/Documents/Quoridor/PySim
{ echo "n";
 echo 2;
 echo y;
 echo "logs/UFtest/nonUFlog$1.txt"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .5;
 echo p;
 echo p;
 echo 100;
 echo 100;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py UF
