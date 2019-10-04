# Track-and-Control(TraCon)-Toolbox
## Real-time animal detection
![](Gif_folder/demo_1.gif)
TraCon can achieve real-time animal detection and output statistic results for standard behavior tests, for example, open field test, elevated plus maze test, Morris water maze, social preference test, et. al.

## Closed-loop feedback control
![](Gif_folder/Demo_closedLoop.gif)
Upon successful detection, we can define a spatial region that would trigger the optogenetic or a sensory stimulation. Here we used two-chamber real-time place preference for demonstration.

## Dynamic region for closed-loop control
![](Gif_folder/demo_social.gif)

Moreover, the spatial region can be either static, as used in two-chamber place preference test, or dynamic, which changes accordingly to the position of another animal.    

## Introduction of TraCon

TraCon toolbox is video-based and written in Python programming language (compatible with Python 2 and Python 3) that can work on Windows, Max OS and Linux system. Due to the low computation requirements, TraCon can run at a single core CPU only computer for real time object detection and feedback control. Considering most neuroscience labs have laser/LED components or customized sensory stimulation, TraCon toolbox can be easily integrated with existing laboratory rig to achieve automation. 


## Step-by-step Video Tutorial
This part is still under development. You may subscript to the mailing list to receive notification regarding the update:
https://docs.google.com/spreadsheets/d/1bvRgqYsHoxdKriIWadSp18Iz_6pi-RCWazMIVA_AIbg/edit?usp=sharing

Or you may check the Youtube channel in the future:
https://www.youtube.com/channel/UCMS8gQo8F_oKKvzGmNWnZBw?view_as=subscriber


## Getting Started

Here we describe our Track-and-Control (TraCon) toolbox, a fully automatic system with real-time object detection and low latency closed-loop hardware feedback. We further demonstrate that the toolbox can be applied in a broad spectrum of behavior tests in the neuroscience field, including open field, cross maze, Morris water maze, real-time place preference, social interaction, and looming-induced defensive behavior tests. TraCon toolbox proved to be an efficient and easy-to-use method, and highly flexible for extension. Moreover, the toolbox is open source and compatible across OS platforms and each lab can easily integrate TraCon with their existing set up to achieve automation. And we hope TraCon toolbox would further accelerate our understanding of the functional architecture of the brain. 

### Prerequisites

1.Python environment and OpenCV library for the object detection analysis.
2.Arduino board for TTL pulse train generation.

This instruction would go through every detail you might need to know while install the TraCon toolbox.


### Intallation

### Windows Users
Installation instruction for windows users:
This installation has been tested in Windows 10 and 7 system

#### Install Python environment:
1.	Download anaconda from www.anaconda.com/distribution/
2.	Chose the Python 3.7 version, 64-Bit Graphic Installer (486MB)
3.	After completion of the download, open the Anaconda3-2019.07-Windows-x86_64.exe installer file
4.	Follow the intuitive installation instruction and chose ‘Add Anaconda to the system PATH environment variable’ during the installation’ and ‘Register Anaconda as the system Python 3.7’

#### Install OpenCV
1.	Open Anaconda Prompt (Anaconda3)
2.	In the command line:
```
pip install opencv-contrib-python
```
#### Install USB serial control Package
1.	Open Anaconda Prompt (Anaconda3)
2.	Type in:
```
pip install pyserial 
```
#### Execution of the code
1.	Open Anaconda and run Spyder
2.	Open the python files downloaded from http://github.com/GuangWei-Zhang/TraCon-Toolbox
3.	Use the default setting of the system.



A step by step series of examples that tell you how to dive into the TraCon toolbox

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
