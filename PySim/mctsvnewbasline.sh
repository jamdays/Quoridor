#!/bin/bash

{ echo "n";
 echo 50;
 echo y;
 echo "logs/mctsvnewbasline/log$1"
 echo y;
 echo .9;
 echo .9;
 echo .5;
 echo .5;
 echo p;
 echo p;
 echo 8;
 echo 8;
 echo w;
 echo w;
 echo n;
 echo y;
 echo n;
 echo y;
 echo w;
 cat;
}| python3 sim.py
