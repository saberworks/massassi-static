---
title: Creating Custom Shaders
author: Sine Nomen
email: sikarenite@hotmail.com
description: >
    This tutorial covers basic light emitting shaders, and how to bring them
    into Radiant.
date: 2003-03-01
category: jo
---

Author: Sine Nomen

## Part 1: Basic Light Shaders

This is probably the most useful and common shader you'll come across.
The basic syntax is pretty straightforward:

    textures/tutorial/shader1
    {
        qer_editorimage textures/doomgiver/light1d
        {
            map $lightmap
        }
        {
            map textures/doomgiver/light1d
            blendFunc GL_DST_COLOR GL_ZERO
        }
        {
            map textures/doomgiver/light1dglow
            blendFunc GL_ONE GL_ONE
        }
    }

`textures/tutorial/shader1` &larr; This format is standard for all
shaders. When creating your own shader, replace 'tutorial' with a folder
name of your choice. If you're using custom textures, you might want to
put them in a physical folder of the same name in gamedata/base. Replace
'shader1' with whatever you want your new shader to be called.

`qer_editorimage textures/doomgiver/light1d` &larr; This line is used only
by the editor; it's not absolutely necessary, but it prevents your
shader from showing up as 'texture not found' in Radiant. You can use
whatever texture you like for this; the most common is just the basic
shader texture.

`map textures/doomgiver/light1d` &larr; This is the basic shader texture
(often used in the editorimage stage as well). In other words, it's the
texture you're plugging into the shader to make it glow. This is the
first stage.

`map textures/doomgiver/light1dglow` &larr; This is the texture that tells
JO which part of the shader will appear to glow. The brightness and
color of the light in JO is dictated by the brightness and color of this
texture. This is the second stage.

## Part 2: Basic Shaders That Emit Light

    textures/nar2/window2
    {
        q3map_lightimage    textures/doomgiver/light1dglow
        qer_editorimage textures/doomgiver/light1d
        q3map_surfacelight  340
        q3map_lightsubdivide    128
        {
            map $lightmap
        }
        {
            map textures/doomgiver/light1d
            blendFunc GL_DST_COLOR GL_ZERO
        }
        {
            map textures/doomgiver/light1dglow
            blendFunc GL_ONE GL_ONE
        }
    }

A few more lines are needed to make the shader actually emit light on to
the surrounding surfaces.

`q3map_lightimage textures/doomgiver/light1dglow` &larr; This texture is
usually the same one used in the second stage. An average color is drawn
from this texture and used to define the color of the light it emits.
Alternatively, you can enter a numeric RGB value here:

`q3map_lightrgb .9803 .9843 1`

The value of this color on a regular 255 point RGB scale is, for
example, 250, 251, 255. Take each digit and divide it by 255 to get a
normalized number for use in your shader.

`q3map_surfacelight 340` &larr; This is the strength of the emitted light.
How it translates into JO depends on a number of factors, so you'll have
to experiment to get it to your liking.

`q3map_lightsubdivide 128` &larr; This line is necessary only if you're
using Q3MAP2 to compile your map. All light-emitting shaders do is
create a series of small point lights (like the ones you'd place in
Radiant) according to the values you enter. This tells the compiler how
far apart to place them.

## Part 3: Implementing Your Shader in Radiant and JO

The syntax of a shader goes in a .shader file (rename the extension of a
.txt file), which in turn goes in the gamedata/base/shaders folder. Open
shaderlist.txt, found in the same folder, and add the name of your
.shader file to the list. Example:

    ...
    sprites
    system
    test
    text_crawl
    tutorial
    ui
    yavin
    zoom
    ...

...and that's it. Open Radiant and you should see the name of your
.shader in the texture menu. Be sure to include the /shaders folder in
your .pk3 (with only your custom .shader) when you release it. Good
luck.
