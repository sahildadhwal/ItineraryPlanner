import unittest
from app import app, itineraries



#itineraries = []

class BasicTests(unittest.TestCase):    
    def setUp(self):
        # Executed before each test
        # Initializes a test client for Flask app and sets it to testing mode
        
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test case for home endpoint ('/')
        # Checks if the endpoint returns a status code 200 and contains the welcome message.
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b"Welcome to Sahil\'s Itinerary Planner!", response.data)

    def test_create_itinerary(self):
        # Test case for create itinerary endpoint ('/create_itinerary/<user>')  
        # Checks if endpoint successfully creates itinerary for a user
        
        
        response = self.app.post('/create_itinerary/San Diego')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Itinerary for San Diego created successfully!", response.data )
        self.assertIn("San Diego", itineraries)

    def test_add_event(self):
        # Test case fofr add event endpount ('/add_event/<user>')
        # Checks if endpoint adds an event to a user's itinerary
        
        # create itinerary for Seattle)
        self.app.post('/create_itinerary/Seattle')
        # add event: Space Needle
        response = self.app.post('/add_event/Seattle', json={'event' : 'Visit Space Needle'} )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Event added to Seattle\'s itinerary!" , response.data)
        self.assertIn('Visit Space Needle' , itineraries['Seattle'])

    def test_view_itinerary(self):
        # Test case for the view itinerary endpoint ('/view_itinerary/<user>')
        # Verifies if endpoint gets user's itinerary correctly

        # create itnerary for Seattle
        self.app.post('/create_itinerary/Seattle')
        self.app.post('add_event/Seattle', json={'event' : 'Visit Space Needle'} )
        response = self.app.get('/view_itinerary/Seattle')

        self.assertEqual(response.status_code , 200)
        self.assertIn(b"Visit Space Needle", response.data)

if __name__== "__main__":
    unittest.main()
