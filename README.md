# Football App User Manual

## Introduction

- What the application does (displays Premier League stats)
- Who this manual is for (non-technical users)

## 1. Getting Started: Prerequisites

- What you need before you begin
- Installing Python (with step-by-step instructions for Windows, macOS, and Linux)
- Installing Git (with step-by-step instructions for Windows, macOS, and Linux)
- Installing PostgreSQL (with step-by-step instructions for Windows, macOS, and Linux)
- Verifying installations

## 2. Setting Up the Application

- Downloading the code from GitHub
- Creating a project folder
- Setting up a virtual environment
- Installing required packages

## 3. Running the Application

- Initializing the database
- Scraping the data
- Starting the web server
- Accessing the application in your browser

## 4. Troubleshooting & FAQs

- Common errors and how to fix them
- Frequently asked questions

## 5. Conclusion

- Summary of what you've accomplished
- How to get further help


## Introduction

Welcome to the user manual for your new Football App! This application is designed to provide you with up-to-date statistics and insights from the Premier League, including top scorers, clean sheets, and hat-tricks. It transforms raw data into an engaging and easy-to-understand dashboard, complete with interactive charts and professional visuals.

This manual is created specifically for non-technical users, meaning you don't need any prior programming knowledge to get this application up and running on your own computer. We will guide you through every step, from preparing your computer to viewing the live statistics in your web browser. Our goal is to make this process as straightforward and hassle-free as possible, ensuring you can enjoy your new football statistics dashboard with ease.

By following the instructions in this manual, you will learn how to:

*   **Prepare your computer**: Install the necessary foundational software.
*   **Set up the application**: Download the application code and configure its environment.
*   **Run the application**: Start the application and populate it with the latest data.
*   **Access the dashboard**: View the Premier League statistics in your web browser.

Let's get started!

## 1. Getting Started: Prerequisites

Before we can set up and run the Football App, there are a few essential tools you need to have installed on your computer. Think of these as the foundational building blocks that allow the application to function correctly. Don't worry if you don't have them yet; we'll walk you through the installation process step-by-step for different operating systems.

### 1.1. Installing Python

Python is a programming language that the Football App is built upon. You'll need a specific version of Python (Python 3.x) for the application to work. Follow the instructions below based on your computer's operating system.

#### 1.1.1. For Windows Users

1.  **Download Python**: Open your web browser and go to the official Python website: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) [1].

2.  **Choose the Installer**: Look for the latest stable release of Python 3.x. For example, if the latest is Python 3.11.x, you would look for a link like "Windows installer (64-bit)" or "Windows installer (32-bit)" depending on your system. Most modern computers are 64-bit. If you're unsure, you can usually find this information in your system settings (e.g., right-click on "This PC" or "My Computer" and select "Properties").

3.  **Run the Installer**: Once the download is complete, locate the downloaded file (it will usually be in your "Downloads" folder) and double-click it to start the installation process.

4.  **Important Step: Add Python to PATH**: In the first screen of the installer, make sure to check the box that says **"Add Python X.X to PATH"** (where X.X is the version number, e.g., 3.11). This is a crucial step that allows your computer to find Python from any command prompt window. If you miss this, you might encounter errors later.

5.  **Proceed with Installation**: Select "Install Now" (recommended for new users) and follow the on-screen prompts. The installation might take a few minutes.

6.  **Finish Installation**: Once the installation is complete, you will see a "Setup was successful" message. Click "Close".

#### 1.1.2. For macOS Users

1.  **Download Python**: Go to the official Python website: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/) [2].

2.  **Choose the Installer**: Download the latest stable Python 3.x macOS installer (e.g., `python-3.11.x-macos11.pkg`).

3.  **Run the Installer**: Open the downloaded `.pkg` file. This will launch the Python installer.

4.  **Follow Prompts**: Follow the on-screen instructions. You can generally accept the default options. The installer will guide you through the process, including agreeing to the license and selecting an installation location.

5.  **Complete Installation**: Once finished, click "Close". Python will be installed in your Applications folder, and the installer will usually set up the necessary PATH variables for you.

#### 1.1.3. For Linux Users (Ubuntu/Debian-based)

Most Linux distributions come with Python pre-installed. However, it might be an older version (Python 2.x) or not the specific Python 3.x version we need. We recommend ensuring you have Python 3.x and `pip` (Python's package installer) installed.

1.  **Open Terminal**: You can usually open a terminal by pressing `Ctrl + Alt + T` or by searching for "Terminal" in your applications menu.

2.  **Update Package List**: Run the following command to update your system's package list:
    ```bash
    sudo apt update
    ```
    You might be asked for your password. Type it in and press Enter (the characters won't show as you type).

3.  **Install Python 3 and pip**: Now, install Python 3 and pip (Python's package installer) by running:
    ```bash
    sudo apt install python3 python3-pip -y
    ```
    The `-y` flag automatically confirms the installation, so you won't be prompted to type 'Y' or 'N'.

### 1.2. Installing Git

Git is a version control system that allows us to download the application code from GitHub, a platform where developers store and manage their projects. You'll need Git to get the Football App onto your computer.

#### 1.2.1. For Windows Users

1.  **Download Git**: Go to the official Git website: [https://git-scm.com/download/win](https://git-scm.com/download/win) [3]. The download will usually start automatically.

2.  **Run the Installer**: Locate the downloaded `.exe` file and double-click it.

3.  **Follow Prompts**: The Git installer has many options. For most users, accepting the default options is perfectly fine. Click "Next" through the various screens until the installation begins. The most important part is ensuring Git is added to your PATH, which is usually the default setting.

4.  **Finish Installation**: Once complete, click "Finish".

#### 1.2.2. For macOS Users

There are several ways to install Git on macOS. The easiest is often by installing Xcode Command Line Tools or Homebrew.

**Option 1: Install via Xcode Command Line Tools (Recommended for simplicity)**

1.  **Open Terminal**: Go to Applications > Utilities > Terminal.

2.  **Install Command Line Tools**: Type the following command and press Enter:
    ```bash
    xcode-select --install
    ```
    A software update pop-up will appear. Click "Install" and agree to the terms. This will install Git along with other developer tools.

**Option 2: Install via Homebrew (Recommended for developers, but also easy for users)**

1.  **Install Homebrew (if you don't have it)**: Homebrew is a popular package manager for macOS. If you don't have it, open Terminal and paste the following command:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    Follow the on-screen instructions, which might include entering your password.

2.  **Install Git**: Once Homebrew is installed, simply run:
    ```bash
    brew install git
    ```

#### 1.2.3. For Linux Users (Ubuntu/Debian-based)

1.  **Open Terminal**: Press `Ctrl + Alt + T`.

2.  **Install Git**: Run the following command:
    ```bash
    sudo apt install git -y
    ```
    The `-y` flag will automatically confirm the installation.

### 1.3. Installing PostgreSQL

PostgreSQL is a powerful, open-source relational database system that the Football App uses to store its data. You will need to install PostgreSQL and create a specific database for the application to function correctly.

#### 1.3.1. For Windows Users

1.  **Download PostgreSQL Installer**: Go to the official PostgreSQL download page for Windows: [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/) [4]. Download the latest stable version of the graphical installer by EDB.

2.  **Run the Installer**: Locate the downloaded `.exe` file and double-click it to start the installation wizard.

3.  **Follow Installation Prompts**: 
    *   **Installation Directory**: You can usually accept the default installation directory (e.g., `C:\Program Files\PostgreSQL\X.X`, where X.X is the version number).
    *   **Select Components**: Ensure that "PostgreSQL Server" and "pgAdmin 4" (a graphical administration tool) are selected. You can optionally deselect "Stack Builder" and "Command Line Tools" if you prefer to manage the database via pgAdmin or the command line later.
    *   **Data Directory**: Accept the default data directory.
    *   **Password**: Set a strong password for the PostgreSQL superuser (`postgres`). **Remember this password**, as you will need it to connect to your database.
    *   **Port**: The default port is `5432`. You can usually leave this as is.
    *   **Pre-installation Summary**: Review the settings and click "Next" to begin the installation.

4.  **Complete Installation**: Once the installation is complete, uncheck the option to launch Stack Builder (unless you need it for other purposes) and click "Finish".

#### 1.3.2. For macOS Users

There are a few ways to install PostgreSQL on macOS. Using Homebrew is generally recommended for its simplicity and ease of management.

**Option 1: Install via Homebrew (Recommended)**

1.  **Install Homebrew (if you don't have it)**: If you haven't already, install Homebrew by opening your Terminal and running:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    Follow the on-screen instructions.

2.  **Install PostgreSQL**: Once Homebrew is installed, run the following command in your Terminal:
    ```bash
    brew install postgresql
    ```
    This will install the latest stable version of PostgreSQL.

3.  **Start PostgreSQL Service**: After installation, you need to start the PostgreSQL service. You can do this by running:
    ```bash
    brew services start postgresql
    ```
    To check if it's running, you can use `brew services list`.

**Option 2: Install via Postgres.app**

1.  **Download Postgres.app**: Go to [https://postgresapp.com/](https://postgresapp.com/) [5] and download the latest version of Postgres.app.

2.  **Install**: Drag the downloaded `Postgres.app` to your Applications folder.

3.  **Launch and Initialize**: Open Postgres.app. It will automatically start a PostgreSQL server and prompt you to initialize a new server. Click "Initialize" and then "Start". You can also configure it to start automatically when you log in.

#### 1.3.3. For Linux Users (Ubuntu/Debian-based)

PostgreSQL is available in the default repositories for Ubuntu/Debian, making installation straightforward.

1.  **Open Terminal**: Press `Ctrl + Alt + T`.

2.  **Update Package List**: Ensure your package list is up-to-date:
    ```bash
    sudo apt update
    ```

3.  **Install PostgreSQL**: Install the PostgreSQL server and client packages:
    ```bash
    sudo apt install postgresql postgresql-contrib -y
    ```
    The `postgresql-contrib` package provides additional utilities and functionalities.

4.  **Verify Installation**: The PostgreSQL service should start automatically after installation. You can check its status with:
    ```bash
    sudo systemctl status postgresql
    ```
    It should show `active (exited)` or `active (running)`. If not, you can start it with `sudo systemctl start postgresql`.

5.  **Switch to PostgreSQL User**: During installation, a default PostgreSQL superuser named `postgres` is created. To interact with PostgreSQL from the command line, you'll often need to switch to this user:
    ```bash
    sudo -i -u postgres
    ```
    You will now be in the `postgres` user's shell. To exit this shell and return to your regular user, type `exit`.

### 1.4. Verifying Installations

After installing Python, Git, and PostgreSQL, it's crucial to verify that they are correctly installed and accessible from your command line or terminal. This step ensures that the rest of the setup process will go smoothly.

#### 1.4.1. Verifying Python

1.  **Open Command Prompt/Terminal**: 
    *   **Windows**: Search for "cmd" or "Command Prompt" in the Start menu and open it.
    *   **macOS/Linux**: Open your Terminal application.

2.  **Check Python Version**: Type the following command and press Enter:
    ```bash
    python3 --version
    ```
    You should see an output similar to `Python 3.11.x` (the exact version number might vary). If you see an error or `Python 2.x`, double-check your installation steps, especially the "Add Python to PATH" step for Windows.

3.  **Check pip Version**: Type the following command and press Enter:
    ```bash
    pip3 --version
    ```
    You should see an output indicating the `pip` version and its location. `pip` is Python's package installer, which we'll use to install other necessary components for the app.

#### 1.4.2. Verifying Git

1.  **Open Command Prompt/Terminal**: Use the same command prompt or terminal window you used for Python.

2.  **Check Git Version**: Type the following command and press Enter:
    ```bash
    git --version
    ```
    You should see an output similar to `git version 2.x.x` (the exact version number might vary). If you see an error, revisit the Git installation steps for your operating system.

#### 1.4.3. Verifying PostgreSQL

1.  **Open Command Prompt/Terminal**: Open a new Command Prompt (Windows) or Terminal (macOS/Linux) window.

2.  **Access PostgreSQL Command Line (psql)**:
    *   **Windows**: Open the `SQL Shell (psql)` application from your Start Menu (it's usually installed with PostgreSQL). You will be prompted for Server, Database, Port, Username, and Password. For default installation, you can press Enter for Server (`localhost`), Database (`postgres`), Port (`5432`), and Username (`postgres`). Enter the password you set during installation.
    *   **macOS/Linux**: If you installed via Homebrew or apt, you can directly use the `psql` command. First, ensure you are the `postgres` user (for Linux) or your regular user (for macOS, if Homebrew installed it to your PATH).
        ```bash
        psql -U postgres
        ```
        You will be prompted for the password for user `postgres` (the one you set during installation).

3.  **Check PostgreSQL Version**: Once connected to the `psql` prompt (you'll see `postgres=#`), type:
    ```sql
    SELECT version();
    ```
    And press Enter. You should see output showing the PostgreSQL version. To exit `psql`, type `\q` and press Enter.

Once you have successfully verified Python, Git, and PostgreSQL installations, you are ready to move on to setting up the Football App!


## 2. Setting Up the Application

Now that your computer is ready with Python, Git, and PostgreSQL, it's time to get the Football App's code onto your system and prepare its environment. This section will guide you through downloading the project, creating a dedicated space for it, and installing all the necessary components.

### 2.1. Downloading the Code from GitHub

The Football App's code is hosted on GitHub, a platform for collaborative software development. We will use Git (which you just installed!) to download a copy of the project to your computer.

1.  **Open Command Prompt/Terminal**: If you closed it, open a new Command Prompt (Windows) or Terminal (macOS/Linux) window.

2.  **Navigate to a suitable location**: You need to decide where you want to save the project on your computer. It's a good practice to create a dedicated folder for your projects. For example, you might want to create a folder called `my_projects` in your `Documents` folder.

    To navigate to a folder, you use the `cd` (change directory) command. Here are some examples:

    *   **Windows**: To go to your Documents folder:
        ```bash
        cd C:\Users\YourUsername\Documents
        ```
        (Replace `YourUsername` with your actual Windows username)

    *   **macOS/Linux**: To go to your Documents folder:
        ```bash
        cd ~/Documents
        ```
    If you want to create a new folder and then go into it, you can use `mkdir` (make directory) and `cd`:
    ```bash
    mkdir my_projects
    cd my_projects
    ```
    Once you are in the desired location, proceed to the next step.

3.  **Download the Project**: Now, we will use the `git clone` command to download the Football App's code. This command will create a new folder named `football_app` in your current location and copy all the project files into it.

    ```bash
    git clone https://github.com/Shashwat-Ghimire/Football-Statistics.git
    ```
    **Note**: You will need to replace `https://github.com/Shashwat-Ghimire/Football-Statistics.git` with the actual GitHub repository URL provided by the developer. If you were provided with a `.zip` file, you would simply extract it to your chosen location instead of using `git clone`.

4.  **Navigate into the Project Folder**: After the download is complete, you will have a new folder named `football_app`. You need to navigate into this folder to work with the project files.

    ```bash
    cd football_app
    ```
    You should now be inside the main project directory.

### 2.2. Setting Up a Virtual Environment

A virtual environment is a self-contained space for your Python projects. It keeps the dependencies (additional software packages) for one project separate from others. This prevents conflicts and ensures that the Football App has exactly what it needs to run without interfering with other Python applications on your system. It's a best practice in Python development.

1.  **Create the Virtual Environment**: While inside the `football_app` directory in your Command Prompt/Terminal, run the following command to create a virtual environment named `venv`:

    ```bash
    python3 -m venv venv
    ```
    This command tells Python to create a new virtual environment in a folder called `venv` within your `football_app` directory. This might take a moment.

2.  **Activate the Virtual Environment**: After creating the virtual environment, you need to activate it. Activating it means that any Python commands you run in that Command Prompt/Terminal window will use the Python and packages from this specific environment, not your system's global Python installation. Windows Powershell is more reliable to use.

    *   **Windows**:
        ```bash
        \venv\Scripts\activate
        ```

    *   **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
    You will know the virtual environment is active because your command prompt or terminal line will change to include `(venv)` at the beginning, like this:

    ```
    (venv) C:\Users\YourUsername\Documents\my_projects\football_app>
    ```
    or
    ```
    (venv) user@computer:~/my_projects/football_app$
    ```

### 2.3. Installing Required Packages

The Football App relies on several external Python packages to perform tasks like web scraping, database management, and web serving. These packages are listed in a file called `requirements.txt` within the project. We will use `pip` (Python's package installer) to install them into your activated virtual environment.

1.  **Install Packages**: With your virtual environment activated (you should see `(venv)` at the start of your prompt), run the following command:

    ```bash
    pip install -r requirements.txt
    ```
    This command tells `pip` to read the `requirements.txt` file and install all the listed packages. `pip install -r requirements.txt`
    This process might take a few minutes, and you will see a lot of text scrolling by as packages are downloaded and installed. Once it's done, you should see a message indicating successful installation.
    If an error occures you can manually install these packages via `pip install *package_name*`

Congratulations! You have successfully set up the Football App's code and its environment. The next step is to run the application and see it in action.

## 3. Running the Application

With all the prerequisites installed and the application code set up in its virtual environment, you are now ready to bring the Football App to life! This section will guide you through initializing the database, scraping the latest Premier League data, and finally, starting the web server to view the dashboard in your browser.

**Important**: Ensure your virtual environment is still activated. You should see `(venv)` at the beginning of your command prompt or terminal line. If not, navigate to your `football_app` directory and activate it using the commands from Section 2.2.

### 3.1. Initializing the Database

The Football App uses a database to store all the player statistics, hat-tricks, and clean sheets data. Before we can add any data, we need to prepare this database. This process is called "making migrations" and "migrating", which essentially sets up the necessary tables in your database.

**Note**: You need to have PostgreSQL downloaded and running in your system along with a database named `'football_app'`.

#### 3.1.1. Creating the `football_app` Database

Before proceeding with database initialization, you need to create a PostgreSQL database named `football_app`. This database will be used by the application to store its data. You can create this database using the `createdb` command-line utility or directly within the `psql` interactive terminal.

**Option 1: Using `createdb` (Recommended for simplicity)**

1.  **Open Command Prompt/Terminal**: Open a new Command Prompt (Windows) or Terminal (macOS/Linux) window.

2.  **Create the Database**: Run the following command. You might be prompted for the `postgres` user's password (the one you set during PostgreSQL installation).
    ```bash
    createdb -U postgres football_app
    ```
    *   `-U postgres`: Specifies that you are connecting as the `postgres` superuser.
    *   `football_app`: This is the name of the database you are creating.

    If the command executes without any output, it means the database was created successfully.

**Option 2: Using `psql` (More control)**

1.  **Access `psql`**: Connect to the PostgreSQL interactive terminal as the `postgres` superuser. You will be prompted for the password.
    *   **Windows**: Open `SQL Shell (psql)` from your Start Menu and enter the connection details (Database: `postgres`, User: `postgres`, Password: your password).
    *   **macOS/Linux**: In your Terminal, run:
        ```bash
        psql -U postgres
        ```

2.  **Create the Database**: Once you are at the `postgres=#` prompt, type the following SQL command and press Enter:
    ```sql
    CREATE DATABASE football_app;
    ```
    You should see `CREATE DATABASE` as output if successful.

3.  **Exit `psql`**: Type `\q` and press Enter to exit the `psql` terminal.

After successfully creating the `football_app` database, you can proceed with the application's database initialization.

1.  **Make Migrations**: 
    ```bash
    python manage.py makemigrations
    ```
    This command inspects your application's models and creates migration files that describe the changes needed for your database schema.

2.  **Apply Migrations**: 
    ```bash
    python manage.py migrate
    ```
    This command applies the changes described in the migration files to your `football_app` database, creating the necessary tables and columns.

If both commands run successfully, your database is now initialized and ready to store data.

### 3.2. Scraping the Data

Now that your database is set up, you can populate it with the latest Premier League statistics. The Football App includes a script to scrape data from a reliable online source.

1.  **Run the Scraper**: With your virtual environment activated, execute the following command:
    ```bash
    python manage.py scrape_data
    ```
    This process might take some time as it fetches data from the internet. You will see progress updates in your terminal. Once completed, the latest Premier League data will be stored in your `football_app` database.

### 3.3. Starting the Web Server

Finally, it's time to start the web server that hosts the Football App. This will make the application accessible through your web browser.

1.  **Run the Server**: In your terminal (with the virtual environment still activated), run:
    ```bash
    python manage.py runserver
    ```
    You will see output indicating that the development server is starting, usually on `http://127.0.0.1:8000/` or `http://localhost:8000/`.

### 3.4. Accessing the Application in Your Browser

1.  **Open Your Web Browser**: Open your preferred web browser (Chrome, Firefox, Edge, Safari, etc.).

2.  **Enter the Address**: In the address bar, type the address provided by the `runserver` command (e.g., `http://127.0.0.1:8000/`) and press Enter.

    You should now see the Football App dashboard, displaying the Premier League statistics!


## 4. Troubleshooting & FAQs

### 4.1. Common Errors and How to Fix Them

*   **"'python' is not recognized as an internal or external command" (Windows)**: This usually means Python was not added to your system's PATH during installation. Re-run the Python installer and ensure the "Add Python to PATH" option is checked. Alternatively, you might need to use `py` instead of `python` in your commands (e.g., `py -m venv venv`).

*   **Virtual Environment Not Activating**: Double-check the activation command for your operating system. Ensure you are in the correct directory (the `football_app` directory) when trying to activate it.

*   **`pip install -r requirements.txt` errors**: If you encounter errors during package installation, it might be due to missing build tools or specific package dependencies. Try installing packages one by one (e.g., `pip install Django`) to pinpoint the problematic one. Ensure your internet connection is stable.

*   **PostgreSQL Connection Errors**: 
    *   **Incorrect Password**: Ensure you are using the correct password for the `postgres` user. If you forgot it, you might need to reset it (this is an advanced topic and usually involves editing PostgreSQL configuration files).
    *   **PostgreSQL Service Not Running**: Verify that the PostgreSQL service is running on your system (see Section 1.3.3 for Linux, or check your Services application on Windows).
    *   **Port Conflict**: If another application is using port `5432`, you might need to configure PostgreSQL to use a different port during installation or in its configuration files.

*   **"Database does not exist"**: This means you haven't created the `football_app` database in PostgreSQL. Go back to Section 3.1.1 and follow the instructions to create it.

*   **"Table '...' does not exist"**: This indicates that the database migrations haven't been applied. Ensure you have run `python manage.py makemigrations` and `python manage.py migrate` successfully (Section 3.1).

*   **Scraping Errors**: If the `scrape_data` command fails, it could be due to changes in the website's structure from which data is being scraped, or an unstable internet connection. Check the application's logs for more specific error messages.

*   **Web Server Not Starting**: Ensure no other application is using port `8000`. You can try running the server on a different port (e.g., `python manage.py runserver 8001`).

### 4.2. Frequently Asked Questions

*   **Q: Can I use a different database system instead of PostgreSQL?**
    A: The application is configured to use PostgreSQL. While it's technically possible to switch to other database systems (like SQLite or MySQL), it would require significant changes to the application's code and is beyond the scope of this manual.

*   **Q: How often should I scrape new data?**
    A: You can scrape new data whenever you want updated statistics. For Premier League data, scraping after each match week would provide the most up-to-date information.

*   **Q: How do I stop the web server?**
    A: In the terminal where the `python manage.py runserver` command is running, press `Ctrl + C` (Command + C on macOS).

*   **Q: The application looks different from the screenshots I saw. Why?**
    A: The appearance might vary slightly depending on your web browser and operating system. Ensure all required packages are installed, as some might be responsible for styling.

## 5. Conclusion

Congratulations! You have successfully navigated through the process of setting up and running the Football App on your local computer. You now have a powerful and visually appealing dashboard that provides up-to-date Premier League statistics, including top scorers, clean sheets leaders, and hat-tricks.

We hope this manual has been clear, comprehensive, and easy to follow. Our aim was to empower you, the non-technical user, to take control of this application and enjoy its features without needing to delve into complex programming concepts.

This application demonstrates how data can be transformed into insightful and engaging visualizations, bringing the excitement of the Premier League directly to your desktop. Feel free to explore the dashboard, re-scrape data for updates, and share your insights with fellow football enthusiasts.

Thank you for using the Football App, and enjoy your Premier League statistics!

## References
1. Python for Windows: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Python for macOS: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
3. Git for Windows: [https://git-scm.com/download/win](https://git-scm.com/download/win)
4. PostgreSQL for Windows: [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)
5. Postgres.app: [https://postgresapp.com/](https://postgresapp.com/)


