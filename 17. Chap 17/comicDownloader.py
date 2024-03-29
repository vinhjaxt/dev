
import os
import datetime
import requests
import bs4


def check_xkcd(last_url):
    """Download all XKCD comics released after the given URL."""
    url = 'https://xkcd.com'
    # Get latest comics URL with comic number for comparison/file update
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    prev_link = soup.select('a[rel="prev"]')[0]
    href = prev_link.get('href')
    number = href.strip('/')
    url = 'https://xkcd.com/{}/'.format(str(int(number) + 1))
    latest_url = url

    if url == last_url:
        print('No new XKCD comics have been published since last check')
    else:
        while url != last_url:
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'lxml')

            comic_elem = soup.select('#comic img')
            if comic_elem == []:
                print('could not find comic image.')
            else:
                try:
                    comic_url = 'https:' + comic_elem[0].get('src')
                    # Download the image.
                    print('Downloading image {}'.format(comic_url))
                    res = requests.get(comic_url)
                    res.raise_for_status()
                except requests.exceptions.MissingSchema:
                    # Skip this comic.
                    prev_link = soup.select('a[rel="prev"]')[0]
                    url = 'https://xkcd.com' + prev_link.get('href')
                    continue

                # Save the image to ./xkcd.
                image = open(os.path.join('Web Comics', os.path.basename(comic_url)), 'wb')
                for chunk in res.iter_content(100000):
                    image.write(chunk)
                image.close()

            # Get the Prev button's url.
            prev_link = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prev_link.get('href')

    return latest_url


os.makedirs('Web Comics', exist_ok=True)

# File containing latest comic URL checked
with open('/Web Comics/last_downloaded.txt') as f:
    info = f.read().splitlines()
    date = info[0]
    last_xkcd = info[1]

date = datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%Y')
print('Last comic check = ' + date)

# Run functions and rewrite file with 'new' URLs
xkcd_url = check_xkcd(last_xkcd)

with open('/Web Comics/last_downloaded.txt', 'w') as f:
    f.write(date + '\n')
    f.write(xkcd_url + '\n')

print('Finished.')