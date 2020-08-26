# Middle-Earth Name Generator
Neural network to generate new character names from Middle-earth. 




## Data

Data obtained from [Tolkien's Characters](https://www.behindthename.com/namesakes/list/tolkien/alpha), which contains character names from _The Hobbit_, _The Lord of the Rings_ and _The Silmarillion_.

The list was extended with alternative names given to some characters – `Other Name` column in the original table. Data was preprocessed by removing duplicates and regnal numbers. The final number of names ascends to 880. The file can be found in `data/`.




## Installation
The code was tested using Python 3.6.10. To install the necessary packages run:
```bash
pip install -r requirements.txt
```



## Usage

Run the program file from command line as:
```bash
python tolkien_name_generator.py
````
For more information about the model, check `notebooks/`.
