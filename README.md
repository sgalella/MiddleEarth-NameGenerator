# Middle-Earth Name Generator
Neural network to generate new character names from Middle-earth. 

<p align="center">
    <img width="622" height="438" src="images/name_generator.gif">
</p>



## Data

Data obtained from [Tolkien's Characters](https://www.behindthename.com/namesakes/list/tolkien/alpha), which contains character names from _The Hobbit_, _The Lord of the Rings_ and _The Silmarillion_.

The list was extended with alternative names given to some characters – `Other Name` column in the original table. Data was preprocessed by removing duplicates and regnal numbers. The final number of names ascends to 880. The file can be found in `data/`.




## Installation
The code was tested using Python 3.6.10. To install the necessary packages run:

```bash
pip install -r requirements.txt
```

If using Conda, you can also create an environment with the requirements:

```bash
conda env create -f environment.yml
```

By default the environment name is `middle-earth-name-generator`. To activate it run:

```bash
conda activate middle-earth-name-generator
```




## Usage

Run the program file from command line as:
```bash
python middle_earth_name_generator.py
````
For more information about the model, check `notebooks/`.
