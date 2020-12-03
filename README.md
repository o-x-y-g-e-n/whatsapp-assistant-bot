# whatsapp-assistant-bot
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors) [![GitHub license](https://img.shields.io/github/license/o-x-y-g-e-n/whatsapp-assistant-bot)](https://github.com/o-x-y-g-e-n/whatsapp-assistant-bot/blob/master/LICENSE) [![GitHub contributors](https://img.shields.io/github/contributors/o-x-y-g-e-n/whatsapp-assistant-bot)](https://GitHub.com/o-x-y-g-e-n/whatsapp-assistant-bot/graphs/contributors/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/o-x-y-g-e-n/badges/)

Google Like assistant in whatsapp.
![Image](https://i.ibb.co/mDDKdrT/undraw-chat-bot-kli5.png)

This is an utility to setup and run an Whatsapp Bot across web and mobile Whatsapp application. The bot listens to some predefined commands and responds to them according the query fired.

### Tech

whatsapp-assistant-bot uses a number of open source projects to work properly:

* [Python] - Python is a programming language that lets you work quickly
and integrate systems more effectively.
* [Selenium] - Selenium automates browsers. That's it!


### Installation

whatsapp-assistant-bot requires [Python](https://www.python.org/downloads/release/python-380/) v3+ to run.

Install the dependencies and devDependencies:

```sh
$ cd whatsapp-assistant-bot
$ pip3 install -r requirements.txt 
```

### Execution
1. Create a whatsapp group or member named `BOT` (all caps) ***This is a mandatory requirement***
2. Message `Hi` to the group or member. ***This is a mandatory requirement***
3. Download `chromedriver` from [here](https://chromedriver.chromium.org/downloads) according to your Chrome Version & Operating System.
4. Setup the absolute path of the driver in `config.ini` file using your favourite text editor. Something like this.
    ```
    [selenium]
    chromePath = /home/shivam/Desktop/chromedriver
    ```
5. Fire the below commands from the directory
    ```sh
    $ cd src
    $ python3 main.py
    ```
6. If you don't see any errors, you have successfully ran the script. Go and fire some commands!
 
### Commands Available
| Command  | Description  | Parameters  | Execution Time  | Examples |
|---|---|---|---|---|
| */quote*  | It fetches a random quote from the datasets/quote.xml file  | -  | 1-2sec | ```/quote``` |
| */fact*  | It fetches a random fact from the datasets/fact.xml file.  |  - | 1-2sec  | ```/fact``` |
| */joke*  |  It fetches a random joke from the datasets/joke.xml file.  |  - | 1-2sec  | ```/joke``` |
| */flirt*  | It fetches a random pick-up line from the datasets/flirt.xml file.  | -  |  1-2 sec  | ```/flirt``` |
| */weather*  | It fetches the weather of the specified city,state or country.  | [country, state, city] |  2-5 sec | ``` /weather china, /weather newyork``` |
|  */youtube* | it fetches the youtube url for the specific term  | [search_term]  | 10-15sec  | ```/youtube how to make pasta```|
| */news*  | it grabs news  | [local, technology, world, entertainment, health, sports, business]  |  5-10 sec | ```/news local, /news business``` |
| */calc*  | it performs mathematical functions  | [argument]  | 2-5 sec  | ```/calc 2^5, /calc 2+5``` |
| */lyrics*  | It fetches the lyric of the song  | [name of the song]  | 10-15 sec  |``` /lyrics havana ``` |
|  */define* | it fetches the defination of the term  | [word]  | 2-5 sec  | ```/define amazing``` |
| */time*| it gives you the current date and day| - | 1 sec | ```/time``` |

### Future Improvements
- [ ] Whatsapp Attachments Commands 

### Demo
[![Video](https://img.youtube.com/vi/PsA2EJ45YZc/0.jpg)](https://youtu.be/PsA2EJ45YZc)


### License
MIT


[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/o-x-y-g-e-n/)

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Python]: <https://www.python.org/>
   [Selenium]: <https://www.selenium.dev/>
   [Chrome]: <https://www.google.com/intl/en_in/chrome/>