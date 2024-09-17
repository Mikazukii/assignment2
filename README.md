PWS link :

Homework 2

**Explain how you implemented the checklist above step-by-step (not just following the tutorial):**
My approach to the implementation was to first think about the overall structure of the project and how the different components would fit together. My main goal was to set up the Django project and the "main" app in a way that covered all the requirements. I started by creating the project and app, keeping the required fields—`name`, `price`, and `description`—in mind for the model. I also wanted to make the model more flexible, so I added other fields like `stock` to manage the products better.
For the function in `views.py`, my reasoning was straightforward: I needed to display some basic information in a template. I kept it simple, just showing the required details (app name, my name, and class). This allowed me to focus on making the code clean and functional without adding unnecessary complexity.
When it came to routing, I wanted it to be smooth and easy to follow, so I linked the views and URLs in a logical way. As for deployment, I made sure everything was correctly set up to run online, but the key was making sure the application worked well in production once it was deployed.

**Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.**
![Graph](./graph.png)

**Explain the use of git in software development!**
Git is a widely used version control system in software development that helps teams track changes to code, manage collaboration, and maintain multiple versions of a project. It allows developers to work on isolated branches for new features or bug fixes without interfering with the main codebase, enabling parallel development. Changes are tracked as commits, which can be reviewed, reverted, or merged with other code, providing a detailed history of the project. Git also simplifies collaboration by helping to resolve conflicts when multiple developers contribute to the same files.

**In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?**
Django is a great starting point for learning software development because it offers a "batteries-included" approach, providing many essential features like an ORM, authentication, and admin interface right out of the box. This allows beginners to focus on learning the core concepts of web development without worrying about setting up basic components. Additionally, Django encourages best practices through its emphasis on clean, maintainable code and has extensive documentation, making it easier for newcomers to follow along. Its scalability and versatility also make it a good framework to use for both small projects and real-world applications.

**Why is the Django model called an ORM?**
Django's model is called an ORM (Object-Relational Mapping) because it allows developers to interact with the database using Python objects instead of writing SQL queries. The ORM maps database tables to Python classes, where each class represents a table and each attribute corresponds to a field in that table. This abstraction simplifies database operations, letting developers create, retrieve, update, and delete records using Python code. The Django ORM automatically handles translating these operations into SQL, making database management easier and more intuitive for developers working in an object-oriented language.

Homework 3

**Explain why we need data delivery in implementing a platform.**  
Data delivery is essential in implementing a platform because it enables the efficient transfer of data between different components, services, or users. Without reliable data delivery, a platform cannot function smoothly, as users or systems would not be able to send, receive, or process the necessary information to perform their tasks. Proper data delivery ensures synchronization, communication, and overall system functionality.

**In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?**  
JSON is generally considered better than XML for most modern applications due to its simplicity and readability. JSON’s lightweight structure makes it faster to parse and easier for both humans and machines to process, especially in web development. It has become more popular than XML because it integrates well with JavaScript, requires less code, and is easier to manipulate, making it ideal for APIs and data exchange in web environments.

**Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.**  
The `is_valid()` method in Django forms is used to validate form data against the predefined form fields and their rules. It checks whether all required fields are filled, ensures that data types are correct, and applies any custom validation logic. This method is crucial because it allows developers to ensure that only clean and valid data gets processed or saved, preventing potential errors or malicious inputs in the application.

**Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?**  
The `csrf_token` in Django forms protects against Cross-Site Request Forgery (CSRF) attacks by ensuring that the request comes from a trusted source. If a form does not use `csrf_token`, an attacker could exploit this vulnerability by tricking users into unknowingly submitting malicious requests. This could result in unauthorized actions, such as data manipulation or security breaches within the platform.

**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**
I tried first to have the concept of product with the attribute which are going to be in the form
Then I implemented it on the models.py, forms.py and views.py
Finally I add the other functions for apply the good format (JSON/XML) to the data added.

**Postman results (4 screens)**
![Screen1](./postman_xml.png)
![Screen2](./postman_json.png)
![Screen3](./postman_xml_id.png)
![Screen4](./postman_json_id.png)
