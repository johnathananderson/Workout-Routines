from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup 
import time 
import re 
import datetime 
import pprint
import json

class Br(): 
    def __init__(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "https://www.jefit.com/exercises/bodypart.php?id=11&exercises=All"
        self.page = 1 
    def start(self): 
        self.browser.get(self.url) 
        time.sleep(1) 
    def next_page(self): 
        self.url = "https://www.jefit.com/exercises/bodypart.php?id=11&exercises=All&All=0&Bands=0&Bench=0&Dumbbell=0&EZBar=0&Kettlebell=0&MachineStrength=0&MachineCardio=0&Barbell=0&BodyOnly=0&ExerciseBall=0&FoamRoll=0&PullBar=0&WeightPlate=0&Other=0&Strength=0&Stretching=0&Powerlifting=0&OlympicWeightLifting=0&Beginner=0&Intermediate=0&Expert=0&page=" + str(self.page + 1)
        self.browser.get(self.url)
        self.page+=1 
        time.sleep(1) 
    def close_out(self): 
        self.browser.close()
    def process_page(self, last):
        result = []
        if last == False:
            for x in range(1,11):
                element = self.browser.find_elements_by_xpath("//*[@id='hor-minimalist_3']/tbody/tr/td/table/tbody/tr[" + str(x) + "]/td[3]/h4/a")
                result.append((element[0].text, element[0].get_attribute('href')))
        else:
            for x in range(1,10):
                element = self.browser.find_elements_by_xpath("//*[@id='hor-minimalist_3']/tbody/tr/td/table/tbody/tr[" + str(x) + "]/td[3]/h4/a")
                result.append((element[0].text, element[0].get_attribute('href')))
        return result
    def process_results(self, exercises):
        results = []
        exercise_number = 1
        for exercise in exercises:
            self.url = exercise[1]
            self.browser.get(self.url)
            try:
                name = exercise[0]
                main_muscle = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[2]/p[1]").text[20:]
                other_muscle = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[2]/p[2]").text[24:]
                workout_type = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[2]/p[4]").text[7:]
                mechanics = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[2]/p[5]").text[12:]
                equipment = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[2]/p[6]").text[12:]
                difficulty = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[2]/p[7]").text[13:]
                instructions = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[4]/p").text[8:]
                picture_url = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[1]/div[1]/p[2]/a").get_attribute('href')
                results.append([name, main_muscle, other_muscle, workout_type, mechanics, equipment, difficulty, instructions, picture_url])
            except:
                try:
                    name = exercise[0]
                    main_muscle = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[3]/div[2]/p[1]").text[20:]
                    other_muscle = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[3]/div[2]/p[2]").text[24:]
                    workout_type = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[3]/div[2]/p[4]").text[7:]
                    mechanics = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[3]/div[2]/p[5]").text[12:]
                    equipment = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[3]/div[2]/p[6]").text[12:]
                    difficulty = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[3]/div[2]/p[7]").text[13:]
                    instructions = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[5]/p").text[8:]
                    picture_url = self.browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/div[1]/div[1]/p[2]/a").get_attribute('href')
                    results.append([name, main_muscle, other_muscle, workout_type, mechanics, equipment, difficulty, instructions, picture_url])
                except:
                    print("ERROR")
                    pass
            print("Exercise:" + str(exercise_number))
            exercise_number+=1
        return results


b = Br() 
b.start()
exercises = [] 
for x in range(130):
    print("Page {}".format(b.page))
    if x < 129:
        exercises += b.process_page(False)
        b.next_page()
    else:
        exercises += b.process_page(True)
results = b.process_results(exercises)
b.close_out() 

print("DONE")

with open('output.json', 'w') as outfile:
    json.dump(results, outfile)
