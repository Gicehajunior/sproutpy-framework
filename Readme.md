## SproutPy- Python Framework for Streamlined Development

SproutPy is a Python framework designed to accelerate your web application development by providing a structured template architecture. It offers a foundation for building well-organized and maintainable projects, allowing you to focus on the core functionalities of your application.

### Getting Started

**Prerequisites-**

* Python (version 3.x recommended)
* Node.js and npm (for asset building)
* A code editor or IDE of your choice (e.g., Visual Studio Code, PyCharm)

**Installation (Coming Soon!)**

There are two ways to get started with SproutPy-

1. **Install from PyPI (Future Release)-**
   * Once SproutPy is available on the Python Package Index (PyPI), you can install it using pip-
     
     ```bash
     pip install sproutpy
     ```

2. **Clone the Repository (Current Development)-**
   * If you want to contribute to the development of SproutPy or use the latest features, you can clone the Git repository-
     
     ```bash
     git clone https-//github.com/Gicehajunior/sproutpy-framework.git
     cd sproutpy-framework
     ```

**Building Assets-**
SproutPy uses Node.js for asset management. After cloning the repository, follow these steps to build assets-

```bash
npm install
npm run build
```

This will install the required dependencies and build the assets for your application.

**Starting the Development Server-**
Once the assets are built, you can start the development server-

```bash
python serve.py
```

**Basic Project Structure**

SproutPy provides a pre-defined directory structure to organize your project effectively. Here's a general outline-

* **app** - This directory contains the core application logic, including controllers, models, middlewares, utilities, and services.
* **config** - This folder stores configuration settings for your application, such as mail, database, and other configurations.
* **requirements.txt** - This file lists the external dependencies required by your project.
* **resources** - This folder contains static file views, houses authentication templates, and other resources.
* **routes** - This folder houses all routes to be used in the application.
* **public** - This folder houses public assets for the application.
* **tests** - This directory is dedicated to writing unit tests for your application code.

**Documentation (Coming Soon!)**

Comprehensive documentation for SproutPy, including detailed explanations of components, usage guides, and best practices, will be available soon.

### Contributing (Welcome!)

SproutPy is under active development, and we welcome contributions from the community. Here's how you can get involved-

* **Report Issues-** If you encounter any bugs or have suggestions for improvement, please raise an issue on the GitHub repository.
* **Pull Requests-** If you've developed a new feature or fixed an existing issue, submit a pull request for review and potential integration.
* **Discussions-** Feel free to join discussions on the GitHub repository to share ideas and collaborate on SproutPy's development.

We appreciate your interest in SproutPy! Stay tuned for further updates and advancements in the framework.

