# Reddit-Scraper
A program that searches through a user provided subreddit for submissions with titles matching a query then downloads the images contained within the post.

## Dependencies
Praw - The library used for interacting with the Reddit API. It allows the user to easily filter submissions and interact with them. In order to install praw copy and paste the following command into your command line.
```
$ pip install praw
```
## Usage
The program takes two command line arguments. The first argument that is passed to the program is assumed to be the subreddit that the user intends on searching. The second argument is assumed to be the query that the user wants to search for. For example if I wanted to search through /r/fountainpens for any posts on /hot that contain the word resin then I would run the following command in the directory of the program.
```
$ python Scraper.py fountainpens resin
```
## Known Isses
* Albums from Imgur are not currently supported due to Imgur breaking the feature that allowed the zipping of gallery's.
* GIF support is under development and not available at ths time.
* The program struggle to find some of the posts for unknown reasons.
* My API access token may have exceeded the maximum number of requests allocated to it. I need to investigate further on the reason behind the request exceptions.
