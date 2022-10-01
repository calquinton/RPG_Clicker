from django.shortcuts import render
import time

# list of dictionaries, stores all achievements
all_achievements = [
    {
        'xp_requirement': 200,
        'name': 'Vault Dweller',
        'description': 'You have reached level 2 in Fallout 3.'
    },
    {
        'xp_requirement': 29450,
        'name': 'Paradigm of Humanity',
        'description': 'You have reached max level (20) in Fallout 3.'
    },
    {
        'xp_requirement': 66700,
        'name': 'True Mortal',
        'description': 'You have reached max level (30) in Fallout 3 with the Broken Steel add-on.'
    },
    {
        'xp_requirement': 201,
        'name': 'Sole Survivor',
        'description': 'You have reached level 2 in Fallout 4.'
    },
    {
        'xp_requirement': 1251,
        'name': 'Born Survivor',
        'description': 'You have reached level 5 in Fallout 4.'
    },
    {
        'xp_requirement': 4501,
        'name': 'Commonwealth Citizen',
        'description': 'You have reached level 10 in Fallout 4.'
    },
    {
        'xp_requirement': 25501,
        'name': 'Unstoppable Wanderer',
        'description': 'You have reached level 25 in Fallout 4.'
    },
    {
        'xp_requirement': 98001,
        'name': 'Legend of the Wastes',
        'description': 'You have reached level 50 in Fallout 4.'
    },
    {
        'xp_requirement': 161062092626,
        'name': 'Game Breaker',
        'description': 'You have reached level 65,535 in Fallout 4, causing the game to crash.'
    },
]

# list of dictionaries, stores earned achievements
earned_achievements = [
    {

    },
]

def home(request):
    return render(request, 'game/home.html')

def achievements(request):
    context = {
        'achievements': all_achievements
    }

    return render(request, 'game/achievements.html', context)