# Stock Market Analysis

## Join the Gitter Discussion

[![Join the chat at https://gitter.im/techmeetscraper/Lobby](https://badges.gitter.im/techmeetscraper/Lobby.svg)](https://gitter.im/techmeetscraper/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Dependencies

   - scipy
   - numpy 
   - scikit learn
   - goose 
   - beautifulsoup
   - pysentiment
   - pandas
   - unidecode 
   - nltk 
   - flask
Note that Python 2.7 needs to be present on the machine.

To install the dependencies, run the following commands.You may need root permissions for your machine.

```sh
pip install -U scipy numpy scikit-learn
pip install -U pysentiment
pip install -U pandas
pip instll -U unidecode
pip install -U nltk
pip install flask
pip install -U bs4
python -m pip install -U pip setuptools
python -m pip install matplotlib
apt-get install python-feedparser
python -m nltk.downloader all
```
To install goose dependency
```sh
git clone https://www.github.com/grangier/python-goose.git
cd python-goose
pip install -r requirements.txt
python setup.py install
```

## Running the app
Clone the git repository into a suitable folder:
```sh
git clone https://github.com/priyanshsaxena/techmeet.git/
cd techmeet
python app.py
```
Once the project is up and running, you can open the output.txt file to get the links of relevant rarticles about the top gainers and losers. You can visualize the results of the stocks by opening the Web UI at http://localhost:5000 in your browser.