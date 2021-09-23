---
title: Jedi Knight Tweak Guide
---

<p class="note">
Note: This tweak guide was written a long time ago when it took a pretty beefy
computer to run Jedi Knight well.  These days pretty much every computer can run
this game at a zillion frames per second, so take everything you read here with
a grain of salt.
</p>

This guide is basically to compile a bunch of useful "stuff" for newbies
and/or people who just haven't gotten very deep into the game. This
guide is designed to help you get the best performance/image quality out
of your computer. It should also help you out with some basic tuning
tips for the actual gameplay. It is separated into the following parts.

- [Graphics](#graphics)
- [Controls](#controls)
- [Audio](#audio)

This guide should not be taken as pure fact, it is just a compilation of
observations by someone who has been playing JK for a long time.

<span id="graphics"></span>

## Graphics

This section is divided into 3 parts.

- [Framerate](#framerate)
- [Resolution](#resolution)
- [3d Acceleration](#3d)

<span id="framerate"></span>

### Framerate

Framerate is generally measured in "frames per second." It is the number
of frames of animation your computer is displaying at any given time in
JK. There are no benchmark utilities or time demos for JK, so you just
have to estimate averages when you are trying to test your framerate.
Think of JK as a cartoon, made up of tons of different still pictures,
all played in sequence to form an animation. The more frames of
animation your computer displays, the smoother the movement will be.
Signs of bad framerate are choppy animation, a slide show effect,
general slowdown and/or enemies/players jumping around the screen (which
can also be LAG, or latency).

Framerate has a direct impact on the gameplay. If you are in a
multiplayer game, and you have a framerate of 15, and your enemy has a
framerate of 60, they will have a very strong advantage\! First, their
aiming will be a lot more accurate (no slide-showing past and having to
compensate for each aim). Second, they can run circles around you while
your computer tries to keep up. Third, if your computer is trying so
hard to keep up with the framerate, it's very likely that it is also
having problems keeping up with the network side of things, so your
computer could be dropping packets.

There has been huge argument over how fast the human eye actually sees.
Movies run at about 24 frames per second. In theory, that means that if
you have 24fps in JK, you will be doing pretty well. However, this
doesn't take into account the fact that movie screens (and real life)
are refreshed all at once, while monitors are actually refreshed
vertically (which is why computer screens on older movies always flash).
I generally like to keep my framerate over 35. This ensures that even
when a battle is going on (IE: a more complex scene) your computer will
be able to keep it up. Remember, framerate is always changing depending
on what is being rendered - the more complex a scene, the more power it
takes to keep everything up and running smoothly.

To actually display your framerate, start a game up, then type `t` to
get to the console (or in multiplayer, type `t` then `Tab`). After
that, just type `framerate`. This will put a number at the top of your
screen (that should change as you walk around). This is your framerate
in frames per second. 30 is decent, but higher is better. Go fight some
battles and see what happens. You don't want this to drop below 30 -
battles will often do that. What's the point of turning up the
resolution (discussed below) so you get a nice 30fps when you're walking
around, but then it drops to below 15 during a battle, when you need it
most\!?

<span id="resolution"></span>

### Resolution

Resolution is basically how many pixels are displayed on your screen at
once.  The higher your resolution, the better the game looks. On the flip side,
the higher the resolution, the more computing power it takes.

To get to the display settings, just start up JK, choose your player,
choose setup, then display. You will see a box listing all available
resolutions with your monitor/video card combo. Generally, if you have a
Pentium 1 based computer, you should try 640x480. Most P2's can handle
800x600 easily, and even 1024x768. It gets difficult to read messages if
you go any higher than that, but it looks better, so if your computer
can handle it and you don't mind missing the messages, feel free. If you
are on a Pentium 1 in software mode (IE: no 3d card, which is explained
below), you may want to crank the resolution down even farther. I used
to play at 320x200 just so I had a decent framerate. Sure, it looked
bad, but the gameplay is where it's at\!

<span id="3d"></span>

### 3d Acceleration

3d Acceleration is when JK uses the 3d features of a 3d card that's
installed in your computer. In order to use JK's 3d acceleration
features, you must have a supported 3d card installed. Basically, a 3d
card takes a lot of the geometry processing load OFF the CPU, thus
freeing it up for other things (transform and lighting, floating point
operations, ai, 2d processing, etc). The 3d card also smoothes out
textures so they don't look so pixelated, reduces the "jagginess" of
polygon edges, and supports advanced features such as multiple
transparencies (in some cases), better lighting effects, etc. 3d
acceleration often allows you to turn the resolution of the game way up.
This is because it takes a huge burden off the CPU, freeing it up to
crunch more numbers and feed polygons to the 3d card.

Most computers nowadays (if not all) come with some type of 3d
Accelerater Card installed. This card can be a separate 3d card, or it
could be built in to your 2d card. Either way, JK supports most 3d
cards. However, even if you have a 3d card installed, you **must** tell
JK that you want to use it\! If you don't, you will not be taking
advantage of the 3d acceleration features of your card and the game. To
turn on 3d acceleration, just start the game, go into setup, click
display, then check the "Enable 3d Acceleration" box. If the box doesn't
appear (it should be above the resolution list), your card most likely
isn't supported. Once you check the box, the resolutions will change to
all valid 3d accelerated resolutions. Higher looks better, as discussed
before, but make sure you keep a good framerate. Just to show yourself
the texture smoothing and image quality enhancements of your card, try
640x480 in software, walk around, test the framerate, then go back,
check the box, and walk around some more. There should be a very
noticeable difference.

Another thing that most 3d cards support is colored lighting. JK itself
doesn't have colored lighting, but it's addon pack, Mysteries of the
Sith, does. You may have to check the "enable colored lighting" box in
the display options to see it. Colored lighting really makes the game
and the engine look a lot nicer.

On a last note, some computers (especially ones that use 3dfx Voodoo
series cards) have a separate 3d card. For instance, someone may have a
RivaTNT card as their primary 2d card, which also has a 3d core.
Attached to this could be a Voodoo 2 3d accelerator card. People do this
often in order to play games that only support 3dfx glide based 3d
acceleration. By enabling JK's advanced display configuration menu, you
can choose which 3d core (in this example, the Riva or the Voodoo) JK
uses. You can only use one at a time. In order to enable the advanced
menu, you will have to run JK from the command line. Click **Start**,
then **Run** then the following:

`C:\Program Files\Lucasarts\Jedi Knight\jk.exe -displayconfig`

Note: you might have to modify the path if you installed JK into a different
directory, or if you're using the Steam or GoG versions.

Once you have started JK, just go to the display menu once again, and
towards the bottom, there will be an "Advanced Options" button. Once you
go in there, there are all kinds of options, but the only one that will
help you is the box that allows you to choose which 3d card you use.
Primary Display Driver will be your main 2d card, or your main 2d/3d
card, whichever you have. Under that, if you have a separate 3d
accelerator, you will see it listed. Just click on it, press OK, and JK
will use that one from now on (unless you go back and uncheck then
recheck the 3d box - if that's the case, you will have to reset the
display as outlined above). The advanced options tab will only show up
if you start JK with the -displayconfig switch.

<span id="controls"></span>

## Controls

This section won't be as long as the previous, but the stuff is equally
important for a good playing experience. First of all, throw away your
joysticks and break out your mouse. That's right\! Most First Person
Shooters are best played with a mouse. The mouse allows you to easily
and accurately aim. The mouse also allows you to easily navigate around
- you can do a full 180° turn with the flick of your wrist.

The mouse can be a little difficult to get used to, but once you do, you
will never switch back. Generally, people use the left mouse button for
fire, and the right for jump. Another popular configuration is
Fire1/Fire2 for JK (since it has multiple fire modes for most of the
weapons).

So, your right hand is on the mouse, and your left is on the keyboard
(unless you're left-handed, in which case this will probably be
reversed). Your keyboard hand should *not* have a "turn right" or "turn
left" key. Those are just a waste. You should use your mouse to
navigate. A better setup is to have a "strafe left" and "strafe right"
key set. This allows you to slide left and right, dodging projectiles,
while still keeping your sights on the enemy.

This setup also allows you to "circle strafe," which is a method of
circling your opponent while keeping your sights steady on them. You
just strafe one way and move your mouse sideways the opposite way. Once
you get used to this, you will be able to literally run circles around a
lot of players.

The rest of the controls aren't critical. A lot of people bind their
most used force powers near there, as well as "activate" - make sure you
have enough keys to use as you need to (the number pad is a good place
for your left hand).

Other controller related tweaks that are important include:

  - Always Run: Should be ON at all times. This makes your player a lot
    faster, thus making you a harder target (as well as making it easier
    for you to chase people down).
  - Aiming Crosshairs: A personal preference, but it really helps with
    aim and orientation.
  - Automatically Switch Weapon: When you pick up a more powerful
    weapon, this will automatically switch to it.
  - Keep Weapon: If you specifically select a weapon, it won't switch it
    off.
  - No Dangerous Weapons: In multiplayer, it's best to get rid of the
    "no dangerous weapons" checkbox. This way, if you have a concussion
    rifle selected, it won't switch down to a crossbow if you pick one
    up.
  - Keep Lightsaber: If you select a lightsaber, it won't switch it off
    unless you do it specifically.
  - Lightsaber Auto-Camera: Switches you to 3rd person view whenever you
    turn on the saber. Again, mostly a preference thing.

<span id="audio"></span>

## Audio

JK supports 3d positional audio through A3d, a 3d sound standard. Any
A3d 1.0 card should support this, as well as most other 3d sound cards
nowadays (through a wrapper). All you have to do is go into the sound
setup and check the "enable A3d sound" box. This box won't appear if you
don't have a supported sound card.
