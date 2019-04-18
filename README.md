# Mission to Mars

![mission_to_mars](Images/mission_to_mars.jpg)

A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what it does.

## Step 1 - Scraping

Scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* The Jupyter Notebook file called `mission_to_mars.ipynb` is used to complete all of the scraping and analysis tasks. The following outlines what is scraped.

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

### Mars Weather

* The Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. 

### Mars Facts

* The Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

### Mars Hemispheres

* The USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

- - -

## Step 2 - MongoDB and Flask Application

 MongoDB with Flask templating to create a new HTML page to display all of the information that was scraped from the URLs above.
 
- - -

## Copyright

© 2019 Trilogy Education Services. All Rights Reserved.
