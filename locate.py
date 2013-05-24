import android
import json

droid = android.Android()
droid.startLocating(10000)                  # 10 sec update freq
while True:
    droid.eventWaitFor("location")          # Block until event arrives
    droid.eventPoll()
    loc = droid.readLocation().result
    if loc == {}:
        print "No Data"
        loc = droid.getLastKnownLocation().result
    else:
        with open("points.json", "a") as f:
            f.write(json.dumps(loc["gps"]) + "\n")
        print loc
