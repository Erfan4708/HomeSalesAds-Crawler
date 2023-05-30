import scrapy


class HomeSpider(scrapy.Spider):
    name = "home_spider"
    start_urls = ["https://divar.ir/s/mashhad/buy-apartment"]

    def parse(self, response):
        for href in response.css("div.post-card-item-af972 a::attr(href)").getall():
            href = "https://divar.ir" + href
            yield response.follow(href, callback=post_detail)


def post_detail(response):
    title = response.css(".kt-page-title__title::text").get()
    meterage = response.css("div.kt-group-row-item--info-row:nth-child(1) > span:nth-child(2)::text").get()
    year_of_construction = response.css("div.kt-group-row-item--info-row:nth-child(2) > span:nth-child(2)::text").get()
    number_of_rooms = response.css("div.kt-group-row-item--info-row:nth-child(3) > span:nth-child(2)::text").get()
    price = response.css("div.kt-base-row:nth-child(3) > div:nth-child(2) > p:nth-child(1)::text").get()
    price_per_meter = response.css("div.kt-base-row:nth-child(5) > div:nth-child(2) > p:nth-child(1)::text").get()
    floor = response.css("div.kt-base-row:nth-child(9) > div:nth-child(2) > p:nth-child(1)::text").get()
    elevator = response.css("div.kt-group-row:nth-child(12) > div:nth-child(1) > span:nth-child(2)::text").get()
    if elevator == "آسانسور ندارد":
        elevator = response.css("div.kt-group-row-item--disabled:nth-child(1) > span:nth-child(2)::text").get()
    parking = response.css("div.kt-group-row:nth-child(12) > div:nth-child(2) > span:nth-child(2)::text").get()
    if parking == "پارکینگ ندارد":
        parking = response.css("div.kt-group-row-item--disabled:nth-child(2) > span:nth-child(2)::text").get()
    warehouse = response.css("div.kt-group-row:nth-child(12) > div:nth-child(3) > span:nth-child(2)::text").get()
    if warehouse == "انباری ندارد":
        warehouse = response.css("div.kt-group-row-item--disabled:nth-child(3) > span:nth-child(2)::text").get()
    data = {
        "title": title,
        "meterage": meterage,
        "Year of construction": year_of_construction,
        "number of rooms": number_of_rooms,
        "price": price,
        "price per meter": price_per_meter,
        "Floor": floor,
        "Elevator": elevator,
        "Parking": parking,
        "Warehouse": warehouse,
    }
    return data
