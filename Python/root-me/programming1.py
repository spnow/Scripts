import re
line = ":Candy!Candy@hzv-djs.n1p.2olmip.IP PRIVMSG dtctdBot :783 / 7600"
chatre = re.compile ("(\d+)\s*([-+/*])\s*(\d+)")
# chatre = re.compile('^(?P<user>\S+) sends "(?P<data>.*)"$')
m = chatre.match(line)
if m:
    print "%s: %s" % (m.group(0), m.group(1), m.group(2))