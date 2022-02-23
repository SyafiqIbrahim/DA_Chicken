############################
#Import scrapy library
############################
import scrapy

############################
#Class Extract
############################
class Extract(scrapy.Spider):
    #Name for scrapy
    name = 'Spider'

    #Website input
    start_urls = ['http://192.168.182.143/spicyx']

    def parse(self, response):
        #Extract image with 'img' tag
        Image_Selector = 'img'

        for x in response.css(Image_Selector):
            #Image stored in src attribute
            newsel = '@src'

            #Display image url
            yield {
                'Image Link:': x.xpath(newsel).extract_first(),
            }

        # To recurse next page
        Page_Selector = '.next a ::attr(href)'
        next_page = response.css(Page_Selector).extract_first()
        if next_page:
            yield scrapy.Request (
                response.urljoin(next_page),
                callback=self.parse
            )