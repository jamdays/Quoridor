#!/bin/bash

{ echo "n";
 echo 1;
 echo y;
 echo "logs/$1"
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
