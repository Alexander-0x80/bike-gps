# Bike GPS Logger for Android

A Simple Python script written using [SL4A](http://code.google.com/p/android-scripting/) to log my mountain bike traveling points without internet connection . 

#### Dependency :
To plot coodrinates on Google maps i am using [pygmaps](http://code.google.com/p/pygmaps/) library . 

To Install : 
`pip install pygmaps`

#### Use :
1. Running _"locate.py"_ on your android device using SL4A Python interpreter, will log your coordinates to _"points.json"_. 
2. _"plot.py"_ Will convert location data from _"points.json"_ and create _"pointmap.html"_ with all points plotted on Google map .

Note that default starting location for Google map is Israel .

#### License :
Released under [WTFPL](http://www.wtfpl.net/) license .