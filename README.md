# Overview

RPG Clicker is a Django web app incremental game, or "clicker" game. To run it, you will need to have both [Django](https://www.djangoproject.com/) and [Python](https://www.python.org/) installed.

To run RPG Clicker after downloading, open your computer's terminal and ensure you are in the directory containing the "RPG_Clicker" folder. Then, run the following command:

```
python manage.py runserver
```

This will start a test server on your device. In a browser, enter one of the following url's into your navigation bar:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

or

[http://localhost:8000/](http://localhost:8000/)

Once here, you will see the home page for RPG Clicker. On this page, you can play the game! To play, begin by clicking the button labelled "Grind XP." You will see your XP go up by 1 each time. Once you have 100 XP, you can buy your first auto XP farm, an "Overworld." Navigate down to the "Store" section and click the button labelled "Purchase an Overworld." You will notice that the purchase cost 100 XP, you now own one overworld, and your XP now goes up by 1 every second with no input from you. Auto XP farms continually generate a certain amount of XP each second, as indicated next to their name. You are now ready to continue playing by clicking, purchasing more auto XP farms, and generating more and more XP!

> ***WARNING:*** If you navigate away from the home page, your progress will be lost. This will be changed in a future update.

On the navigation bar at the top of the screen, clicking "Achievements" will navigate you to the achievements page. On this page, you will see many achievements you can earn by gaining higher and higher XP. In a future update, this will change to only displaying achievements you have already earned.

I made RPG Clicker to learn how to use the Django framework. I hope you enjoy it as much as I enjoyed making it!

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

The first web page you will see is the home page. Navigate between the home page and the achievements page using the navigation bar at the top of each page.

The home page is where RPG Clicker is played (instructions for playing the game can be found above, in "Overview"). On this page, you will find three main sections: The navigation bar, the XP area, and the store. In the XP area, you can see how much XP you currently have and generate XP by clicking the "Grind XP" button. In the store section, you can purchase auto XP Farmers. Your XP and the number of auto XP farmers you own are all dynamically displayed based on user input.

On the achievements page, you will find many achievements listed. These achievements are displayed by looping through a list located in the file "views.py." In the future, the achievements page will be changed to only show achievements you have earned while playing.

# Development Environment

* Python 3.10.7
* Django 4.1.1
* Visual Studio Code 1.71.2

# Useful Websites

* [Official Django Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
* [Django Tutorial by Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

# Future Work

* Improve web page appearances.
* Implement Django database to allow for saved games.
* Implement dynamic achievements page.