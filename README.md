<h1>Intercars background</h1>
<p>
Intercars Leicester is an ambitious car dealership based in Leicester.<br>
They are very active in auctions in the east and west midlands.<br>
They have basic data collection techniques which could be significantly<br>
improved to enable them to gain greater insight from the data they collect<br>
which would in turn drive profitable decisions.
</p>

<h3>The project</h3>
<p>
Intercars Leicester were approached with the concept of migrating all their<br>
data which at the time was kept in paper form into an on premises MySQL database<br>
with a dedicated server laptop which could be connected to from any other laptops<br>
via ssh or via a GUI.<br>

This is the second part of this discontinued project. Herein is the GUI development<br>
with Python and Kivy interacting with the MySQL database.

</p>

<h4>The project plan</h4>

<p>

The objective of this project is to develop a graphical user interface, GUI, that would<br>
enable non technical staff to interact with the database to accomplish the following:

<ul>

<li> <b>Data entry:</b> This simplifies data entry such that<br>you don't have to know sql to enter data into the database.<br>The hard work is done in the background using python and sql</li>
<li> <b>Data retrieval and summaries:</b> Users will be able to retrieve tabulated data<br>and to view pre-defined charts and graphs of useful metrics<br>without knowing Python or sql programming.</li>

</ul>

All of this is made possible using python and sql in the background.

</p>

<h4>KV code</h4>

<p>
The GUI frontend is designed with Kivy. The KV files are the codes for the various screens/pages that the user interacts with.<br>
These screens are then linked with the python codes in the background, the backend, which either pulls data or displays data to and fro.

</p>


<h4>Python code</h4>

<p>

The python code consists of classes and functions which are designed to interact with the GUI via the .kv files and the database.<br>
Firstly, the python code pulls data from the GUI and performs any transformation necessary then sends it to the database.<br>

The sql codes used for inserting data into the database, work with the procedures and triggers in the database<br>
i.e. they are coded with the procedures and triggers in mind; such that when the data reaches the database the<br>
procedures and triggers transport the ready data to their final destination.<br>

For data retrieval, python codes are used to pull raw tabulated data and summaries from the database<br>
then it displays the outputs on the GUI via tabs for viewing. Example illustrations can be found on <a href="https://github.com/ManunEbo/Intercars-DB-GUI/tree/master/2.%20Sample%20GUI%20Illustrations">2. Sample GUI Illustrations</a>

<p>

Unfortunately, the requirements.txt for this project is missing i.e. unretrievable.<br>
However, it included:

<ul>

<li>python 3.8</li>
<li>python-mysql-connector</li>
<li>sqlalchemy</li>
<li>matplotlib</li>
<li>Numpy</li>
<li>Pandas</li>
<li>Kivy</li>
<li>Kivymd</li>
<li>MySQL</li>

</ul>

</p>


<p>
Since the project was discontinued and Intercars did not object to the publishing of<br>
this body of work to illustrate my capabilities, in additions to me owning this project,
I have decided to publish it publicly.

<b>Note:</b> This project is part 2 of the discontinued project.<br>
You can find the first part, Intercars-DB here <a href="https://github.com/ManunEbo/Intercars-DB">Intercars-DB</a>
<br><br>
The whole project was certainly an enjoyable experience: I learned a great deal, in a very short period of time.

</p>








