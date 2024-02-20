# Django Blog

The project utilizes the Django framework to create a dynamic blog. Key features include creating, editing, and deleting articles, as well as reading and filtering articles based on their publication status. The user interface design focuses on delivering a pleasant user experience.

### Technologies used:

* Django: The main web framework offering powerful web development features.
* HTML/CSS/JavaScript: Used for creating and styling web pages.
* Bootstrap: A CSS framework facilitating responsive design.
* Python: The primary programming language used with Django.
* Git: For version control and tracking code changes.

### Key features:

* User Management: Integration of Django's User model to handle user-related functionalities.
* Publication Model: Use of the BlogPost model to store article information.
* Class-Based Views: Utilization of class-based views to organize controller logic.
* Authentication System: Restricts certain features to authenticated users.
* Automatic Data Storage: Articles are automatically saved in a PostgreSQL database table.
* Image Handling: Use of ImageField to allow articles to have an associated image.

### Deployment Instructions:

1. Clone the repository from Git.
2. Set up the virtual environment and install dependencies.
3. Perform Django migrations to create the database.
4. Run the Django development server.
5. Access the site at the specified URL.
