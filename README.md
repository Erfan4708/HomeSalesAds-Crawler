# HomeSalesAds-Crawler

This web crawler, which is written with Scrapy, refers to the wall site (Mashhad apartments) and the features of each ad such as
+ **name**
+ **Meterage**
+ **Year of construction**
+ **Number of rooms**
+ **Price**
+ **Price per meter**
+ **Floor**
+ **Does it have an elevator?**
+ **Does it have a warehouse?**
+ **Does it have parking?**

and saves it in a file in **Json** and **Csv** formats.

By opening the code
```
scrapy crawl home_spider -O home_data.json
```
Or

```
scrapy crawl home_spider -O home_data.csv
```
At
terminal,
that is in the folder **home_data**

you can observe the scraped data in below files:
`home_data.json`
Or
`home_data.csv`

As you will notice, the data in the output files are not clean and thus are not suitable to use in data analysis; therefore by running the file
`clean_data.py`

You can save the cleaned data in the file
`home_data_clean.json`
Or
`home_data_clean.csv`
