#!/bin/bash

{ echo "n";
 echo 20;
 echo y;
 echo "logs/10s_p1_lower_spp/log$1.txt"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .9;
 echo p;
 echo p;
 echo 10;
 echo 10;
 echo w;
 echo w;
 echo n;
 echo n;
 cat;
}| python3 sim.py
