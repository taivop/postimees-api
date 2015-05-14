from article import Article
import time, codecs

range_min = 10001
range_max = 100000
num_saved = 0

# Open file
f = codecs.open('../data/out_{}_{}.csv'.format(range_min, range_max), 'w', "utf-8")

# Start timing
start_time = time.time()

# Pull and save articles
for article_id in range(range_min, range_max+1):
    a = Article.get_article(article_id)
    print("{:0}: ".format(article_id), end="")
    print(a.title if a else "---")

    # Save only if page actually contained an article
    if a:
        s = a.to_csv() + '\n'
        f.writelines(s)
        num_saved += 1

    sleep_ms = 0
    time.sleep(sleep_ms/1000)


# Print summary
num_scraped = range_max+1-range_min
duration = time.time() - start_time

print("\n --<< SUMMARY >>--")
print("Scraped {} pages in {:.1f} seconds.".format(num_scraped, duration))
print("Retrieved {} articles ({:.0%}).".format(num_saved, num_saved/num_scraped))