# bf-copy
A clone of BrainFuck in Python made to use as less space as possible.
<br>
<br>
# Tutorial
<br>

## How does it work?
It's pretty much like bf (BrainFuck):
There's about 10000 cells, all at 0 by default and can only contain numbers.
And a pointer which can go from left to right between the cells and modify the value which the it is pointing at.
You can print on the console the cell corresponding to its value in ASCII, assuming the pointer is on the first cell which has a value of 103: when you will print it, it will print *g* because 103 is "g" in ASCII. You can also print the actual value: meaning on the 103, it will actually print 103 and not *g*, which is pretty useful for debugging and bf doesn't have it. Another new feature (compared to bf) is that you can output the 10000 cells and their value, again useful for debugging too.
<br>

## Commands
```i```
The command ***i*** increments the cell value which is being pointed at by the pointer by 1. <br>
```d```
The command ***i*** decrements the cell value which is being pointed at by the pointer by 1. <br>
```()```
The delimiters ***(*** and ***)*** repeat the code between them until the current value of the cell which the pointer is pointing at is 0. <br>
```^```
The command ***^*** increments the pointer value by 1. <br>
```v```
The command ***v*** decrements the pointer value by 1. <br>
```!```
The command ***!*** prints the ASCII value of the value of the cell which is being pointed at. <br>
```§```
The command ***§*** prints the value of the cell which is being pointed at. <br>
```m```
The command ***m*** prints the value of the 10000 cells. <br>
