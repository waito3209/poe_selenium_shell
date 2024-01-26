# poe_selenium_shell
A simple poe selenium version shell , use selenium headless
## Installation

### Step 1: Install Python


### Step 2: Set Up a Virtual Environment (Optional)

It's recommended to set up a virtual environment to isolate the project dependencies. To create a virtual environment, open a terminal or command prompt and navigate to the project directory.

```bash
cd poe_selenium_shell

```

Then, run the following command to create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.


### Step 3: Install Required Packages

To install the project dependencies, run the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

This command will install all the necessary packages specified in the `requirements.txt` file.

### Step 4: Install Firefox

If Firefox is not already installed on your system, also login in to poe (gmail or other methord in Firefox

### Step 5: Install Firefox Driver
Download the appropriate driver version for your operating system and place it in a directory of your choice.

### Step 6: Modify Path in `main.py`

Open the `main.py` file in a text editor of your choice. modify the var 
```
cache_dr = "path/to/cache"
profile = webdriver.FirefoxProfile("/home/USERNAME/snap/firefox/common/.mozilla/firefox/8snfq1yq.default")

```


## Running the Project


In your terminal or command prompt, navigate to the project directory and execute the following command:

```bash
python main.py
```

The project will now run, and you should see the output in the terminal or command prompt.

