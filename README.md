# Mi-HRMonitor

This is a connector server and automation between [Notify for Mi Band](https://mibandnotify.com/) and [HRCounter](https://github.com/qe201020335/HRCounter).
It uses [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) on the phone and python for the server.

## Usage
In daily usage you only need to:
- Run the server
- Start a workout in the Notify app (not neccesary but increases HR update rate)

## Setup
### Notify
- Enable Notify>Tools>Tasker Integration

Tools | Tasker Integration
:----:|:----:
![image](https://user-images.githubusercontent.com/40366128/153191652-df0e4008-9974-414d-9de6-ec5230fdc227.png) | ![image](https://user-images.githubusercontent.com/40366128/153191707-fc658505-6d4c-4cd8-93b3-94c14fc94d1b.png)

### Tasker
- Open [this](https://taskernet.com/shares/?user=AS35m8ku9Pw0bnSHS7%2BZ7y1E2q4KHnPpDHYObULwmn66Y8z5T7zuiwcBTY98jwTDGZd2pA%3D%3D&id=Project%3AMi+Band+HR+Monitor) link on your phone.
- Press import
  - Press yes Import Data to Tasker
  - Press yes to enable the project
- Select the project from bottom of the screen 
- Press `Profiles>HR Received>Wifi Connected` enter your wifi name in the SSID section
  - This prevents your phone connecting to random devices if you aren't connected your home network
- Back to project then `Tasks>HRtoweb>HTTP Request` enter your `http:\\SERVER_IP:PORT`(default port is 7575) in the url section

### Server
- Run the server opening a cmd or creating a `.bat` file and writing `python3 hrserver.py`
- Allow firewall
asd

### HRCounter
- Install HRCounter and open the game after installing
- Open the file `Beat Saber\UserData\HRCounter.json`
- Set `"DataSource":` to `"WebRequest"`
- Set `"FeedLink":` to `"http://localhost:7575"`
  - If the server is running on another computer write it's ip instead of `localhost`

## Notes
- Probably there is a better way to do this but I like my way because if it breaks I can't get mad at someone and probably can fix it by myself.
- Feel free to contanct, open an issue or submit PRs.
