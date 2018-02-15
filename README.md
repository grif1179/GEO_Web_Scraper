# GEO_Web_Scraper
Web scraper used to get the download links from databases with publicly available genomics data.

# Environment Setup
1. Download python 3.6.4

2. Install pip

3. Install virtualenv
```
pip install --upgrade virtualenv
```
4. Go to where you have this project cloned and in the terminal type:
```
virtualenv --python python3 env
```
If you are on windows you might have to run:
```
virtualenv --python "c:\python36\python.exe" env
```
5. Activate environment
For Mac/Linux:
```
source env/bin/activate
```
For Windows:
```
.\env\Scripts\activate
```
6. Install packages needed to run project
```
pip install requests
pip install beautifulsoup4
```
