# XalDigitalChallenge
From the initial email, I received the PDF with instructions you can see in the repo under the name ***instructions.pdf***. I also received a CSV file that you can find in ***./dataset/Sample.csv***.
You can test the solution working online in:
  HTTP://18.223.32.201:4000/users
This link shows the functionality of showing all the elements in the table, for more interactions with the DataBase see the section **Interacting with the DataBase**.

## The solution explained
The process of the solution is as follows:
* First create a Postgres DB and fill it with the received CSV file, which ERD can be found below. I added the column *id* as the primary key.
  * Before creating the table, the script checks if the column state has length 2 and only contains letters   
![Alt text](/img/ERD.png)

* Create the REST API with Python and Flask
* Gather everything together inside a Docker Container.
* Build and deploy the Docker container in an AWS-EC2 RedHat instance.
The diagram for the solution is the following:

![Alt text](/img/app.png)

## Interacting with the DataBase
### Get all users
This is a GET method that list all the content inside the Users table
> HTTP://18.223.32.201:4000/users  

### Create a user
This is a POST method that receives a JSON with key-values equivalent to the ones declared in the Users table definition
> HTTP://18.223.32.201:4000/users
> Example of JSON
> > {first_name:<'first_name'>,
      last_name:<'last_name'>,
      company_name:<ta['company_name'],
      address=data['address'],
      city=data['city'],
      state=data['state'],
      zip=data['zip'],
      phone1=data['phone1'],
      phone2=data['phone2'],
      email=data['email'],
      department=data['department']}
