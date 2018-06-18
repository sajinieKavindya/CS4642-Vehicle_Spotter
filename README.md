# CS4642-Vehicle_Spotter
This Scrapy project scrapes vehicle information from "https://ikman.lk/" web site.

## Running the project
For prerequisites, please refer the official Scrapy documentation at https://doc.scrapy.org/en/latest/intro/install.html

Go to the root directory and start scraping by running,

 `scrapy crawl vehicles -o <output_file_name> -a location=<location> -a category=<vehicle_category> -a sort=<date_desc|date_asc> -a by_paying_member=<0|1>`

eg: `scrapy crawl vehicles -o vehicles.json -a location=gampaha -a category=cars -a sort=date_desc -a by_paying_member=1`

Sample values for above parameter: 

		*location = {colombo, gampaha, negombo, kelaniya, ja-ela, kadawatha, delgoda, divulapitiya, ganemulla, kandana, katunayake}
		*category = {vans-buses-lorries, motorbikes-scooters, three-wheelers, heavy-machinery-tractors}
		*sort = {date_desc, date_asc} only
		*by_paying_member = {0, 1} only
