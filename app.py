# Activate VM:
# source venv/bin/activate

import logging
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

itineraries = {}

# Configure logging for Grafana
logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    logging.info('Request Headers: %s', request.headers)
    logging.info('Request Body: %s', request.get_data())



# Route: Home Endpoint
@app.route('/')
def home():
    # returns JSON resonse w/ Welcome string
    return jsonify(message  = "Welcome to Sahil\'s Itinerary Planner!")


# # Define a route for the root URL
# @app.route('/')
# def hello_world():
#     return 'Hello World! This is Sahil\'s Travel Itinerary Planner'


# Route: Create itinerary for a user
@app.route('/create_itinerary/<user>', methods = ['POST'])
def create_itinerary(user):
    # Creates new itinerary for specific user if they dont already exisit
    # return JSON with SUCCESS or FAILURE message
    if user in itineraries:
        return jsonify(message = f'Itinerary for {user} already exists!'), 400
    
    itineraries[user] = []
    return jsonify(message = f'Itinerary for {user} created successfully!')


# Route: Add event to user's itinerary
@app.route('/add_event/<user>' , methods = ['POST'])
def add_event(user):
    # Adds new event to itinerary for specific user
    # return JSON with SUCCESS or FAILURE message
    if user not in itineraries:
        return jsonify(message = f'No itinerary found for {user}!'), 400

    # Expects a JSON payload with an 'event' attribute.
    event = request.json.get('event')
    itineraries[user].append(event)
    return jsonify(message = f'Event added to {user}\'s itinerary!')


# Route: View a user's itinerary
@app.route('/view_itinerary/<user>', methods = ['GET'])
def view_itinerary(user):
    # return a user's itinerary as a JSON response or  error message if there are no itinerearies
    if user not in itineraries:
        return jsonify(message = f'No itineries found for {user}!'), 400
    return jsonify(itinerary=itineraries[user])



if __name__ == '__main__':
    app.run(debug = True)

