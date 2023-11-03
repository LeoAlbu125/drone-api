
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import random
from droneapi import create_app
from database.models import setup_db, Drone, Photo
import dotenv



dotenv.load_dotenv(dotenv.find_dotenv())
#database_path = os.getenv("DB_NAME")
#database_filename = "database.db"
#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))



class DroneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        
        self.app = create_app()
        self.client = self.app.test_client
        self.app.config['TESTING'] = True
        #self.database_name = "Test"
        self.database_path = "postgresql://{}".format(os.getenv("DB_NAME"))
        #self.database_path = "postgres://{}/{}".format(
        #    'localhost:5432', self.database_name)
        setup_db(self.app)
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            #self.db.create_all()

        
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    
    def drone_role_patch_drone_error(self):
        drone_patch = {
            "drone_name":"test",
            "drone_model":"t_e_s_t"
            }
    
        res = self.client().patch("/drones/1", json=drone_patch, headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODk4MTAwNSwiZXhwIjoxNjk5MDY3NDA1LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyJdfQ.UpPEZNnGgCKECwv2OAD60ATNnlsdkbV3T2zhI9LT_Kz7AHiQ79jSufEdjMroboW4irZ-xkK4tkJX5lwc9aUIxwOQgW39mIRXHjFyjADxW_x8mkByMg4Ue9n02EtPnguzAJh6JiVqzguj6pD-sSOmJ29PwJlOwBIyf2a17XbipnOB3wgo-41zwJXfCMc1u_JAUUjBzKf0SC0AebHc_991yJtPeC0_GmcE5HWwlr60ubUohJx3dQtSSCuADxwGQsZkciY6T1g2JW9GQmymJKzu7Q6uj2BTcVcGPJdNBl8UkJxlYSSrDWK0JB9GymdbBzsfuhX7hflwZBa6KK3eZl5HZg"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"],False)
     
     
     
     
    def test_drones(self):
        res = self.client().get("/drones")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["drones"])
        
    def test_drones_photos(self):
        res = self.client().get("/1/photos", headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["photos"])
        
    def test_drones_photos_404_error(self):
        res = self.client().get("/31321/photos", headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        
    def test_drones_photos_access_error(self):
        res = self.client().get("/1/photos")
        self.assertEqual(res.status_code, 401)
        
    """ 
    def test_post_photo(self):
        nody= {"tag":"foto minha",
               "content":"adsaskdjalsdjlkadjla2kj32j23287u39auh",
               "drone_id":1

            }

        res = self.client().post("/photos", json=nody, headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA",
            "Accept": "application/json"
        })
        
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["photo"])
       
    def test_post_photo_error_no_drone(self):
        new_photo_2 = {
            "tag":"test12345678",
            "content":"dasdadad2131312da21dqa",
            "drone_id":12312312312
        }
    
        res = self.client().post("/photos", json=new_photo_2, headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        
    def test_post_photo_error_no_token(self):
        new_photo = {
            "tag":"dasdsda",
            "content":"asdasdas",
            "drone_id":1
        }
    
        res = self.client().post("/photos", json=new_photo)
        
        
        self.assertEqual(res.status_code, 401)
    
    def test_patch_drone(self):
        drone_patch = {
            "drone_name":"test",
            "drone_model":"t_e_s_t"
        }
    
        res = self.client().patch("/drones/1", json=drone_patch, headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"],True)
        self.assertIsNotNone(data["drone"])
        
    def test_patch_drone_error(self):
        drone_patch = {
            "drone_name":312312312312,
            "drone_model":3123123123123
        }
    
        res = self.client().patch("/drones/1", json=drone_patch, headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"],False)
    
    def test_delete_photo(self):
        
      
        photo = Photo(id=999,tag="testatest",content="dsadasdads",drone_id=1)
        photo.insert()
        
        res = self.client().delete("/photos/999", headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"],True)
    
    def test_delete_photo_error(self):
        
      
        res = self.client().delete("/photos/99999", headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA"
        })
        data = json.loads(res.data)
        
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"],False)
    
    def drone_role_get_photo(self):
        res = self.client().get("/1/photos", headers={
            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODk4MTAwNSwiZXhwIjoxNjk5MDY3NDA1LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyJdfQ.UpPEZNnGgCKECwv2OAD60ATNnlsdkbV3T2zhI9LT_Kz7AHiQ79jSufEdjMroboW4irZ-xkK4tkJX5lwc9aUIxwOQgW39mIRXHjFyjADxW_x8mkByMg4Ue9n02EtPnguzAJh6JiVqzguj6pD-sSOmJ29PwJlOwBIyf2a17XbipnOB3wgo-41zwJXfCMc1u_JAUUjBzKf0SC0AebHc_991yJtPeC0_GmcE5HWwlr60ubUohJx3dQtSSCuADxwGQsZkciY6T1g2JW9GQmymJKzu7Q6uj2BTcVcGPJdNBl8UkJxlYSSrDWK0JB9GymdbBzsfuhX7hflwZBa6KK3eZl5HZg"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["photos"])
    """

    
    
    
if __name__ == '__main__':
    unittest.main()