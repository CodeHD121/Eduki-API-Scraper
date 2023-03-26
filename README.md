# Eduki-API-Scraper

This scraper is for the website https://eduki.com/de, more specifically its API.
Eduki is a platform where teachers can sell and buy custom material for students of different age and topics.
The scraper has two files - one will download data via the eduki API and save it as a JSON-file, while the other file will extract data and save it as a XLSX-file.

The first one, eduki_API.py, manipulates the API to change parameters like the amount of data or the subject:
![2023-03-26 14_44_09-AmazonScraper py – eduki_API py](https://user-images.githubusercontent.com/91540358/227776847-b5043373-81f1-4eac-849a-358795a6d2be.png)

It will save the custom data as a JSON file which then will be loaded with the second file, eduki_load.py.
This one will create a dictionary for each entry and convert it into an XLSX-file with Python Pandas.
![2023-03-26 14_45_41-AmazonScraper py – eduki_load py](https://user-images.githubusercontent.com/91540358/227777088-62ac4225-905e-4adc-a410-5636c53bc797.png)

The XLSX will look like this:
![2023-03-26 14_47_48-Eduki-Mathe-36 xlsx - Excel](https://user-images.githubusercontent.com/91540358/227777117-53526468-7874-4c55-b225-f734ed9fe5f5.png)

