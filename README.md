PWS link :

Explain how you implemented the checklist above step-by-step (not just following the tutorial):
My approach to the implementation was to first think about the overall structure of the project and how the different components would fit together. My main goal was to set up the Django project and the "main" app in a way that covered all the requirements. I started by creating the project and app, keeping the required fields—`name`, `price`, and `description`—in mind for the model. I also wanted to make the model more flexible, so I added other fields like `stock` to manage the products better.

For the function in `views.py`, my reasoning was straightforward: I needed to display some basic information in a template. I kept it simple, just showing the required details (app name, my name, and class). This allowed me to focus on making the code clean and functional without adding unnecessary complexity.

When it came to routing, I wanted it to be smooth and easy to follow, so I linked the views and URLs in a logical way. As for deployment, I made sure everything was correctly set up to run online, but the key was making sure the application worked well in production once it was deployed.

![Graph](./Client-browser.png)
