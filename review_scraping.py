from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os

############################ SCRAPING DUOLINGO REVIEWS ##############################

browser = webdriver.Chrome()

url_duolingo = "https://www.amazon.com/Duolingo-Learn-Languages-Free/dp/B00F8L2VO4"
browser.get(url_duolingo)
time.sleep(3)

all_reviews = browser.find_element(By.XPATH,"//*[@id='reviews-medley-footer']/div[2]/a")
all_reviews.click()
time.sleep(5)

all_reviews_list_duolingo = []



for i in range(5):

    reviews_list = browser.find_elements(By.XPATH,"//*[contains(@id, 'customer_review')]/div[4]")
    
    time.sleep(3)
    for individual_review in reviews_list:
        all_reviews_list_duolingo.append(individual_review.text)



rev_count_duolingo = 1
with open("duolingoreviews.txt","w") as file:
    for individual_duolingo_review in all_reviews_list_duolingo:
        file.write(str(rev_count_duolingo)+")" + " " + individual_duolingo_review + "\n")
        file.write("\n")
        rev_count_duolingo += 1


        

############################ SCRAPING ROSETTA STONE REVIEWS ##############################

url_rosettastone = "https://www.amazon.com/Rosetta-Stone-UNLIMITED-Languages-Activation/dp/B082DZBFP7/ref=sr_1_1?keywords=rosetta%2Bstone&qid=1681909508&sr=8-1&th=1"
browser.get(url_rosettastone)
time.sleep(3)

see_all_reviews = browser.find_element(By.XPATH,"//*[@id='reviews-medley-footer']/div[2]/a")
time.sleep(3)

all_reviews_list_rosetta_stone = []

for i in range(5):

    reviews_rosetta = browser.find_elements(By.XPATH, "//*[contains(@id, 'customer_review')]/div[4]")
    time.sleep(3)
    for individual_review_rosetta_stone in reviews_rosetta:
        all_reviews_list_rosetta_stone.append(individual_review_rosetta_stone.text)



rev_count_rosetta_stone = 1
with open("rosettastonereviews.txt","w") as file:
    for individual_rosetta_stone_review in all_reviews_list_rosetta_stone:
        file.write(str(rev_count_rosetta_stone)+")" + " " + individual_rosetta_stone_review + "\n")
        file.write("\n")
        rev_count_rosetta_stone += 1



############################ SCRAPING BABBEL REVIEWS ##############################


url_babbel = "https://www.amazon.com/Babbel-Language-Languages-including-Subscription/dp/B08C9HH97M/ref=pd_rhf_d_ee_s_pd_sbs_rvi_sccl_1_1/143-7737796-6553642?pd_rd_w=ZJE8H&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=XQ6SM963GKB6PGG39CW6&pd_rd_wg=o7Ow3&pd_rd_r=d554e62a-153b-4b4d-b246-c1610f85765c&pd_rd_i=B08C9HH97M&th=1"
browser.get(url_babbel)
time.sleep(3)

see_all_reviews_babbel = browser.find_element(By.XPATH,"//*[@id='reviews-medley-footer']/div[2]/a")
time.sleep(5)

all_reviews_list_babbel = []

for i in range (5):
    reviews_babbel = browser.find_elements(By.XPATH,"//*[contains(@id, 'customer_review')]/div[4]")
    time.sleep(3)
    for review in reviews_babbel:
        all_reviews_list_babbel.append(review.text)

rev_count_babbel = 1
with open("babbelreviews.txt","w") as file:
    for individual_babbel_review in all_reviews_list_babbel:
        file.write(str(rev_count_babbel)+")" + " " + individual_babbel_review + "\n")
        file.write("\n")
        rev_count_babbel += 1
        










