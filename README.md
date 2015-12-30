# dlink-dir628-loginbruteforce
simple python to attempt a brute force to a dlink dir-628 wifi/router/firewall<br>
<br>
Brute force login utility for the dlink dir-628 wifi/router/firewall.<br>
<br>
this little box uses javascript to do some custom stuff to the password before sending to the router.<br>
<br>
It first takes the user input and either truncates or pads 0x01 to 16 characters.<br>
<br>
It then prepends the hash (listed in the script from the router, changes every few minutes) to the password.<br>
<br>
It then pads the password with 0x01 to 63 characters.<br>
<br>
Only then does it MD5 hash it.<br>
<br>
Then it prepends the hash again and sends it to the router<br>
<br>
My guess is that the password has to be stored in plain text on the router somewhere.<br>
Will be looking for that next<br> 
<br>
<br>
USAGE:  python dlink-dir628-brute.py \<ip of device\> \<path to wordlist\> <br>
<br>
this may cause router to crash around 33,000 attempts...or so.
