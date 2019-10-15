#!/bin/bash

function welcome_and_greet() {
    echo "Network Access Uncontrolled Toolkit v0.1";
    echo "Author: @TanoyBose";
    echo "License: Will be added here pre-release";
    echo "https://github.com/n0tty/nau-tools"

}

function test_file_exists() {
    test -f $1 && return 1 || return 0;
}

function setup_ttyd() {
    echo "Setting up a tty webserver";
    mkdir -p $HOME/.nautools/utils/bin/
    ttyd_filename="ttyd_linux."`uname -m`;
    if [ -f $ttyd_filename ]
    then
        cp $ttyd_filename $HOME/.nautools/utils/bin/ttyd_server;
        echo "4" > $HOME/.nautools/.nautools_config_status;
        echo "We have got the power of TTYd with us now!";
    else
        echo "[*] There is some issue with ttyd file. Just download the latest release for the platform and copy it to .nautools directory with the name ttyd_server";
        echo "TTYd isn't exetremely essential component of this utility. So it is fine if you do not want to utilize it or download it.";
        sleep 3;
     fi
}

function get_and_copy_modules() {
    clear;
    echo "Building directories";
    mkdir -p $HOME/.nautools/
    mkdir -p $HOME/.nautools/core/
    mkdir -p $HOME/.nautools/menu/
    mkdir -p $HOME/.nautools/config/
    mkdir -p $HOME/.nautools/tmp/
    mkdir -p $HOME/.nautools/utils/src/
    mkdir -p $HOME/.nautools/utils/bin/
    nau_main="NauTools.py";
    clear;
    echo "Attempting to copy modules.";
    if [ -f $nau_main ]
    then
        cp $nau_main $HOME/.nautools/$nau_main;
        echo "1" > $HOME/.nautools/.nautools_config_status;
        echo "[+] Main module ready ";
    else
        echo "[-] NAU TAP module missing";
        exit;
    fi
    sleep 1;
    clear;
    echo "Attempting to copy modules.."
    cp -r core/ $HOME/.nautools/
    echo "[+] Core module copied"
    echo "2" > $HOME/.nautools/.nautools_config_status
    cp -r menu/ $HOME/.nautools/
    echo "[+] Menu module copied"
    echo "3" > $HOME/.nautools/.nautools_config_status
    sleep 1;
    clear
    echo "Attempting to copy modules..."
    sleep 1;
}

function check_if_root() {
    echo "This application requires root";
    test -r /etc/shadow && return 1 || return 0;
}

function first_run_nautools() {
    echo "Seems like the program has not been run before.";
    echo "Reinitializing...";
    mkdir -p $HOME/.nautools;
    echo "Completed initializing";
    echo "0" > $HOME/.nautools/.nautools_config_status
    #clear;
}

function test_first_run() {
    echo "Checking if the program has been run before.";
    if [ -d $HOME/.nautools ]
    then
        echo "Seems like the first run has been completed.\nIncase there is some error in the execution of the tool, run \"nau_cleanup.sh\" and re-run \"nau_setup.sh\"";
        exit;
    else
        first_run_nautools;
    fi
    #test -d $HOME/.nautools/ && echo "Seems like firstrun has been completed.\nIncase there is some error in the execution, read up the wiki on how to troubleshoot issues and incase it does not help, raise a issue on the the project repositiory."; exit; || first_run_nautools;
}

function setup_kali() {
    echo "This is identified as a kali system";
    test_first_run;
    apt-get install -y ebtables macchanger net-tools tcpdump arptables iptables wget python3 git zip bridge-utils sshpass;
    get_and_copy_modules;
    clear;
    echo "Initialization complete! Adding binaries to path.";
    new_path="export PATH=\"$HOME/.nautools/:$PATH\"";
    echo "running: "$new_path;
    echo "" >> $HOME/.bashrc;
    echo "export PATH=\"$HOME/.nautools/:\$PATH\"">> $HOME/.bashrc;
    #$new_path;
    #echo $PATH;
    #service ssh start;
    #service ssh restart;
    setup_ttyd;
    echo "If we reached this point, the device is well setup for Breaking Network Access Control! Go Pwn!";
    welcome_and_greet;
}

function setup_arch() {
    echo "Just assumed this to be arch linux mate";
    #test_first_run;
}

function identify_architecture() {
    test -f /etc/apt/sources.list && setup_kali || setup_arch;
}

if [ check_if_root ]
then
    echo "All ok! Seems like you are root!";
    if [ -f /etc/apt/sources.list ]
    then
        setup_kali;
    else
        setup_arch;
    fi
else
    echo "Oops! Seems like you are not root! Get outta here mate!";
    exit;
fi
