import simplejson as json
import pygmaps

ilmap = pygmaps.maps(31.7833, 35.2167, 10)

with open("points.json", "r") as points:
    for point in points:
        jdata = json.loads(point)
        ilmap.addpoint(
            jdata["latitude"],
            jdata["longitude"],
            "#0000FF")

ilmap.draw("./pointmap.html")
