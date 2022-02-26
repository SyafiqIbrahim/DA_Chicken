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

    ####################################
    #Parse function
    #Start crawling website
    ####################################
    def parse(self, response):
        #Extract image with 'img' tag
        Image_Selector = 'img'

        #Loop response to extract each image URL
        for x in response.css(Image_Selector):
            #Image URL stored in src attribute
            URL = '@src'

            #Display image URL
            yield {
                'Image Link:': x.xpath(URL).extract_first(),
            }
        ###########################
        #To recurse next page
        ###########################
        #Select '.next a' tag with 'href' attribute
        Page_Selector = '.next a ::attr(href)'

        #Extract URL to next page
        next_page = response.css(Page_Selector).extract_first()

        #If valid URL is available, follow link and call Parse function on the link
        if next_page:
            yield scrapy.Request (
                response.urljoin(next_page),
                callback=self.parse
            )