# Project 2 Practical Project

## Contents
### 1. [Brief](#Brief)
### 2. [Plan](#Plan)
#### 1. Tools
### 3. [Architect](#Architect)
#### 1. Entity Diagram
#### 2. CI Pipeline
#### 3. Project Tracking
### 4. [Implementation](#Implementation)
#### 1. Swarm
#### 2. Ansible
#### 3. Jenkins
#### 4. HTML Update Page
#### 5. Nginx
### 5. [Risk Assessment](#Risk-Assessment)
### 6. [Testing](#Testing)
### 4. [Future Improvements](#Future-Improvements)



## Brief
The project consisted of creating an application which is curated from 4 micro severs, allowing the user to generate random Objects against a set of predefined rules. This must include full expansion on tasks and tools that are needed to achieve the project goal. Project risks and issues to be recorded in an agile methodology as the development progresses. The application must also make use of the feature branch model within the Version Control System. This system being automated by a CI server and deployed onto a cloud virtual machine.

Requirements:
-	Project tracking board to track progression, full risk assessment to record issues/risks faced during creating project
-	An application fully integrated using the feature-branch model into a VCS, have the app built through a CI server and deployed to a cloud based vm.
-	Webhooks emplaced to automatically recreate and redeploy through CI server Jenkins when changes are made
-	Must be deployed using containerisation and an orchestration tool
-	Make use of an Ansible Playbook
-	Make use of the reverse proxy

## Plan
The project idea consists of taking random objects from a database of brands and clothes and allow the user to generate a combination of the both. This is to be done using 4 micro services, in which each are to depend on each other in order for the application to work.
- Service 1 to render Jinja2 templates to interact with application, this is the front end of the website and will host the output of the generated function for the user. This service will make a request to the micro services to produce this result.
-	Service 2 & 3 simultaneously will generate random objects by requesting the objects from a database. The objects from each table will be split between the two micro services.
-	Service 4 will make a direct request to the previous services 2 and 3, using variables from each to combine the generated objects in a string.
(Create two different implementations of each service)

#### Tools
   - Trello Board
   - Version Control: Git
   - CI Server: Jenkins
   - Configuration Management: Ansible
   - Cloud server: GCP virtual machines
   - Containerisation: Docker
   - Orchestration Tool: Docker Swarm
   - Reverse Proxy: NGINX

## Architect
### Entity Diagram 
![entity](https://github.com/AndreM132/project2/blob/master/pictures/entity.png)

The Entity Diagram displays a brief breakdown of how the database stores the data necessary in order to generate the random objects from each list. This includes a table of Brands, and a table of Clothing items. Each including a primary key, they link directly through the Outfit’s table as this holds the primary key and both foreign keys taken from their respective tables. Essentially, Service 2 holds the Brands data and service 3 is to manage the Clothes data. Service 4 consisting of the Outfit’s table in order to generate the objects at random it connects the tables through the databases together to produce the output string of text. 

### CI Pipeline
![cipipeline](https://github.com/AndreM132/project2/blob/master/pictures/Pipeline2edit.jpg)

The CI (Continuous Integration) pipelines takes advantage of the technologies stated within the requirements. This begins with the code fed directly into the Version Control System known as Git, using Github as the host repository location. Github remaining the most effective and useful tool to handle the code and easily push updates to a selected feature branch enabling you to make changes and deletions without having to affect the master branch. The project progression was tracked using the software Trello board, in which is to be explained in the following sections. Continuous Integration server Jenkins is used to automate the installation files as well as handling the deployment of the application keeping it live. The Google Cloud Platform (GCP) was the tool used to create the necessary virtual machines to create and run the application, also being the foundation for the Database using MySQL. 

Docker is used to containerise the application enabling it to run all together rather than separated, this is also assisted by the technology Docker Swarm & Stack as the orchestration tool. This allows the application to deploy much quicker and efficiently as a single command line will run the application stack. Stack also ensures each micro server has a replica server to keep the app actively running with little to no downtime. Dockerhub is used as the version control for the Docker Images and Containers. Ansible handles the configuration management of the application, while NGINX remotely access the application from the master node and is able to present the app live from its IP address link. 

Standard HTML was used for the front-end design of the application GUI in which users were to only see and be able to interact with. The application ran using the software Flask through GCP which worked as the bridge between the front and back end design. In order to use python code within the HTML, Jinja2 offered the ability to pass variables through the programming language and HTML. Finally, MySQL gave access to the SQL database in which held the data necessary to generate random objects. 


### Project Tracking
A Trello board was used to track the progression of the project overall from start to finish, showing the planning and steps necessary that were required to achieve the task at hand. The project worked in two different sprints, stating the initial project plans and approach along with the newer project plan and structure. The process worked in an Agile method as all sections of the project had been worked on simultaneously for most of the time or completed in sections together.

![projecttrack](https://github.com/AndreM132/project2/blob/master/pictures/project2firstsprint.JPG)

First Sprint: In the first sprint user stories had been defined, outlining what was important for the user to be able to access and interact with. The user ideally would produce a short story from a button click function that would take use of the randomly generated objects and display the story on the HTML page. The planning tracked the main areas to focus on to create the application, and the necessary steps to document its progress. Testing plans were also outlined.


![projecttracktwo](https://github.com/AndreM132/project2/blob/master/pictures/project2secondsprint.JPG)

Second Sprint: The second sprint features the project plan change, refining the user stories to ensure they’re in line with what the user will be able to do on the new application. Planning stages were tweaked to keep on track with what the objectives were, as well as the progress stage to keep informed of what’s currently being worked on. Some tasks that were completed were output into the finished section, and some testing stages necessary had been outlined.

![projecttrackthree](https://github.com/AndreM132/project2/blob/master/pictures/project2finishedsprint.JPG)

Final Sprint: The final view of the project sprint cycle as all stages were completed and moved to the relevant section. This included the completion of testing for the application.


## Implementation
The application had been through a couple different design phases and ideas as stated within the project planning. The first idea was to produce short stories dependant on the theme and setting that each were randomly generated. On a button click, the user would generate two random objects from each database table to see a string of text on the HTML GUI with their theme, setting and story. 
Yet this idea was simplified to a better idea of giving the user the ability to win randomly generated clothing items from random brands through a dynamic updating url link per click. The micro service application was successful, producing a new brand and clothing item on the home page upon clicking the ‘Home’ link or refreshing the page. The application had been Dockerized by placing the micro services into a container, and making use of Docker swarm orchestration tool which enabled the application to deploy effectively. Jenkins automated the deployment of the application. 

![implementation](https://github.com/AndreM132/project2/blob/master/pictures/homepage-project2.JPG)

Home Page: The HTML Home Page acted as the output location for the randomly generated objects. A string was produced letting the user know they won the randomly generated branded clothing items. Upon refreshing the page or clicking on the home navigation url link, a new pair of objects taken from the database utilised within micro services 2, 3 and 4 produced on screen in the first micro service application. Due to the replica services and constant live state of the application supported by Jenkins, the page could be refreshed at a quick rate and giving the ability to be clicked enough times to responsively always have new items generated.

![implementation](https://github.com/AndreM132/project2/blob/master/pictures/brandsandclothes-project2.JPG)

Brands and Clothes page: The second page held the databased stored items of all the Brands and Clothes. Yet this gave the user the ability to see the previously stored winning items in a list format. It also added new entities upon each link refresh of the home page as new objects were being generated. Each pair had also been added directly into the MySQL database table Outfit to keep a record of all the winning items.

### Swarm
![swarm](https://github.com/AndreM132/project2/blob/master/pictures/swarmproject2.JPG)

Connecting each micro service’s application together via a network created, the orchestration tool efficiently replicated each micro service to secure the stability of the network to keep it live for the users. Shown in the diagram are the application containers created for swarm.

### Ansible
![ansible](https://github.com/AndreM132/project2/blob/master/pictures/ansible.JPG)

Ansible worked as the configuration management for the project. This held the responsibility of initialising the Docker swarm to be able to deploy the application. The tool also initialised the worker node as the generated ssh keys were to be emplaced in. This connected the nodes together through the same network, allowing each virtual machine to be accessed from another. By successfully setting up the master and each worker role through Ansible, the application was then ready to be built and deployed through the Jenkins pipeline. Ansible also preinstalled Docker on the machine so it’s accessible when at the build stage.

### Jenkins
![jenkins](https://github.com/AndreM132/project2/blob/master/pictures/jenkinsworksdone.JPG)

This CI server takes pre-written scripts reading them as rules to build and run the system intended, connecting to Github via webhooks. This happens by the script folder created within the project code, setting up a Jenkinsfile that contains a pipeline design that handles the build, the deployment and the ansible playbook command to run the pre-configurations. The build file sets up Docker-compose build and pushes it to Docker as the sudo user, enabling Jenkins during each update to run the Docker-compose commands. The project is then deployed through the deploy script, ssh into the user as the Ansible playbook is configured for the Jenkins user. This includes within the body of the code setting up the project directly as well as the bashrc and setting up the environment variables upon each trigger of the deployment command. Prior to the deployment, the Ansible script executes the playbook file to run Ansible.

The pipeline had been set up to enable the scripts to be executable before accessing them as without it Jenkins will not run the said scripts. The stage then moves onto building the application as this is handled by previously stated build and Ansible scripts. Once built, the Deployment stage commenced, running the deploy script to keep the application automatically live through its IP address and port, accessible to the user with little downtime. 

Jenkins saves the deployment of the application through its pipeline design, ensuring once the environment variables are exported to activate the database the application can deploy through Docker stack. Running the service stackapp due to it being live from the build configuration, the application is live on the HTML url link and continuously live. 

From the diagram above this shows the stage view of Jenkins, presenting the execution, build and deployment of the application with a list of successful builds. Due to how Jenkins is set up through its pipeline, each time a new change is committed to the master branch via Github Jenkins is to automatically trigger through webhooks that connect the two services together. The webhook once fed the Jenkins IP address and correct port, will inform Jenkins of the change as soon as it has been pushed. The service is able to log reports on its successful or failed builds as the blue dots by the number listed builds ran in its history, represent the successful deployment of the application. Above this the weather symbol states the history of the Jenkins builds, meaning no recent builds have failed its automation, running at 100% coverage.

### HTML Update Page
![htmlup](https://github.com/AndreM132/project2/blob/master/pictures/updatedhomepage.JPG)

Through the stable update of Github being automatically applied to the HTML page via webhooks directing into the CI server Jenkins, on refreshing the page or clicking the Home url link the application is automatically updated with information displayed on the page.

### Nginx
![nginx](https://github.com/AndreM132/project2/blob/master/pictures/nginx.JPG)

A 5th service was included within the project spec, thus being the Nginx service. This node hosted the configuration file for the reverse proxy feature between ports 80 and 5000, giving the ability to run the application remotely from the nginx container as it refers to the master node and its port. When the nginx link is accessed, the running application displayed on the HTML GUI created.

## Risk Assessment
![riskassess](https://github.com/AndreM132/project2/blob/master/pictures/riskassess.JPG)

The Risk Assessment takes a deeper look into some possible risks that occur during the process of building the application, as well as some possible future risks that could occur. It scales through different areas such as the database, server and possible VCS risks that could affect the integrity of the application. The Risk and Impact of the occurrence is evaluated, with a proposed mitigation solution to solve the possible risk. The responsibility is stated of who has ownership of handling the risk, as well as how tolerable the situation would be theoretically.

## Testing
The application was unit tested on all micro services to see how the system holds up and if it’s performing the actions required. This takes the application folder of each micro service and runs tests against its performance, producing a coverage report showing each tests’ cover percentage. The coverage proves how efficient and effective the code is in order to create the application. Each test featured unit testing the creation of the database and the teardown, ensuring the SQL instance is active and able to obtain generated objects from. This also includes the configuration testing for the database environment set up, obtaining the test database and test secret key.

![py1](https://github.com/AndreM132/project2/blob/master/pictures/pytestapp1.JPG)

App 1 Test Coverage: The first application where it provides the environment and setup of what the user will see, had passed with 100% coverage. The unit test mock was a tool featured to replicate a result from the running application to check if the same result is produced in order to pass the test. This was present within the home page view test, checking is the get request gives the correct response code of 200 which states the page display. The second page, Brands and Clothes was also tested making sure it’s consistently accessible.

![py2](https://github.com/AndreM132/project2/blob/master/pictures/app2test.JPG)

App 2 Test Coverage:  App 2’s micro service covered the Brands of the database, randomly generating a brand within a list of 10 options for the user to be selected from. The unit tests applied on testing the brands service testing if it was successfully running, as well as creating a test brand within the generator function and asserting it back to check if the result would pass suitable.

![py3](https://github.com/AndreM132/project2/blob/master/pictures/app3test.JPG)

App 3 Test Coverage:  App 3’s tests carried out the same as the Brands micro service, where this application focused on generating the Clothing items of the database from a selection of 10. The service is tested to ensure a random clothing item will generate as it creates a mock entity into the test database replicating the MySQL process. If returned successful, the test will pass.

![py4](https://github.com/AndreM132/project2/blob/master/pictures/app4test.JPG)

App 4 Test Coverage:  The bulk of the micro services connecting together remained within app 4. The outfit database was referred to in the unit mock testing stage, checking if the correct values are returned from their respective services 2 and 3. If the names of the items were present in the database and the application was able to print out the randomized objects to screen then the test would pass.

## Future Improvements
The project would benefit from more functionality on the HTML pages for the users to interact with. Such as a button so they can choose when they would like to generate a new selection of randomized objects. The user ideally should be able to use the button click that on the front end GUI will display the clothing item and brand as titles, with a string line beneath stating they have won. A special message appearing when the user has won a specific combination of randomly generated objects could grant the user another branded clothing item as a bonus in a text box below the winning line.

An improvement on the use of tools for the project would also be beneficial, such as improving knowledge with Groovy syntax and applying a better use of the Jenkins pipeline such as enable it to run tests once the application is live. This would allow the use of Jenkins to become a more significant purpose in its automation as reports could be generated on test coverage and performance of the application. 

Unit testing could be improved, including improved test percentages in each report from running pytest on each of the micro services. This would give a clear view of the full application thoroughly tested and displayed in the testing section. This also proves beneficial to the application as the higher the percentage pass rate, the more efficient the code produced has proven to be and shows there are no lines of code missing that haven’t yet been tested.

