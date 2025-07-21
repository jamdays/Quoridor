#!/bin/bash

{ echo "n";
 echo 2;
 echo y;
 echo "logs/extra_long_spp_switched/log$1.txt"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .9;
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
