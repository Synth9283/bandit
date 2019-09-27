#!/bin/bash

# colors
red=`tput bold && tput setaf 1`
green=`tput bold && tput setaf 2`
yellow=`tput bold && tput setaf 3`
blue=`tput setaf 4`
reset=`tput sgr0`

# PS3
PS3=${red}'Bandit challenge to exploit: '${reset}

# menu function
while true;
do
	read -p ${red}"Press enter to continue"
	clear
	echo ${yellow}"                            overthewire.org bandit            "
	echo ${green}"================================================================================"${blue}
	select opt in "bandit0" "bandit1" "bandit2" "bandit3" "bandit4" "bandit5" "bandit6" "bandit7" "bandit8" "bandit9" "bandit10" "bandit11" "bandit12" "bandit13" "bandit14" "bandit15" "bandit16" "bandit17" "bandit18" "bandit19" "bandit21" "bandit22" "bandit23" "bandit24" "bandit27" "bandit28" "bandit29" "bandit30" "bandit31" "Quit"
	do
		clear
    case $REPLY in
      1)
        scripts/bandit0.py
				break
        ;;
      2)
        scripts/bandit1.py
				break
        ;;
    	3)
        scripts/bandit2.py
				break
        ;;
      4)
        scripts/bandit3.py
				break
        ;;
      5)
        scripts/bandit4.py
				break
        ;;
      6)
        scripts/bandit5.py
				break
        ;;
      7)
        scripts/bandit6.py
				break
        ;;
      8)
        scripts/bandit7.py
				break
        ;;
      9)
        scripts/bandit8.py
				break
        ;;
      10)
        scripts/bandit9.py
				break
        ;;
      11)
        scripts/bandit10.py
				break
        ;;
      12)
        scripts/bandit11.py
				break
        ;;
      13)
        scripts/bandit12.py
				break
        ;;
      14)
        scripts/bandit13.py
				break
        ;;
      15)
        scripts/bandit14.py
				break
        ;;
      16)
        scripts/bandit15.py
				break
        ;;
      17)
        scripts/bandit16.py
				break
        ;;
      18)
        scripts/bandit17.py
				break
        ;;
      19)
        scripts/bandit18.py
				break
        ;;
      20)
        scripts/bandit19.py
				break
        ;;
      21)
        scripts/bandit21.py
				break
        ;;
      22)
        scripts/bandit22.py
				break
        ;;
      23)
        scripts/bandit23.py
				break
        ;;
      24)
        scripts/bandit24.py
				break
        ;;
      25)
        scripts/bandit27.py
				break
        ;;
      26)
        scripts/bandit28.py
				break
        ;;
      27)
        scripts/bandit29.py
				break
        ;;
      28)
        scripts/bandit30.py
				break
        ;;
      29)
        scripts/bandit31.py
				break
        ;;
      30)
        break 2
        ;;
      *) echo "invalid option $REPLY";;
    esac
  done
done
clear
echo ${green}"Thank you for using my script! -SKane"
