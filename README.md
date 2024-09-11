PWS link :

Explain how you implemented the checklist above step-by-step (not just following the tutorial):
My approach to the implementation was to first think about the overall structure of the project and how the different components would fit together. My main goal was to set up the Django project and the "main" app in a way that covered all the requirements. I started by creating the project and app, keeping the required fields—`name`, `price`, and `description`—in mind for the model. I also wanted to make the model more flexible, so I added other fields like `stock` to manage the products better.
For the function in `views.py`, my reasoning was straightforward: I needed to display some basic information in a template. I kept it simple, just showing the required details (app name, my name, and class). This allowed me to focus on making the code clean and functional without adding unnecessary complexity.
When it came to routing, I wanted it to be smooth and easy to follow, so I linked the views and URLs in a logical way. As for deployment, I made sure everything was correctly set up to run online, but the key was making sure the application worked well in production once it was deployed.

Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
![Graph](./graph.png)

Explain the use of git in software development!
Git is a widely used version control system in software development that helps teams track changes to code, manage collaboration, and maintain multiple versions of a project. It allows developers to work on isolated branches for new features or bug fixes without interfering with the main codebase, enabling parallel development. Changes are tracked as commits, which can be reviewed, reverted, or merged with other code, providing a detailed history of the project. Git also simplifies collaboration by helping to resolve conflicts when multiple developers contribute to the same files.

In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
Django is a great starting point for learning software development because it offers a "batteries-included" approach, providing many essential features like an ORM, authentication, and admin interface right out of the box. This allows beginners to focus on learning the core concepts of web development without worrying about setting up basic components. Additionally, Django encourages best practices through its emphasis on clean, maintainable code and has extensive documentation, making it easier for newcomers to follow along. Its scalability and versatility also make it a good framework to use for both small projects and real-world applications.

Why is the Django model called an ORM?
Django's model is called an ORM (Object-Relational Mapping) because it allows developers to interact with the database using Python objects instead of writing SQL queries. The ORM maps database tables to Python classes, where each class represents a table and each attribute corresponds to a field in that table. This abstraction simplifies database operations, letting developers create, retrieve, update, and delete records using Python code. The Django ORM automatically handles translating these operations into SQL, making database management easier and more intuitive for developers working in an object-oriented language.
