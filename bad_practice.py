import sys
import rhythmsurgeon

def classic_beat(event):
    return event["type"] == "AddClassicBeat"

level = rhythmsurgeon.Level(sys.argv[1])
level.rows.sort(key=lambda r: r["row"])

which = input("What would you like to scan for? 1 for x----- rows, 2 for double swing, like 1 tick and 2 swing. Use -1 for all scans. > ")

if which == 1 or which == -1:
    for item in filter(classic_beat, level.events):
        if level.x_at_beat(item["bar"], item["beat"], item["row"])[0] == "x":
            print("You have an x pattern that starts with an x at bar {0} and beat {1}. It's pattern is {3}."
            .format(level.x_at_beat(item["bar"], item["beat"], item["row"])["bar"],level.x_at_beat(item["bar"], item["beat"], item["row"])["beat"],level.x_at_beat(item["bar"], item["beat"], item["row"])["pattern"]))
elif which == 2 or which == -1:
    for item in filter(classic_beat, level.events):
        if item["swing"] >= item["tick"] * 2:
            print("You have a double swing pattern that has a tick of {0} and a swing of {1} at bar {2} and beat {3}.".format(item["tick"], item["swing"],item["bar"], item["beat"]))