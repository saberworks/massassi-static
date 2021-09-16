---
title: "C Elements: COG Basics"
category: jk
description: >
    A very newbie-friendly cog guide explaining the essentials.
date: 1999-04-28
author: Rishka
email: mkoger@tcs.tulane.edu
original: c_elements.htm
---

Author: Rishka


The COG language is a C-based language. What's that mean? Well, C is one
of the most popular programming languages used today. Other programming
languages (including Java and COG) are *based* on it, meaning that they
work very similiar and use many of the same commands. In this tutorial,
I'm going to discuss many of the commands that were carried over from C.
By the time you finish this tutorial, you should have a basic knowledge
of how to program, not just in COGs, but in any C-based language. Let's
get started, shall we?

## OPERATORS:

You're probably wondering what in the world is an operator? Well,
simply put, an operator is a special character that performs a
specific function such as *multiply*. Operators are
*the* most common C element you'll see in
cogs. Below is a list of all *known*
operators in the COG language. Most of them you will recognize.
Probably the only ones that need explaining are the *logical
operators*.

A logical operator extends the action of *if-else* statements. They
let you combine two or more relational tests into a single statement
(AND or OR operators) or change the value returned from a relation
(NOT operator). We'll discuss logical operators more when we go over
*if-else* statements.


### Primary Math Operators

<div class="tutorial-table no-headers" markdown=1>

|    |                     |
|:--:|:--------------------|
| \* | Multiplication      |
| /  | Division            |
| %  | Modulus (remainder) |
| \+ | Addition            |
| \- | Subtraction         |

</div>

### Relational Operators

<div class="tutorial-table no-headers" markdown=1>

|     |                          |
|:---:|:-------------------------|
| ==  | Equal to                 |
| \>  | Greater than             |
| \>= | Greater than or equal to |
| <   | Less than                |
| <=  | Less than or equal to    |
| \!= | Not equal to             |

</div>
 
### The Logical Operators

<div class="tutorial-table no-headers" markdown=1>

|      |     |
|:----:|:----|
| &&   | AND |
| \|\| | OR  |
| \!   | NOT |

 

## COMMENTS:

Comments are not COG commands. In fact, Jedi Knight/MotS ignores any
and all comments in your COGs. So why use comments? You should add
comments in your COGs that explain in plain language (not COG) what's
going on. Use comments abundantly so that someone reading your COG
later has a clear guide to the COGs functions. Another programmer
might be able to trace through your code and figure out how the COG
works, but comments speed up the process.

In COGs, comments begin with one of two things: either a double slash
(//) or a pound sign (\#). Comments extend to the end of the line.
Anything following a comment is disregarded by Jedi Knight. Also, you
can put comments on a line by themselves *or* at the end of a line of
code (remember, anything *following* that comment is disregarded).
Examples of comments:

```
    // Increments x by 1
    x = x + 1;  
    
    x = x + 1; // also increments x by 1
```

Both of these examples do the same thing; they're just layed out
different. How you choose to add your comments is up to you. Using
comments for things like the example above is redundant, as anyone can
tell that *x* is being incremented by 1. I suggest using comments
*only* when they help explain what is going on in the code.

 
## IF-ELSE STATEMENT:

One of the most common C commands, the
*if* statement can be found in every
programming language. The *if* statement
tests the relational operators (see above) and decides exactly which
sections of code to run and which to ignore. The
*if* statement is a multiline programming
statement. Basically, what this means is that it almost always takes
more than one line of code. Here is the format of the
*if* statement:

<span class="tutorial-gray" markdown=1>
> if (*relationalTest*)  
> { *A block of one or more statements* }
</span>

From the italics, you can tell that the
*if* statement uses a relational test
that you must supply inside the parantheses. The parantheses are
*required*; without them, your *if*
statement won't work. *relationalTest* can be the comparison of any
two variables.

<span class="tutorial-red">Warning! Never put a semicolon after the closing 
parantheses! Jedi
Knight will think that the *if* statement
is finished and will begin executing the block of statements that
follow the *if*, whether or not the
relational test is true or false.</span>

OK, so let's put this into practice now. Say we want to check and see
if a number is greater than 0, and if it is, to print out on the
screen that it is? Here's how you'd do it:

```
    if (x > 0)  
    {  
        Print("x is greater than 0!");  
    }
```

Not much to it, now is there? OK, that's all fine and dandy, but what
if we wanted to know if the number is between 0 and 5? We could use
two *if* statements:

```
    if (x > 0)
    {
        if (x < 5)
        {
            Print("x is greater than 0 and less than 5!");
        }
    }
```

But that's more work than is necessary. It's much easier using the
*logical* operators. Here's how we'd do it using logical operators.

```
    if ((x > 0) && (x < 5))
    {
        Print("x is greater than 0 and less than 5!");
    }
```

See how much easier that was? Logical operators are very useful for
*if* statements. Now, there's another
side to the *if* statement... the
*else* statement. The
*else* statement determines what happens
if the relation is *false*. The *if*, as
you already know, determines whether or not a block of code runs, but
it's possible to extend the action of
*if* so that it runs one block of code or
another depending on the result. To do this, we simply need to add the
*else* statement after the
*if*'s closing brace. Here is the format
of the *if-else* statement:

<span class="tutorial-gray" markdown=1>
> if (*relationalTest*)  
> { *A block of one or more COG statements* }  
> else  
> { *Another block of one or more COG statements* }
</span>

The *else* statement runs only if
*relationalTest* is false. Here's an example of the
*if-else* statement at work:

```
    if (x > 0)
    {
        Print("x is greater than 0!");
    }
    else
    {
        Print("x is not greater than 0!");
    }
```

Well, that seems to be it on the
*if-else* statement. Now, we'll move on
to some of the other **C elements**.

## LOOPS:

<span class="tutorial-orange" markdown=1>
DEFINITION - A *loop* is a program's repeated execution of the same
set of instructions.
</span>

Looping is a very important concept in programming. In fact, COGs (as
well as C++) provide three different forms of loops:
*while* and
*do...while* loops, which do things over
and over until some condition is ture, and the
*for* loop, which persforms some actions
a specific number of times.

### The *while* Loop

The *while* loop repeats as long as a
relational test is true. As soon as the relational test becomes false,
the *while* loop terminates and the rest
of the program continues. One of the most important (and most
forgotten) points about loops is making sure that the loop terminates.
An infinite loop can cause hang-ups and/or crashes. To keep loops from
executing forever, you write a controlling relational test, just like
the relational tests that appear inside
*if* statements. Unlike an
*if* statement, a
*while* body keeps repeating as long as
the relational test is true.

<span class="tutorial-red" markdown=1>
Warning! You *must* make sure that something inside the loop
eventually changes the *while*'s
relational test. If the relation is true when the
*while* first begins, and if nothing
inside the body of the *while* ever
changes the relational test, it executes forever. The loop will never
stop, and you'll lose your title of "Master COG Guru Programmer." =)
</span>

Enough introduction. Here's the format of the
*while* loop:

```
    while (relationalTest)
    {
        // Block of one or more COG statements
    }
```

Just like the *if*,
*while* is a multiline statement. Also
like *if*, parantheses *must* appear
around the relational expression. The relational expression can
contain one or more relational operators. If you use more than one
relational operator inside the relational expression, use logical
operators (&& and | |) to combine the relational tests.

The relational test appears at the top of the
*while* loop. The location of the test is
important; if the *while* expression is
false the first time through, the loop will not even execute once\!
The body of the *while* loop executes
only if the relational expression is true, and it keeps executing as
long as the relational expression is true. If and when the relational
expression becomes false, the COG continues at the statement following
the *while* loop's closing brace.

Well, now on to the next loop....

### The other *while*: the *do-while* Loop

There is a second *while* loop, called
the *do-while* loop, whose relational
test appears at the bottom of the loop's body rather than the top.
Here is the format of the *do-while*
loop:

```
    do
    {
        // Block of one or more COG statements
    }
    while (relationalTest);
```

As with the *while* loop, you must put
parantheses around the relational expression. The final semicolon
after the relational test is *required* to terminate the
*do-while* statement.

You should use a *do-while* loop instead
of a *while* loop when you want the body
of the loop to execute at least once. The location of the
*do-while*'s relational test casues
execution to fall through and run the body of the loop at least once.
Only *after* the body executes once can the
*do* loop check the relational test to
see whether or not the loop should terminate. Only after the
relational test is false will the rest of the COG continue executing.
The *while* loop might never execute
because Jedi Knight checks the relational test before the body has a
chance to execute. *do-while*, on the
other hand, doesn't check the relation until the loop executes one
full time.

Simple enough, eh? On to the *for*
loops....

### The *for* Loop

The *for* statement makes
*for* loops look rather difficult, but
*for* loops really aren't that difficult
to understand. The syntax of the *for*
statement may look a little strange but you'll get used to it. Here's
the format of the *for* loop:

```
    for (startexpression; relationalTest; countExpression)
    {
        // A block of one or more COG statements
    }
```

When Jedi Knight encounters a *for*
statement, it follows these steps to perform a loop:

1.  Perform the *startexpression*, which is usually the assignment of
    a value.
2.  Test the relational expression for a true or false result.
3.  Perform the body of the loop if the relation is true.
4.  Perform the *countExpression*, which usually increments or
    decrements the operation.
5.  Go back to step 2.

When the relation is tested and found to be false, the COG stops
looping and the COG continues on at the statement following the
*for* loop. As with
*while*, never put a semicolon right
after the *for* statement's parantheses.
However, semicolons are required *inside* the parantheses. The
*for* loop is thoe only statement that
requires such semicolon placement.

Here is a sample *for* loop:

```
    for (i = 1; i <= 10; i = i + 1)
    {
        PrintInt(i);
    }
```

When Jedi Knight gets to this *for* loop,
it prints the following output to the screen:

<span class="tutorial-blue" markdown=1>
> 1 

> 2 

> 3 

> 4 

> 5 

> 6 

> 7 

> 8 

> 9 

> 10 
</span>

Jedi Knight automatically updates the integer *i* each time the
*for* loop executes. The body of this
*for* loop executes exactly 10 times.
Here are the parts of this *for* loop:

> *startexpression*: `i = 1`
> 
> *relationalTest*: `i <= 10`
> 
> *countexpression*: `i = i + 1`

Next are the five actions of the *for*
loop applied to this specific loop. Follow the actions listed here and
you'll see how Jedi Knight produced the numbers from 1 to 10:

1.  Assigns **1** to the variable *i*. You should have a integer named
    *i* defined in your symbols section. Jedi Knight executes this
    *startexpression* only once, before the loop begins.
2.  Jedi Knight tests the relational test, *i \<= 10*, to see whether
    it's true or false. The first time the loop is run, *i* is **1**
    (due to the assignment just made in step 1) and the conditional is
    true, so the body of the loop is executed.
3.  The statement inside the loop body executes, the first time
    printing a **1** for *i*.
4.  The *countexpression* executes, adding **1** to *i*, so that it
    stores a **2** in *i*.
5.  Jedi Knight goes back to step 2, testing the conditional again and
    executing the body of the loop nine more times until *i* contains
    **11**. At that point, the loop is terminated and the program
    continues.

Also, it's important to note that the *countexpression* does not have
to increment the value. It can also decrement the value or increase
the number by a value other than **1**.

