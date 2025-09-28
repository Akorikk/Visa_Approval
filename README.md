# Visa_Approval

Data ingestion is responsible for fetching data from any data source cloud storage, vector DB, APIs, etc and bringing it into your pipeline. what is artifact mean the generative output lets say after running the code whatever output its generating we have to save somewhere that why we create artifact folder
how to ingest a data 

Mongo DB :-if we want to store something to mongoDB so first of all we have to convert the data ta a format call dictionary so there is conveter inside pandas called todict with the help of todict we can convert a scv file to dictionary what is dictionary its having "key" & "value" so with the help of key and value pair we have to store our data to mongoDB unlike in mysql we store the data in schema
data = df.to_dict(orient="records") # it will convert the csv file to dictionary with the help of key and value pair we can store the data to mongodb 
you have to create a data base name inside the cluster and inside database its all the collections

what is Logging whatever statement we are doing in your code  instead of doing the print statement in the terminal we can save in a log file because what happens whenever we production add this particular code in the cloud server there we will be getting any kind of terminal so lets say if any error occur in our application if some kind of failure is there what we can do we can download that particular log file and we can immediately check what is the issue happen inside our code that why logging is very important 

we have to create exception to figure out in which line which file it is having the error and automatically it will figure out 

Utils the functionality we will be using frequently in our code, lets say in this project i am having some yaml file now lets say if i want to read this particular yaml file i have to write a function called read yaml so whenever we need to read the yaml we need to call the particular function lets say i want to read 10 times a particular yaml file  so i have to write again this particular function again 10 time inside my code bit its not a recommended way insted of doing that we can create a main utils so inside that we are going to create this particular function and whenever i required it i'll just import from this particular file (main_utils.py)