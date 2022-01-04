if [ "$(whoami)" != 'root' ];
	then
		echo "У вас нет root прав. Продолжить?(Y/n)"
		read continue
		if [ $continue != 'n' ];
			then
				apt install python3 python3-pip speedtest-cli
				chmod +x SpeedTest.py
				clear
				echo 'Программа установлена!'
			else
				exit
			fi
	else
		apt install python3 python3-pip speedtest-cli
		chmod +x SpeedTest.py
		clear
		echo 'Программа установлена!'
		echo 'Использовать как бинарный файл?(Y/n)'
		read utb
		if [ $utb != 'n' ];
			then
				echo "python3 /bin/SpeedTest.py" > testspeed
				install testspeed /bin
				install SpeedTest.py /bin
				rm -f testspeed
			else
				exit
			fi
	fi
