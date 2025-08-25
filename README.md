# Football App User Manual

## Introduction

- What the application does (displays Premier League stats)
- Who this manual is for (non-technical users)

## 1. Getting Started: Prerequisites

- What you need before you begin
- Installing Python (with step-by-step instructions for Windows, macOS, and Linux)
- Installing Git (with step-by-step instructions for Windows, macOS, and Linux)
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

### 1.3. Verifying Installations

After installing Python and Git, it's crucial to verify that they are correctly installed and accessible from your command line or terminal. This step ensures that the rest of the setup process will go smoothly.

#### 1.3.1. Verifying Python

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

#### 1.3.2. Verifying Git

1.  **Open Command Prompt/Terminal**: Use the same command prompt or terminal window you used for Python.

2.  **Check Git Version**: Type the following command and press Enter:
    ```bash
    git --version
    ```
    You should see an output similar to `git version 2.x.x` (the exact version number might vary). If you see an error, revisit the Git installation steps for your operating system.

Once you have successfully verified both Python and Git installations, you are ready to move on to setting up the Football App!


## 2. Setting Up the Application

Now that your computer is ready with Python and Git, it's time to get the Football App's code onto your system and prepare its environment. This section will guide you through downloading the project, creating a dedicated space for it, and installing all the necessary components.

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

**Note**: You need to have postgresql downloaded and running in your system along with a database named `'football_app'`.

1.  **Make Migrations**: This command tells Django (the web framework the app is built on) to look at the app's models (which define the structure of our data) and create instructions for how to set up the database tables.

    ```bash
    python3 manage.py makemigrations stats
    ```
    You should see output indicating that new migrations have been created. For example:
    ```
    Migrations for 'stats':
      stats/migrations/0001_initial.py
        - Create model Team
        - Create model Player
        - Create model PlayerSeasonStats
        - Create model HatTrick
      stats/migrations/0002_cleansheet.py
        - Create model CleanSheet
    ```
    (The exact migration files might vary slightly, but you should see `CleanSheet` if you're using the latest version of the app.)

2.  **Apply Migrations**: Now, we apply these instructions to your database. This command actually creates the tables in your `db.sqlite3` file (which will be created automatically in your `football_app` directory if it doesn't exist).

    ```bash
    python3 manage.py migrate
    ```
    You will see a series of messages indicating that various migrations are being applied. This might take a moment. Once it's complete, your database is ready to receive data.

### 3.2. Scraping the Data

Now that the database is set up, we can populate it with the latest Premier League statistics. The Football App includes a built-in tool (a "management command") that scrapes data directly from Wikipedia.

1.  **Run the Scraper**: Execute the following command to start the data scraping process:

    ```bash
    python3 manage.py scrape_football --url "https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League#Season_statistics" --league "Premier League" --season "2023-24"
    ```
    Let's break down this command:
    *   `python3 manage.py scrape_football`: This is the command to run our custom data scraping tool.
    *   `--url "https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League#Season_statistics"`: This specifies the Wikipedia page from which the data will be scraped. This URL points to the 2023-24 Premier League season statistics page.
    *   `--league "Premier League"`: This tells the scraper which league to associate the data with.
    *   `--season "2023-24"`: This specifies the season for the scraped data.

    The scraping process might take a few minutes, as it connects to the internet, downloads the web page, extracts the tables, and saves the data into your database. You will see messages in your terminal indicating the progress, such as "Scraping complete ✅ for 2023-24" and details about the tables found and data extracted.

    **Note**: You can run this command again in the future to update the data. The application is designed to handle new data without creating duplicates, ensuring your statistics are always accurate and up-to-date.

### 3.3. Starting the Web Server

Now that your database is populated with the latest Premier League data, it's time to start the web application. This will launch a local web server on your computer, making the Football App accessible through your web browser.

**Note** : Check or restart your postgresql to ensure that the process is actually running. You need to run the windows powershell as administrator and run `net start postgresql-x64-17`. Please note that -17 is the postgres version installed in your system.

1.  **Start the Server**: In your Command Prompt/Terminal (with the virtual environment still activated), run the following command:

    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```
    Let's break down this command:
    *   `python3 manage.py runserver`: This is the Django command to start a development web server.
    *   `0.0.0.0:8000`: This tells the server to listen on all available network interfaces (`0.0.0.0`) and use port `8000`. This means the application will be accessible from your web browser at a specific address.

    You will see output similar to this:
    ```
    Watching for file changes with StatReloader
    Performing system checks...
    System check identified no issues (0 silenced).
    August 19, 2025 - 09:14:10
    Django version 5.2.5, using settings 'football_stats.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
    WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
    For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
    ```
    **Important**: Do not close this Command Prompt/Terminal window. The server needs to keep running for the application to be accessible. If you close it, the application will stop.

### 3.4. Accessing the Application in Your Browser

Finally, with the web server running, you can now open your web browser and view the Football App dashboard!

1.  **Open Your Web Browser**: Launch your preferred web browser (e.g., Chrome, Firefox, Edge, Safari).

2.  **Enter the Address**: In the address bar of your browser, type the following address and press Enter:

    ```
    http://127.0.0.1:8000/
    ```
    This address (`127.0.0.1`) refers to your own computer (also known as `localhost`), and `:8000` is the port number we specified when starting the server. You should now see the Football App dashboard, displaying the Premier League statistics!

    Congratulations! You have successfully set up and run the Football App on your local machine. You can now explore the top scorers, clean sheets leaders, and hat-tricks for the 2023-24 Premier League season.

## 4. Troubleshooting & FAQs

Even with clear instructions, sometimes things don't go exactly as planned. This section aims to address common issues you might encounter while setting up or running the Football App, along with frequently asked questions. If you run into a problem, please refer to this section first.

### 4.1. Common Errors and How to Fix Them

Here are some common error messages you might see and what they mean, along with steps to resolve them.

#### Error 1: `python3: command not found` or `python: command not found`

*   **Meaning**: Your system cannot find the Python interpreter. This usually means Python was not installed correctly or was not added to your system's PATH (for Windows users).
*   **Solution**:
    1.  **Revisit Python Installation**: Go back to Section 1.1. "Installing Python" and carefully follow the steps for your operating system. For Windows, ensure the "Add Python X.X to PATH" checkbox was selected during installation.
    2.  **Restart Terminal/Command Prompt**: After reinstalling or modifying PATH, close your current Command Prompt/Terminal window and open a new one. Sometimes, changes to system variables only take effect in new sessions.
    3.  **Verify Installation**: Use `python3 --version` to confirm Python is now recognized.

#### Error 2: `pip is not recognized as an internal or external command` or `pip3: command not found`

*   **Meaning**: Similar to the Python error, your system cannot find the `pip` (Python package installer) command.
*   **Solution**:
    1.  **Revisit Python Installation**: `pip` is usually installed alongside Python. Ensure Python was installed correctly as per Section 1.1.
    2.  **For Linux**: Ensure you ran `sudo apt install python3-pip`.
    3.  **Restart Terminal/Command Prompt**: Close and reopen your terminal.
    4.  **Verify Installation**: Use `pip3 --version` to confirm `pip` is recognized.

#### Error 3: `git: command not found`

*   **Meaning**: Your system cannot find the Git command.
*   **Solution**:
    1.  **Revisit Git Installation**: Go back to Section 1.2. "Installing Git" and follow the steps for your operating system carefully.
    2.  **Restart Terminal/Command Prompt**: Close and reopen your terminal.
    3.  **Verify Installation**: Use `git --version` to confirm Git is recognized.

#### Error 4: `ModuleNotFoundError: No module named 'django'` or similar `ModuleNotFoundError`

*   **Meaning**: The Python packages required by the Football App are not installed in your active Python environment.
*   **Solution**:
    1.  **Activate Virtual Environment**: Ensure your virtual environment is activated. You should see `(venv)` at the beginning of your command prompt/terminal line. If not, activate it using the commands from Section 2.2.
    2.  **Install Requirements**: Run `pip install -r requirements.txt` again while your virtual environment is active (Section 2.3).

#### Error 5: `Address already in use` when starting the web server

*   **Meaning**: Another program on your computer is already using port `8000`, which the Football App tries to use.
*   **Solution**:
    1.  **Wait and Retry**: Sometimes, a previous instance of the server might not have shut down completely. Wait a minute or two and try running `python3 manage.py runserver 0.0.0.0:8000` again.
    2.  **Use a Different Port**: If the issue persists, you can try running the server on a different port, for example, port `8001`:
        ```bash
        python3 manage.py runserver 0.0.0.0:8001
        ```
        If you do this, remember to access the application in your browser at `http://127.0.0.1:8001/` instead of `http://127.0.0.1:8000/`.
    3.  **Identify and Kill Process (Advanced)**: For advanced users, you can find which process is using the port and terminate it. This varies by operating system:
        *   **Windows (Command Prompt)**:
            ```bash
            netstat -ano | findstr :8000
            ```
            Look for the `PID` (Process ID) in the last column. Then, use `taskkill /PID <PID> /F` (replace `<PID>` with the actual number).
        *   **macOS/Linux (Terminal)**:
            ```bash
            sudo lsof -i :8000
            ```
            Look for the `PID` in the output. Then, use `kill -9 <PID>` (replace `<PID>` with the actual number).

#### Error 6: `django.db.utils.OperationalError: no such table: stats_players` or similar database errors

*   **Meaning**: The database tables have not been created or are corrupted.
*   **Solution**:
    1.  **Run Migrations**: Ensure you have successfully run the database migration commands as described in Section 3.1:
        ```bash
        python3 manage.py makemigrations stats
        python3 manage.py migrate
        ```
    2.  **Delete `db.sqlite3` (Last Resort)**: If migrations don't fix it, you can delete the `db.sqlite3` file (located in your `football_app/football_app` directory) and then re-run the `makemigrations` and `migrate` commands. **Warning**: This will delete all existing data, so you will need to re-scrape the data afterwards.

### 4.2. Frequently Asked Questions (FAQs)

#### Q1: How often can I update the data?

A1: You can update the data as often as you like by re-running the scraping command:

```bash
python3 manage.py scrape_football --url "https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League#Season_statistics" --league "Premier League" --season "2023-24"
```
The application is designed to handle updates without creating duplicate entries.

#### Q2: Can I scrape data for a different season or league?

A2: The current scraper is specifically configured for the 2023-24 Premier League season from the provided Wikipedia URL. Modifying it for other seasons or leagues would require changes to the `scraper.py` file and potentially the database models, which is beyond the scope of this manual for non-technical users. It would involve understanding web scraping techniques and Django development.

#### Q3: The charts are not showing data or look empty.

A3: This usually means there was an issue during the data scraping process, or the database is empty. 

*   **Check Scraper Output**: Look at the output in your terminal when you ran the `scrape_football` command. Did it report successful scraping? Were there any errors?
*   **Verify Database Content**: You can quickly check if data exists by trying to re-run the scraper. If it says "Extracted X unique clean sheets" and "Extracted Y unique player stats", then data is present.
*   **Restart Server**: Sometimes, simply restarting the web server (`Ctrl+C` to stop, then `python3 manage.py runserver 0.0.0.0:8000` to restart) can resolve display issues.

#### Q4: How do I stop the application?

A4: To stop the web server, go to the Command Prompt/Terminal window where the server is running and press `Ctrl + C` (hold down the `Ctrl` key and press `C`). You will see messages indicating the server is shutting down.

#### Q5: How do I close the virtual environment?

A5: To deactivate the virtual environment, simply type `deactivate` in your Command Prompt/Terminal and press Enter. Your prompt will return to its normal state (without `(venv)`).

```bash
deactivate
```

#### Q6: Can I access the app from another device on my network?

A6: Yes, if your computer and the other device are on the same local network. Instead of `http://127.0.0.1:8000/`, you would use your computer's local IP address. To find your computer's IP address:

*   **Windows**: Open Command Prompt and type `ipconfig`. Look for "IPv4 Address".
*   **macOS/Linux**: Open Terminal and type `ifconfig` or `ip a`. Look for an IP address starting with `192.168.` or `10.`.

Then, on the other device, enter `http://your_computer_ip_address:8000/` in the browser.

Remember, this is for local network access only. For public access, you would need to deploy the application to a web hosting service, which is a more advanced topic.

## 5. Conclusion

Congratulations! You have successfully navigated through the process of setting up and running the Football App on your local computer. You now have a powerful and visually appealing dashboard that provides up-to-date Premier League statistics, including top scorers, clean sheets leaders, and hat-tricks.

We hope this manual has been clear, comprehensive, and easy to follow. Our aim was to empower you, the non-technical user, to take control of this application and enjoy its features without needing to delve into complex programming concepts.

This application demonstrates how data can be transformed into insightful and engaging visualizations, bringing the excitement of the Premier League directly to your desktop. Feel free to explore the dashboard, re-scrape data for updates, and share your insights with fellow football enthusiasts.

Thank you for using the Football App, and enjoy your Premier League statistics!

## References
1. Python for Windows: https://www.python.org/downloads/windows/
2. Python for macOS: https://www.python.org/downloads/macos/
3. Git for Windows: https://git-scm.com/download/win
