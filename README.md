# Visa_Approval

lets say yor data is presnet in any cloud platform fro example in this project we have used mongoDB (i keep my connection string in my laptop system environment variable i can load this particular environment variable with the help of operating system package why i kept this particular credential inside my environment variable becasue i dont wat to keep as public if you create any secret credential file credential project insted of keeping hard code we can keep inside environment variable and when you required it at that time you can read fro the environment varibale and its is the most secured way to create a project )so we have to write a component called data ingestion and this is going to be our first component in a pipeline so after data ingestion our data validation will run after data validation our data Transformation will run after that our model training and after model evaluation and model pusher so this is the pipeline we are following  Data ingestion is responsible for fetching data from any data source cloud storage, vector DB, APIs, etc and bringing it into your pipeline. what is artifact mean the generative output lets say after running the code whatever output its generating we have to save somewhere that why we create artifact folder
how to ingest a data 

# pipeline

to run the data ingestion we need constant, constant is nothing just a path let say if i want to create something inside data ingestion folder i have to store inside feature store which is added to constant,  if i want to change any data ingestion file isnted of opening file writing a code we can write a data ingestion constent inside constent folder and we can make it automate after adding data ingestion realted constant we have to add entity 
"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
after running data ingestion we will get train.csv and test.csv our output

DATA VALIDATION after data ingestion we have to execute nest component which data validation, now if we want to validate the data wht we have to do we have first of all we have to load train.csv and test.csv we have to check this particular data whether the data is in correct format or not if there is any data problem or not so the output i am getting from the firt component thta is the input from the next component which is data validation that means this is my artifact so this is caleed artifact entity this mean we are getting some output and this particualr output we are sending for the next component which is data validation and data validation will execute it will give some output and this particular output i have to send to my next component whicg is our data transformation and again data transformation will give some output will send to next comptnent model trainer and the next component is model evaluation and then model pusher, tht mean whenvevr i am executing the pipeline it is taking some input and generating some output and the output is getting to next component and so on and the output actually we are getting this is nothig but our artifact entity to write entity we have to write config entiy firt import everthing inside constant from our_project_name.constant import *

why i hhave kept mongodb_connection in separate file in configuration because lets say whenvevr i want to do data ingestion so whenever i have to make a connection with my nongodb 

modular coding instead of creating aii the code inside one file we are creating a different files our a folders and there you keeping your code and whenever we required it we are calling thta particular code from there only 


entity inside entity we are having two kinds of entity called artifact and config so lets understant what is config entity soto run data ingestion we need constant  constant is nothing just a path let say if i want to create something inside data ingestion folder i have to store inside feature store which is added to constant to manipulate this partivular constant we need something called config entity, what config entity will do it will take the constant and it will make the path 

after daya ingestion we have to execute nest component which data validation

Mongo DB :-if we want to store something to mongoDB so first of all we have to convert the data ta a format call dictionary so there is conveter inside pandas called todict with the help of todict we can convert a scv file to dictionary what is dictionary its having "key" & "value" so with the help of key and value pair we have to store our data to mongoDB unlike in mysql we store the data in schema
data = df.to_dict(orient="records") # it will convert the csv file to dictionary with the help of key and value pair we can store the data to mongodb 
you have to create a data base name inside the cluster and inside database its all the collections

what is Logging whatever statement we are doing in your code  instead of doing the print statement in the terminal we can save in a log file because what happens whenever we production add this particular code in the cloud server there we will be getting any kind of terminal so lets say if any error occur in our application if some kind of failure is there what we can do we can download that particular log file and we can immediately check what is the issue happen inside our code that why logging is very important 

we have to create exception to figure out in which line which file it is having the error and automatically it will figure out 

Utils the functionality we will be using frequently in our code, lets say in this project i am having some yaml file now lets say if i want to read this particular yaml file i have to write a function called read yaml so whenever we need to read the yaml we need to call the particular function lets say i want to read 10 times a particular yaml file  so i have to write again this particular function again 10 time inside my code bit its not a recommended way insted of doing that we can create a main utils so inside that we are going to create this particular function and whenever i required it i'll just import from this particular file (main_utils.py)