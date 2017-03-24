# Stock Market Analysis

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
git clone https://github.com/ssh-iitmandi/StockMarketAnalysis5thTechMeet.git/
cd TechMeet
python app.py
```
Once the project is up and running, you can open the output.txt file to get the links of relevant rarticles about the top gainers and losers. You can visualize the results of the stocks by opening the Web UI at http://localhost:5000 in your browser.