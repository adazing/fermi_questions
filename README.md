# ABOUT
Hi! This is a website application that can be ran on your browser. This application is meant to practice [Fermi Questions for Science Olympiad](https://www.soinc.org/fermi-questions-c), and one can customize the questions, either by importing them from files ([Here are good file examples](https://github.com/landy8697/open-scioly-fermi/tree/master/formatted_test_data)) or by adding them individually.

# INSTALLATION
## INSTALL PYTHON + PIP
Install [Python](https://wiki.python.org/moin/BeginnersGuide/Download) on your device.
Install [Pip](https://pip.pypa.io/en/stable/installation/) on your device.

## DOWNLOAD CODE
Click the green "CODE" button on the repository page and download the ZIP file. Extract the ZIP file on your device.

## PYTHON VENV

### Go to your terminal and type:
#### Unix/macOS
```python3 -m venv /absolute_path_to_outer_fermi_questions_folder/env```
#### Windows
```py -m venv \absolute_path_to_outer_fermi_questions_folder\env```

### Activate virtual environment:
#### Unix/macOS
```source /absolute_path_to_outer_fermi_questions_folder/env/bin/activate```
#### Windows
```\absolute_path_to_outer_fermi_questions_folder\env\Scripts\activate```

### Install packages:
#### Unix/macOS
```python3 -m pip install -r /absolute_path_to_outer_fermi_questions_folder/requirements.txt```
#### Windows
```py -m pip install -r \absolute_path_to_outer_fermi_questions_folder\requirements.txt```

Now, you are done installing! Close the terminal.

# OPENING THE APPLICATION
Open a terminal and type:
#### Unix/macOS
```source /absolute_path_to_outer_fermi_questions_folder/env/bin/activate```
#### Windows
```\absolute_path_to_outer_fermi_questions_folder\env\Scripts\activate```

Next, type:
#### Unix/macOS
```python3 /absolute_path_to_outer_fermi_questions_folder/fermiquestions/manage.py runserver```
#### Windows
```py \absolute_path_to_outer_fermi_questions_folder\fermiquestions\manage.py runserver```

Now go onto your web browser and go to the url:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
