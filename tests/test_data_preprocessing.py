import unittest
from unittest.mock import *

from src.enrichment_api import data_preprocessing

class DataPreprocessingTests(unittest.TestCase):
    def test_data_preprocessing(self):
        article_content = """ 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TEST</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
            </style>
        </head>
        <body>
            <h1>I want this content</h1>
            <p>Important Information</p> 
            <script>
                Should not include this
            </script>
        </body>
        </html>
        """ 
        article_title = "TEST"     
        result = data_preprocessing (article_content, article_title)
        self.assertNotIn("Should not include this", result)
        self.assertNotIn("font-family: Arial, sans-serif;", result)
        self.assertNotIn("<meta charset=", result)
        self.assertIn("I want this content", result)
        self.assertIn("Important Information", result)
    
    def test_data_preprocessing_title(self):
        article_content = """ 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>TEST</title>
        </head>
        <body>
            <script>
                The script get the article content dynamically 
            </script>
        </body>
        </html>
        """ 
        article_title = "TEST"     
        result = data_preprocessing (article_content, article_title)
        self.assertNotIn("The script get the article content dynamically", result)
        self.assertIn("TEST", result)
        

if __name__ == '__main__':
    unittest.main()
