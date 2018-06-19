import scrapy

class IkmanIk(scrapy.Spider):
    name = "vehicles"

    def start_requests(self):
        yield scrapy.Request('https://ikman.lk/en/ads/%s/%s?sort=%s&by_paying_member=%s' % (self.location, self.category
                                                                        , self.sort, self.by_paying_member), self.parse)

    def parse(self, response):
        for item in response.css('div.serp-items div.ui-item div.item-content'):
            next_page = item.css('a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse_individual)

        page = response.css('div.serp-pagination a.pag-next::attr(href)').extract_first()
        if page is not None:
            yield response.follow(page, callback=self.parse)


    def parse_individual(self, response):

        def extract_with_css(item, query):
            elem = item.css(query).extract_first()

            if elem is not None:
                return elem.strip()
            else:
                return elem

        def parse_item_properties(item):
            keys = item.css('div.item-properties dl dt::text').extract()
            values = item.css('div.item-properties dl dd::text').extract()
            item_properties = {}

            for index in range(len(keys)):
                item_properties[keys[index]] = values[index]

            return item_properties


        def get_value(key, dict):
            return dict.get(key, "NULL")


        for item in response.css('div.item-detail div.ui-panel-content'):
            item_properties = parse_item_properties(item)

            yield {
                'Name': extract_with_css(item, 'div.item-top h1::text'),
                'For sale by': extract_with_css(item, 'div.item-top p.item-intro span.poster a::text'),
                'Price': 'Rs ' + extract_with_css(item, 'div.ui-price-tag span.amount::text'),
                'Brand': get_value("Brand:", item_properties),
                'Model year': get_value("Model year:", item_properties),
                'Condition': get_value("Condition:", item_properties),
                'Transmission': get_value("Transmission:", item_properties),
                'Model': get_value("Model:", item_properties),
                'Body type': get_value("Body type:", item_properties),
                'Fuel type': get_value("Fuel type:", item_properties),
                'Engine capacity': get_value("Engine capacity:", item_properties),
                'Mileage': get_value("Mileage:", item_properties),
                'Item Description': item.css('div.item-description p::text').extract(),
                'Date': extract_with_css(item, 'div.item-top p.item-intro span.date::text'),
                'Location': extract_with_css(item, 'div.item-top p.item-intro span.location::text')
            }


