
# GitHub README

To create README create a file called `README.md` in the root directory. 

`.md` stands for markdown file type which is a commonly used programming file format to write documents in.

To lean more about markdown, [click here](https://www.markdownguide.org/basic-syntax/).

Generally you want to include following:
* small section about what the program does
* how to install the program (locally and on the cloud using docker for example)
* how to use different important features of the program (how to train the model/how to evaluate the model)
* how to run the main program itself (for example if it is a dashboard, to run it run `py run.py`.
* how to use important API calls (if your program for example creates prediction - how to make a call to that predictive class so it returns the prediction results)
* how to set-up any necessary credentials/keys

[Here](https://github.com/plotly/plotly.py/blob/master/README.md) is an example of a professional README file. 

[Here](https://github.com/tensorflow/tensorflow) is what TensorFlow's README looks like.


# How to install virtual environment

To create a virtual environment you have  to options:
* make a fresh environment where nothing is installed (when you are starting your own project)
* install all necessary packages using requirements.txt (when you are using someone elese's project)

To do this, type the following commands into the terminal console. `Shell` console or if that does not work switch to `cmd` or `Python` consoles.


## Fresh environment set-up

### 1.  Create enviroment
First we want to establish environment using `py -PYTHON_VERSION -m venv ENVIRONMENT_NAME` where `PYTHON_VERSION` stands for the Python interpreter version you want your project to use, and `ENVIRONMENT_NAME` is the name of the new environment.

Example of how it would look like when the `PYTHON_VERSION` is 3.8 and `PYTHON_VERSION` is .env .

```
py -3.8 -m venv .env
```
### 2.  Activate enviroment

Next you want to activate your enviroment so that VS Code knows that it needs to run the code using it. Once activated this means all the new packages you will install will be installed into activated environment. `ENVIRONMENT_NAME\Scripts\activate` where `ENVIRONMENT_NAME` is the name of the new environment you created earlier. This assumes enviroment is in the root directory, if it is not, you need to adjust the relative path!

Example using the name of the enviroment you create earlier `.env`:

```
.env\Scripts\activate
```
---
When you close VS Code and start next time, make sure the enviroment is activated and you are not using the global one!

---


### 3. Update pip
Next important step is to upgrade `pip` to the latest version because most newest package versions will not be able to be installed with older pip version. 99.9% of the time newest version of `pip` will be able to install any of the old package versions (when it fails, google is your friend).

```
py -m pip install --upgrade pip
```
---
### 4. Install anything you need

Now you can normally install any packages you want and they will be installed into your virtual enviroment.

Example next: `pip install pandas`.

---

#### Recap 

```
py -3.8 -m venv .env
.env\Scripts\activate
py -m pip install --upgrade pip
```

Example next: `pip install pandas`.

## requirements.txt set-up

If you have an existing projet that you setting-up the enviroment for, you want to install all necessary packages with `requirements.txt`.

### 1. Create a new environment
First you set-up your enviroment similarly to a fresh set-up:

```
py -3.8 -m venv .env
.env\Scripts\activate
py -m pip install --upgrade pip
```

### 2. Install packages in requirements.txt
And now use the following command to install all the dependancies: 
```
py -m pip install -r requirements.txt
```

---

#### Recap

```
py -3.8 -m venv .env
.env\Scripts\activate
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```


# How to create requirements.txt

When you push your code to GitHub, you want anyone to be able to download, run it and continue working on it. This means they will have to be able to successfully install all dependancies for your code using `requirements.txt`.

To create the file make sure the correct enviroment is active and use the following command:

```
pip freeze > requirements.txt
```
This will create `requirements.txt` in the root directory with all packages and their dependancies used in your project.

# .gitignore

Before pushing your code to GitHub, sometimes there are files/folders you do not want/need to update.

This includes things like:
* the enviroment itslef - because it's very large and GitHub doesn't allow updating anything more than 100mb
* `__pycache__` - cache generated by Pyhon
* any sensitive files containing credentials/passwords
* trained weights of models - especially deep learning because those can be in GB sizes

To exclude these from being pushed to GitHub, in the root directory create `.gitignore` file.

Inside create a new line withe whatever you want to exclude from being pushed to GitHub.

Example:

```
.env/
__pycache__/
credentials1.py
models/credentials2.py
```
This will remove all folders and their content with names `.env` and `__pycache__`. 

It will remove `credentials1.py` file in the root directory and `credentials2` in the `models` directory - but will keep everything else in there.




