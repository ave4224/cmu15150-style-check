import sys

f = open("tmp/runner.sml", "w")
f.write("val _ = markAppends \"" + sys.argv[1] + "\"")
f.close()