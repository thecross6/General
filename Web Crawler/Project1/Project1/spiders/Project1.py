import scrapy
import re
from collections import deque
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# Allowed_domains stops the crawler from exiting, lyle.smu.edu
class QuotesSpider(scrapy.Spider):
    name = "Project1"
    start_urls = ['http://lyle.smu.edu/~fmoore/']
    handle_httpstatus_list = [404]
    allowed_domains = ["lyle.smu.edu"]
    f = open('Output.txt', 'w')
    o = open('Words.txt', 'w')
    # Pages that need crawling
    URL = deque()
    # Page with the words found within and their frequency. Page is the unique document ID
    all_words = {}

    def parse(self, response):
        if response.status == 404:
            self.close(QuotesSpider, "\n\nDun Goofed\n\n")
        temp_URL = []
        # Word and Frequency storage (ONLY htm and html)
        Words = {}
        # Unique Document Id
        QuotesSpider.f.write("Current page:\t" + response.request.url + "\tStatus Code:\t" + str(response.status) + "\n\n")
        QuotesSpider.f.write("Links: \n")
        for a in response.css('a::attr(href)'):
            link = a.extract()
            temp_URL.append(link)
            QuotesSpider.f.write(link + "\n")

        QuotesSpider.f.write("\nIMG's: \n")
        # img = "graphic files", as found on the .docx file
        for img in response.css('img::attr(src)'):
            QuotesSpider.f.write(img.extract() + "\n")
        QuotesSpider.f.write("\n\n")

        #QuotesSpider.o.write(response.request.url + "\n")
        for word in response.css('*::text'):
            # Take out start/end space
            instance = word.extract().strip()
            # Remove special characters
            instance = re.sub(r'[^a-zA-Z0-9]',' ', instance)
            # Split a string into individual words
            instance = instance.split()
            for temp in instance:
                if temp in Words:
                    Words[temp] += 1
                else:
                    Words[temp] = 1
                #QuotesSpider.o.write(temp + "\n")
        #QuotesSpider.o.write("\n")
        QuotesSpider.all_words[response.request.url] = Words
        # print(QuotesSpider.all_words)
        #raise scrapy.exceptions.CloseSpider('done goofed')

        #print("\n\nTemp URL's: \n", temp_URL, "\n\n")
        for next_page in temp_URL:
            if re.search("htm|html$", next_page):
                # Pages not granted access to the crawler
                if not re.search("dontgohere", next_page):
                    next_page = next_page.replace("'", "")
                    next_page = next_page.replace('"', "")
                    #print("\nText Check:", next_page, "\n")
                    # Do not go into hidden links
                    if response.css('a[href="'+next_page+'"]::text'):
                        # Stay within the domain
                        next_page = response.urljoin(next_page)
                        if re.search("lyle.smu.edu/~fmoore", next_page):
                            #print("\nAdded", next_page, "\n")
                            QuotesSpider.URL.append(next_page)

        #print("\n\nBefore: ", QuotesSpider.URL, "\n\n")
        next_page = QuotesSpider.URL.popleft()
        #print("\n\nAfter: ", QuotesSpider.URL, "\n\n")
        if next_page is not None:
            return scrapy.Request(next_page, callback=self.parse)
        else:
            print("Top 20 stop words")

# Run the Crawler
settings = Settings()
spider = QuotesSpider()
process = CrawlerProcess(settings)
process.crawl(spider)
process.start()

# Get Term Frequency for all words and remove stopwords
TF = {}
for document in QuotesSpider.all_words.keys():
    total_number_words = len(QuotesSpider.all_words[document].keys())
    Word_Freq = {}
    for word in QuotesSpider.all_words[document].keys():
        # Remove stopwords
        if not re.match("all|may|must|here|with|many|are|at|this|to|if|why|where|who|was|do|no|in|the|not|or|but|is|and|of|for|else|be|^\w$|^\w\w$", word.lower()):
            # Words and Frequency (NO page/id)
            freq = QuotesSpider.all_words[document][word] / total_number_words
            freq = round(freq, 3)
            Word_Freq[word] = freq
    TF[document] = Word_Freq

# Number of documents with a word
instances = {}
for documentSearch in QuotesSpider.all_words.keys():
    for word in QuotesSpider.all_words[documentSearch].keys():
        instances[word] = 1
        for document in QuotesSpider.all_words.keys():
            if word in QuotesSpider.all_words[document]:
                instances[word] += 1
print(instances)