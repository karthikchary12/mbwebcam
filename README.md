# Mbwebcam 

  Firstly there are somethings alredy exist to view your Ip webcamera, but when it comes to linux and mac there are some limitations which would be problem for windows applications. Ehen through you can get the IP webcam camera view by copying the url into the browser but it is a python code which I want to improve it further as of now it is basic one which can help to access the camera view from your IP webcams

## PREREQUISITES ( Please verify if you have installed )

* Python3
* Pip
* Ip webcam(on your mobile)

## Installation :

### (NOTE: This will work only when Your both devices are connected to the same network/wifi )

First Open your terminal/command line to clone this using
```
git clone https://github.com/karthikchary12/mbwebcam.git
```
Get into the directory
```
cd mbwebcam
```
Now install the required packages using the requirements.txt
```
pip install -r requirements.txt
```
### Mobile setup

You need to install a application know as IP webcam on your mobile 

![Screenshot from 2022-10-08 20-56-47](https://user-images.githubusercontent.com/63688597/194715124-a13b0c41-af26-47ff-9dbf-011ff9b1045f.png)


Open the application and scroll down where you can see Start Server

![Screenshot from 2022-10-08 20-57-14](https://user-images.githubusercontent.com/63688597/194715136-2da8e050-edc1-4c1e-a469-33c252582188.png)


Agree to the camera permissions and you can see your camera view on the screen Now you should notedown your Ip url 

![Screenshot from 2022-10-08 20-57-39](https://user-images.githubusercontent.com/63688597/194715176-876bd3eb-7b8b-422b-bf23-1a53c2ffd5d9.png)


Now open your mbwebcam folder and run the python file 
```
python3 mbwebcam.py
```
Now enter your noted url in it

![Screenshot from 2022-10-08 20-49-06](https://user-images.githubusercontent.com/63688597/194715193-8f48c961-bb25-499a-8768-e2947acdba0e.png)


Done you can get the mobile camera view on your pc 

![Screenshot from 2022-10-08 20-51-13](https://user-images.githubusercontent.com/63688597/194715205-94f06ff7-1e13-4c17-bc56-4fadc14159f9.png)

### If anyone have good ideas and solution to improve this code you can help me with it by becoming collaborator or atleast you can mail me 
* sriramkarthikchary@gmail.com
