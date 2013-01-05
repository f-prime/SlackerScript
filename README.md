About SlackerScript
===================

SlackerScript is a simple language I created on a Friday night just for the hell of it. There is no real reason other than the fact that I enjoy writing interpreters and I was bored...

Current Statements
------------------

These are all the current statements available in SlackerScript

* ADD
* SUBTRACT
* MULTIPLY
* DIVIDE
* SAY
* FOR
* FOREVER
* #
* END VARS

Usage
-----

    python SlackerScript.py <file.slacker>

Docs of Sorts
-------------

### Setting Variables

In Slacker Script variables must be the first thing you set. When you are done setting variables you must tell the interpreter by typing
    END VARS
Here is an example:

    var1 = 1
    var2 = 2
    END VARS
    ADD var1,var2

The END VARS statement tells the interpreter that it is time to start executing the code of the actual program.

### ADD Statement

This applies to the SUBTRACT, MULTIPLY, and DIVIDE statements as well.

The ADD statement has a bit of a learning curve to it at first, but is very easy to understand.

Let's take a look at the following code.

    one = 1
    two = 2
    END VARS

    ADD one,two

The output of this program will obviously be three because 1 + 2 = 3, easy. However, now that this piece of code has been executed the variable [one] has been set to 3. Now, you may be asking why that is exactly, well, what the ADD statement does is it takes the output and sets it to the variable to the left of the comma. So now if we continue this script and write:

    ADD one, two

We will get 5 because the variable one is now 3 and 2 + 3 = 5.
Again, this applies to all the other math statements.

### SUBTACT Statement

To fully understand how this statement works read the ADD statement docs, this is just a quick example.

    one = 1
    two = 2
    END VARS
    SUBTRACT two, one


### MULTIPLY Statement

To fully understand how this statement works read the ADD statement docs, this is just a quick example.

    one = 15
    two = 2
    END VARS
    MULTIPLY two, one

### DIVIDE Statement

To fully understand how this statement works read the ADD statement docs, this is just a quick example.

    one = 24
    two = 2
    END VARS
    DIVIDE one, two

### FOR 
