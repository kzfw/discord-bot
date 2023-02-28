import json
import requests as req
import discord.utils as du

roles = []
URL = ''

# Get all roles
def getRoles(member):
    # Get and return all server roles
    allRoles = du.get(member.guild.roles)
    return allRoles

def getUserRoles(userId):
    # Send get request to site (TODO: Add functionality on website side)
    requestData = req.get(URL + userId) # Request information from user with id = userId
    jsonData = json.loads(requestData.text) # Interpret JSON data as text

