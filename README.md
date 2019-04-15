# Flask News Application

![Komo News Highlights](https://bobcat.grahamdigital.com/image/upload/view?width=1280&height=720&method=crop&url=https://media.wsls.com/photo/2017/04/24/Whats%20News%20Today_1493062809311_9576980_ver1.0.png)

This App consumes [News API](https://newsapi.org/) and fetches data from different news sources and collates them by category and source.

You can see the live Application here [Komo News](https://komo-news-highlight.herokuapp.com/).

Author Information
========
James Komo 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to:

-   Have python installed
-   Have a terminal to interact with the app.
-   Any text editor


Installation
========

    $ git clone https://github.com/jameskomo/news-highlight.git


Build & Deployment
========

**NOTE:** You need to have fully cloned it to run it locally.


    $ ./start.sh 

    # it will launch the web page from local server and fetch 
    news using api provided

##Built With

- Built with Python 3.6
- Flask
- Styled using Bootstrap

Behavior Driven Development (BDD)
==================================

| Input                                                            | Output                                                                         |
|------------------------------------------------------------------|--------------------------------------------------------------------------------|
| User Visits Home Page https://komo-news-highlight.herokuapp.com/ | User sees various news sources on the homepage of the application.             |
| User selects news source                                         | User views all news articles from the selected news source in the application. |
| User opens news source and clicks on article                     | User sees image, description and the time a news article was created.          |
| User clicks on an article based on news source                   | User reads the full article on the source website.                             |


Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!

## License

MIT License

Copyright (c) 2019 James Komo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

