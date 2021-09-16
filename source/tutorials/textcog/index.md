---
title: "Text Messages/Basic Cog"
author: EvanC
email: ev@wave.co.nz
description: >
    A bit of basic cog and how to make text messages appear on the screen.
date: 1998-08-01
original: textcog.htm
category: jk
---

Author: EvanC


  
Get this cog: [Download cog](textcog.zip)
  
This is pretty simple. Using the line Print(); in cogs you can print
text to the screen. This small tutorial will let those without much cog
knowledge have text messages.  
  
While I'm at it I may as well go into cog a bit. Lets start at the
start:  
  
You can open/create cogs with a text editor. Remember to have the file
extension as .cog and not .txt The first section in a cog is the symbols
section. This section starts with the word "symbols" It ends with the
first "end". From the cog we will be using this is the symbols
section:  
  

``` 
symbols

sector      sec
message entered

end
```

As you can see, it starts with a "symbols" and ends with an "end". In
between there are two lines. The first starts with a "sector" and ends
with a sec. If you open the cog with JED and add this cog you will
notice it has a value called "sec" Those of you who are observant will
notice that this is also the last word of the sector line. It's not a
coincidence. Try changing the "sec" into "sect". If you open up JED
again and try to add the cog the value should now be "sect". So, the
first word is what the object is. It can be sector, thing, surface,
sound ETC. Check JKspecs for more info. The second word is the name of
the object. As far as I know there is no limit to what this can be
called(but I would avoid objects with the same name). On to the second
line. This is a different kind of line. It starts with a "message" and
ends with "entered". This is probably the most important part of coging.
The JK engine sends messages to it's cogs. So when a level starts up it
sends a startup message to the cog. This brings us to the code section.
At the start of the code section is a "code" and at the end, like
symbols section, it has an "end". Here is what it looks like:  

```
code

entered:
Print("you have entered the sector");
return;

end  
```
  
Sp, you know what a startup message is but this message is "entered".
The entered message is sent when a sector or thing is entered. Anyway,
lets look at the code section. In the middle is a word "entered:". This
is the start of the entered section. This section ends with "return;".
In between is the code of the cog. When the entered message is received
the code in the entered section is run. In this case it is this:  
  

``` 
Print("you have entered the sector");
```


This line tells JK to print the message "you have entered the
sector". So each time the sector "sec" is entered the cog
will print "you have entered the sector" to the screen.



For more information on code verbs (like Print) and messages 
go to the Unoficcial JK file specs.



If you need more explaining or don't understand something 
please email me and I'll see if I can help you.



Evan C
