# Simple web application that controls the door lock throught relay module.



# Service use file systemctl 

`sudo cp RPiApplication.service /etc/systemd/system/RPiApplication.service`


Once this has been copied, you can attempt to start the service using the following command:

`sudo systemctl start RPiApplication.service`

sudo systemctl stop RPiApplication.service

When you are happy that this starts and stops your app, you can have it start aoutomatically on reboot by using this command:

`sudo systemctl enable RPiApplication.service`

`man systemctl`
