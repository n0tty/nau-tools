#!/bin/bash

function check_if_root() {
    echo "This application requires root";
    test -r /etc/shadow && return 1 || return 0;
}

if [ check_if_root ]
then
    echo "All ok! Seems like you are root!";
    echo "Removing Nau-Tools Configurations";
    rm -rf $HOME/.nautools;
    echo "Removing Paths";
    sed '/nautools/d' ~/.bashrc > bashrcold;
    cp bashrcold ~/.bashrc;
    rm bashrcold;
    echo "Cleanup Successful!";
    echo "Note: Cleanup of nautools doesn't mean the installed dependencies have been removed";
    echo "Now go ahead and remove the project repo. =D ";
else
    echo "Oops! Cleanup requires root privs.";
    exit;
fi
