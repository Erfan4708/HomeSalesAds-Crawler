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

By running the code
```
scrapy crawl home_spider -O home_data.json
```
Or

```
scrapy crawl home_spider -O home_data.csv
```
At
cmd
that in the folder **home_data**
It is opened, you can do the scrap and the netich in the file
`home_data.json`
Or
`home_data.csv`

As you can see, the data in the output files are not clean and are not suitable for use in data analysis, so by running the file
`clean_data.py`

You can save the cleaned data in the file
`home_data_clean.json`
Or
`home_data_clean.csv`
