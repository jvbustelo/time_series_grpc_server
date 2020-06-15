# Time Series gRPC Server
Server side of the gRPC time series assignment.

This server was created with the packages grpcio and grpcio-tools. The proto file was defined in the first place, set in both server and client and then the generation of the protocol buffer files was done by the compiler based on this proto file.

The project is divided in a modular fashion. The meter readings data is stored in the data folder. All files which run and support the server are in the server_app folder. Finally, there is a tests folder.

The server app has been created with an OOP approach, definining an actor for each necessary action. This enables readability, maintainability and extensibility. All the actors can be easily modified or extended with new functions if new requirements were to arise. Note that for such an simple example, this approach might seem like overdoing, yet it has been chosen for the sake of presentability.

# How to run the server
Clone the repository and in your virtual environment's terminal run:

```pip install -r requirements```

You are almost ready to go. Run the ```__main__.py``` file located in the root directory. If you wish to specify a specific port to expose, you can do so by setting the ```port``` variable to the ```Server.run()``` function in the file. Make sure you specify the same port number for the client!
