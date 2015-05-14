# Unofficial API for Postimees.ee
Article scraper for the Estonian news site Postimees.

### How it works
On wap.postimees.ee, articles are exposed in a very easily parseable format, and can be queried by changing article ID in the URL. Example: [wap.postimees.ee/?wid=3190591](http://wap.postimees.ee/index.php?wid=3190591).

### Usage
See example in `scrape_articles_csv.py`.

### Dependencies
* lxml
* requests
