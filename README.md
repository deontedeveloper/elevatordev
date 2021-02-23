Assigned to:
<p>This project developes the code for a model elevator of 2 cars runs on a raspberry pi 3 <br>
<br>
<h2>TO CLONE</h2>

-git clone https://github.com/sdev265ev/elevator.git<br>
<br>
**HISTORY** <br>

One year ago AHI funded the building of a tabletop model prototype. <br>
The general requirements was the prototype controller and software must control a five (5) floor elevator prototype. <br>
There was an understanding that project was likely to be more complex than initially anticipated.<br>
<br>
The prototype was constructed to discover and identify issues. <br>
The previous team confirmed that Raspberry Pi(s) are capable of controlling a prototype model elevator<br>
<br>
**CURRENT STATUS** <br>

<br>
With the success of the prototype, AHI has agreed to continue funding the project to scale up the model and add features<br> 
with a new team of developers. The model and software will implement as many “normal” passenger elevator functions as possible. <br>
<br>
</p>



**MASTER (raspberry pi)**<br>

<p>
[x]gets button presses<br>
[x]Gets car location<br>
[x]Maintain floor lists<br>
[x]Send floor stop lists to cars<br>
[ ]Computes car movement priority <br>
</p>


**CAR 1 control (raspberry pi)**
<p>
[x]Move car up/down<br>
[x]Controls door<br>
[x]Knows location<br>
[x]Monitor floor button<br>
[x]Turns lamp on/off<br>
[x]Send car info to master<br>
[x]Receives floor stop list from master<br>
</p>

**CAR 2 control (Raspberry PI)**
<p>
[x]Move car up/down<br>
[x]Controls door<br>
[x]Knows location<br>
[x]Monitor floor button<br>
[x]Turns lamp on/off<br>
[x]Send car info to master<br>
[x]Receives floor stop list from master<br>
</p>

**Monitor Hallway Buttons (Raspberry PI)**
<p>
[x]Controls Hall Way LAMP<br>
[x]Send button info to master<br>
</p>
