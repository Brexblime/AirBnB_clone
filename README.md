AirBnB Clone Project
This project aims to create a simple clone of the AirBnB website, implementing various features and concepts of higher-level programming. The project will be developed in stages, gradually building a web application with a command interpreter, a website, database storage, a RESTful API, and more.

Command Interpreter
The command interpreter is a tool to manage AirBnB objects through a console interface. It allows users to perform operations such as creating new objects, retrieving objects, updating object attributes, and deleting objects. The command interpreter also provides features like counting objects and computing statistics.

How to Start
To start the command interpreter, follow these steps:

Clone the repository to your local machine.
Navigate to the project's root directory.
Run the console.py script using the Python interpreter.

$ ./console.py


How to Use
Once the command interpreter is running, you can use various commands to interact with the AirBnB objects. The available commands include:

create: Create a new object of a specified class.
show: Show the details of a specific object.
all: Show all objects or all objects of a specific class.
update: Update the attributes of an object.
destroy: Delete an object.
count: Count the number of objects or the number of objects of a specific class.
quit: Exit the command interpreter.
To execute a command, type the command followed by any necessary arguments. The command interpreter will process the command and display the appropriate output.

Examples
Here are some examples of using the command interpreter:

$ ./console.py
(hbnb) create User
94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a
(hbnb) show User 94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a
[User] (94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a) {'id': '94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a', 'created_at': '2023-07-14T10:00:00', 'updated_at': '2023-07-14T10:00:00'}
(hbnb) all
["[User] (94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a) {'id': '94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a', 'created_at': '2023-07-14T10:00:00', 'updated_at': '2023-07-14T10:00:00'}"]
(hbnb) update User 94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a name John
(hbnb) show User 94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a
[User] (94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a) {'id': '94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a', 'created_at': '2023-07-14T10:00:00', 'updated_at': '2023-07-14T10:00:00', 'name': 'John'}
(hbnb) destroy User 94a9c6e2-5d54-4bda-bc1f-8a07e4e3d45a
(hbnb) all
[]
(hbnb) quit
$
