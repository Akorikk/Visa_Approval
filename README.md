# Visa_Approval

Data ingestion is responsible for fetching data from any data source cloud storage, vector DB, APIs, etc and bringing it into your pipeline.

Mongo DB :-if we want to store something to mongoDB so first of all we have to convert the data ta a format call dictionary so there is conveter inside pandas called todict with the help of todict we can convert a scv file to dictionary what is dictionary its having "key" & "value" so with the help of key and value pair we have to store our data to mongoDB unlike in mysql we store the data in schema
data = df.to_dict(orient="records") # it will convert the csv file to dictionary with the help of key and value pair we can store the data to mongodb 
you have to create a data base name inside the cluster and inside database its all the collections

what is Logging whatever statement we are doing in your code  instead of doing the print statement in the terminal we can save in a log file because what happens whenever we production add this particular code in the cloud server there we will be getting any kind of terminal so lets say if any error occur in our application if some kind of failure is there what we can do we can download that particular log file and we can immediately check what is the issue happen inside our code that why logging is very important 

we have to create exception to figure out in which line which file it is having the error and automatically it will figure out 