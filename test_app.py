import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import db, Movie, Actor


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.executive_producer_token ='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rTkVNa0l4T1VNMU5UVkRSRE13UXpoRE4wVTJNMEZHUWpVM1FrVkZPRUpDTVRoR05qUTBPUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob29wLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMjEyNTM1Mjc0NzUyMTY4Mjg3MyIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9vcC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc5NjIxODk1LCJleHAiOjE1Nzk2MjkwOTUsImF6cCI6IjJQNGFzRlREWEsyc0liRm9xZWhabXZqS0ZkckFqZ0JjIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.w0UGK97NGEYOFAP86-aD7-9X3uAAVhRL7LmqxhVL-kLtNIynoYlHi_iiVnDjOgMRkwOZY-aE-apKJyTHgUleFi41GxsmeyoL3k55iWaRfVQf2mGIg6VlP8yuxqhjbcmmGY0VJ-S3NHNtoW6igf5t7yIIXoT9mRsUTQxDcDxjUMFKWr3etrElgVz2IwaJ8ELQLFrozM9KGcOsGspuEugOaDmJK3YyVuw8xHGOu6N5HS0F9PkDsIlgwFPUI1U13ZNLIVeAD-b3zZZQCxvdEmu_8f_VJHOUopxKr1mL5DPm54_JRbe3n8_ypoouYElQTT8dJMsaL06SzpO60HEoIpGKhA'
        self.casting_director_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rTkVNa0l4T1VNMU5UVkRSRE13UXpoRE4wVTJNMEZHUWpVM1FrVkZPRUpDTVRoR05qUTBPUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob29wLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTA3MDY4MTYyOTQ2Mzg3NzY4NSIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9vcC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc5NjIyMzIyLCJleHAiOjE1Nzk2Mjk1MjIsImF6cCI6IjJQNGFzRlREWEsyc0liRm9xZWhabXZqS0ZkckFqZ0JjIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6bW92aWVzIl19.3N9i5kG0qHeh8VrRM0SOUNg1o5Idz3MtttD6xhXpGj00lGJCkpv648DqPSKp4CbW5aFISOrMJpMz_DadGuBdNA2Mfg68roBUvZqDCAkcFbhc4YOCgvQ8R1kadsswyhFfhAcmWvbFBBEmSKvLIIxTcrqoFVx6LUnjrb0pmhexxoOzEn8-0g_99pY1CuPumY64BeO44h7GLaynTn9ZijpHok3xkt5Skn_I2LEGhyK62zF1iZM-UUDfKAP7Han1438z8pANPuk9fqHaKMT0dRIqZDwwFTj31bCuv1Gd34d9Wl2QW2bDh9z_WJYJGiitfurwfD7xtCq5BTc8YH_Z36VKnw'

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        
        response = self.client().get(
            '/actors',
            headers={
                "Authorization": "Bearer {}".format(self.casting_director_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()