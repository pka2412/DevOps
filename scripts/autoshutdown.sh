#!/bin/bash

#this script checks for the logged in users
#if there are no logged in users, then the system will shutdown

users=$(who | wc -l)
if [ $users -lt 1 ] ; then
    sudo shutdown -h +1 "shuting down in 1 minute"
fi
