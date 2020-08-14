# Auto-opens the flask application

from selenium import webdriver
import os

def flaskopen() :
	path = os.popen("readlink -f geckodriver").read()[:-1]
	driver = webdriver.Firefox(executable_path = path)
	driver.get("http://127.0.0.1:5000/")
