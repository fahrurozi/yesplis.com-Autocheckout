from audioop import add
from tkinter import *
from tkinter import messagebox as mb
import datetime
import csv
from unicodedata import name
from pydoc import cli
from unicodedata import name
from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

root = Tk()
root.geometry('520x700')
root.title("Yesplis Test")
root.configure(background='grey')

bni = '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div:nth-child(3) > div > div:nth-child(3) > div'
permata = '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div:nth-child(3) > div > div:nth-child(1) > div'
mandiri = '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div:nth-child(3) > div > div:nth-child(2) > div'
other = '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div:nth-child(3) > div > div:nth-child(4) > div'


wd = wd.Chrome()

def initial(wd):
    wd.maximize_window()
    wd.implicitly_wait(5)
    wd.delete_all_cookies()
    wd.get('https://yesplis.com/')

def click(browser, element_css):
    WebDriverWait(browser, 60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    browser.find_element_by_css_selector(element_css).click()

def wait_before_ready(browser, element_css):
    WebDriverWait(browser, 60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(browser, 60).until(
        ec.element_located_to_be_selected((By.CSS_SELECTOR, element_css))
    )
    
def checkout(gender, jumlah_tiket):
    WebDriverWait(wd, 60).until(
        ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight'))
    )
    click(wd, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight')
    input_name_checkout = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input')
    print('++++++++++++++++++++'+input_name_checkout.get_attribute('value'))
    WebDriverWait(wd, 60).until(
        ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input'), nama)
    )

    if(gender == 'male'):
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(1)')
    else:
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(2)')

    for x in range(int(jumlah_tiket)):
        n = x+2
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(2) > div:nth-child('+str(n)+') > div > div:nth-child(2) > div.y-row.y-row-ticketuser > div.y-ticketuser-checkbox.y-checkbox.y-gray-text')
        print('==========='+str(n))
    
    

    #Chose payment
    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div.detailTiket > div > div:nth-child(1) > div > p')
    if(payment_method == 'permata'):
        click(wd, permata)
    elif(payment_method == 'mandiri'):
        click(wd, mandiri)
    elif(payment_method == 'bni'):
        click(wd, bni)
    elif(payment_method == 'other'):
        click(wd, other)

    #submit
    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(6) > div.y-buynow-body.y-black-text > div.y-button.y-blue-button.y-is-fullwidth')

def get_ticket(wd, url_tiket, urutan_tiket, jumlah_tiket):
    wd.get(url_tiket)
    if(urutan_tiket == '0'):
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > a')
        for x in range(jumlah_tiket-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > div > div.incQuantity.itemQuantity > p')
    else:
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > a')
        for x in range(jumlah_tiket-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > div > div.incQuantity.itemQuantity > p')
    click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.checkOutBox > div.checkOutButton > a')

def login(wd, email, password):
    click(wd, '.y-white-button')

def check_value():
    g = var.get()
    if(g==1):
        gender ='male'
    else:
        gender ='female'

    payment_method = cvar.get()
    email = iemail.get()
    password = ipassword.get()
    nama = inama.get()
    url_tiket = iurl_tiket.get()
    urutan_tiket = iurutan_tiket.get()
    jumlah_tiket = ijumlah_tiket.get()
    
    print(email)
    print(password)
    print(nama)
    print(url_tiket)
    print(urutan_tiket)
    print(jumlah_tiket)
    print('-'+gender)
    print('-'+payment_method)

def saveinfo():
    # check_value()
    g = var.get()
    if(g==1):
        gender ='male'
    else:
        gender ='female'

    payment_method = cvar.get()
    email = iemail.get()
    password = ipassword.get()
    nama = inama.get()
    url_tiket = iurl_tiket.get()
    urutan_tiket = iurutan_tiket.get()
    jumlah_tiket = ijumlah_tiket.get()
    add_input_1 = iadd_input_1.get()
    add_input_2 = iadd_input_2.get()
    add_input_3 = iadd_input_3.get()
    print(add_input_1+str(type(add_input_1)))
    print(add_input_1 == '')
    # <class 'str'>
    # True
    initial(wd)

# Login
    click(wd, '.y-white-button')
    email_input = wd.find_element_by_xpath('//*[@id="loginContainer"]/div/div[2]/div[2]/form/div[1]/div/input')
    email_input.send_keys(email)
    password_input = wd.find_element_by_xpath('//*[@id="password"]')
    password_input.send_keys(password)
    click(wd, '#btn-login')
   
    WebDriverWait(wd, 60).until(
            ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '#HomeLayout > div.y-navbar > div > div.y-right-navbar > div:nth-child(1) > img'))
    )

# Get Ticket
    wd.get(url_tiket)
    if(int(urutan_tiket) == '0'):
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > a')
        for x in range(int(jumlah_tiket)-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > div > div.incQuantity.itemQuantity > p')
    else:
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > a')
        for x in range(int(jumlah_tiket)-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > div > div.incQuantity.itemQuantity > p')
    click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.checkOutBox > div.checkOutButton > a')

# Checkout
    WebDriverWait(wd, 60).until(
        ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight'))
    )
    click(wd, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight')
    input_name_checkout = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input')
    print('++++++++++++++++++++'+input_name_checkout.get_attribute('value'))

    # #BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input

    if(add_input_1 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_1 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_1.clear()
        column_input_1.send_keys(add_input_1)
    if(add_input_2 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(6) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_2 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(6) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_2.clear()
        column_input_2.send_keys(add_input_2)
    if(add_input_3 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(7) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_3 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(7) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_3.clear()
        column_input_3.send_keys(add_input_3)

    WebDriverWait(wd, 60).until(
        ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input'), nama)
    )

    if(gender == 'male'):
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(1)')
    else:
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(2)')

    for x in range(int(jumlah_tiket)):
        n = x+2
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(2) > div:nth-child('+str(n)+') > div > div:nth-child(2) > div.y-row.y-row-ticketuser > div.y-ticketuser-checkbox.y-checkbox.y-gray-text')
        print('==========='+str(n))
    
    
    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div.detailTiket > div > div:nth-child(1) > div > p')
    if(payment_method == 'permata'):
        click(wd, permata)
    elif(payment_method == 'mandiri'):
        click(wd, mandiri)
    elif(payment_method == 'bni'):
        click(wd, bni)
    elif(payment_method == 'other'):
        click(wd, other)


    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(6) > div.y-buynow-body.y-black-text > div.y-button.y-blue-button.y-is-fullwidth')

def resubmit():
    # Get Ticket
    g = var.get()
    if(g==1):
        gender ='male'
    else:
        gender ='female'

    payment_method = cvar.get()
    email = iemail.get()
    password = ipassword.get()
    nama = inama.get()
    url_tiket = iurl_tiket.get()
    urutan_tiket = iurutan_tiket.get()
    jumlah_tiket = ijumlah_tiket.get()
    add_input_1 = iadd_input_1.get()
    add_input_2 = iadd_input_2.get()
    add_input_3 = iadd_input_3.get()

    wd.get(url_tiket)
    if(int(urutan_tiket) == '0'):
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > a')
        for x in range(int(jumlah_tiket)-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > div > div.incQuantity.itemQuantity > p')
    else:
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > a')
        for x in range(int(jumlah_tiket)-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > div > div.incQuantity.itemQuantity > p')
    click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.checkOutBox > div.checkOutButton > a')

# Checkout
    WebDriverWait(wd, 60).until(
        ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight'))
    )
    click(wd, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight')
    input_name_checkout = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input')
    print('++++++++++++++++++++'+input_name_checkout.get_attribute('value'))


    if(add_input_1 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_1 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_1.clear()
        column_input_1.send_keys(add_input_1)
    if(add_input_2 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(6) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_2 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(6) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_2.clear()
        column_input_2.send_keys(add_input_2)
    if(add_input_3 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(7) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_3 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(7) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_3.clear()
        column_input_3.send_keys(add_input_3)


    WebDriverWait(wd, 60).until(
        ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input'), nama)
    )

    if(gender == 'male'):
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(1)')
    else:
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(2)')

    for x in range(int(jumlah_tiket)):
        n = x+2
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(2) > div:nth-child('+str(n)+') > div > div:nth-child(2) > div.y-row.y-row-ticketuser > div.y-ticketuser-checkbox.y-checkbox.y-gray-text')
        print('==========='+str(n))
    
    
    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div.detailTiket > div > div:nth-child(1) > div > p')
    if(payment_method == 'permata'):
        click(wd, permata)
    elif(payment_method == 'mandiri'):
        click(wd, mandiri)
    elif(payment_method == 'bni'):
        click(wd, bni)
    elif(payment_method == 'other'):
        click(wd, other)


    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(6) > div.y-buynow-body.y-black-text > div.y-button.y-blue-button.y-is-fullwidth')
    # get_ticket()
    # checkout()
    # save()
    # msg()

def relaunch():
    wd.get('https://yesplis.com/logout')
    wd.get('https://yesplis.com/login')

    g = var.get()
    if(g==1):
        gender ='male'
    else:
        gender ='female'

    payment_method = cvar.get()
    email = iemail.get()
    password = ipassword.get()
    nama = inama.get()
    url_tiket = iurl_tiket.get()
    urutan_tiket = iurutan_tiket.get()
    jumlah_tiket = ijumlah_tiket.get()
    add_input_1 = iadd_input_1.get()
    add_input_2 = iadd_input_2.get()
    add_input_3 = iadd_input_3.get()

    # Login
    email_input = wd.find_element_by_xpath('//*[@id="loginContainer"]/div/div[2]/div[2]/form/div[1]/div/input')
    email_input.send_keys(email)
    password_input = wd.find_element_by_xpath('//*[@id="password"]')
    password_input.send_keys(password)
    click(wd, '#btn-login')
   
    WebDriverWait(wd, 60).until(
            ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '#HomeLayout > div.y-navbar > div > div.y-right-navbar > div:nth-child(1) > img'))
    )

# Get Ticket
    wd.get(url_tiket)
    if(int(urutan_tiket) == '0'):
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > a')
        for x in range(int(jumlah_tiket)-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div > div > div > div > div.incQuantity.itemQuantity > p')
    else:
        click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > a')
        for x in range(int(jumlah_tiket)-1):
            click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.box-category > div > div:nth-child('+urutan_tiket+') > div > div > div > div.incQuantity.itemQuantity > p')
    click(wd, '#DetailEvent > div.y-container-de > div > div.y-column.y-ticket-column.y-padside-12 > div > div.checkOutBox > div.checkOutButton > a')

# Checkout
    WebDriverWait(wd, 60).until(
        ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight'))
    )
    click(wd, '#BuyNow > div.y-popup > div > div.y-popup-footer > div.y-button.y-blue-button.y-popup-buttonRight')
    input_name_checkout = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input')
    print('++++++++++++++++++++'+input_name_checkout.get_attribute('value'))

    if(add_input_1 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_1 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(5) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_1.clear()
        column_input_1.send_keys(add_input_1)
    if(add_input_2 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(6) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_2 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(6) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_2.clear()
        column_input_2.send_keys(add_input_2)
    if(add_input_3 != ''):
        wait_before_ready(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(7) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_3 = wd.find_element_by_css_selector('#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(7) > div.y-inputPlace.y-inputHasIcon > input')
        column_input_3.clear()
        column_input_3.send_keys(add_input_3)

        
    WebDriverWait(wd, 60).until(
        ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(2) > div.y-inputPlace.y-inputHasIcon > input'), nama)
    )

    if(gender == 'male'):
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(1)')
    else:
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(1) > div.y-buynow-body > div > div:nth-child(4) > div.y-inputPlace.y-radio-group > div:nth-child(2)')

    for x in range(int(jumlah_tiket)):
        n = x+2
        click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(2) > div:nth-child('+str(n)+') > div > div:nth-child(2) > div.y-row.y-row-ticketuser > div.y-ticketuser-checkbox.y-checkbox.y-gray-text')
        print('==========='+str(n))
    
    
    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(4) > div.y-buynow-body > div.detailTiket > div > div:nth-child(1) > div > p')
    if(payment_method == 'permata'):
        click(wd, permata)
    elif(payment_method == 'mandiri'):
        click(wd, mandiri)
    elif(payment_method == 'bni'):
        click(wd, bni)
    elif(payment_method == 'other'):
        click(wd, other)


    click(wd, '#BuyNow > div.y-columns > div:nth-child(2) > div:nth-child(6) > div.y-buynow-body.y-black-text > div.y-button.y-blue-button.y-is-fullwidth')

# creating labels and entry widgets


l1 = Label(root, text="Yesplis",width=25,font=("times",20,"bold"),bg='blue',fg='white')
l1.place(x=70,y=20)
l2 = Label(root, text="Email",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l2.place(x=70,y=100)
# e1 = Entry(root,width=30,bd=2)
iemail = Entry(root,width=30,bd=2)
iemail.place(x=240,y=100)
l3 = Label(root, text="Password",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l3.place(x=70,y=130)
ipassword = Entry(root,show="*",width=30,bd=2)
ipassword.place(x=240,y=130)
l4 = Label(root, text="Nama",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l4.place(x=70,y=160)
inama = Entry(root,width=30,bd=2)
inama.place(x=240,y=160)
# dateEntry -Date selection entry with drop-down calendar



l5 = Label(root, text="Gender", width=20, font=("times",12,"bold"),anchor="w",bg='grey')
l5.place(x=70,y=190)

# radiobuttons
var = IntVar()
r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='grey')
r1.place(x=235,y=190)
r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12),bg='grey')
r2.place(x=315,y=190)

l6 = Label(root, text="Link Tiket",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l6.place(x=70,y=220)
iurl_tiket = Entry(root,width=30,bd=2)
iurl_tiket.place(x=240,y=220)

l10 = Label(root, text="Urutan Jenis Tiket",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l10.place(x=70,y=250)
iurutan_tiket = Entry(root,width=30,bd=2)
iurutan_tiket.place(x=240,y=250)

l10 = Label(root, text="Jumlah Tiket",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l10.place(x=70,y=280)
ijumlah_tiket = Entry(root,width=30,bd=2)
ijumlah_tiket.place(x=240,y=280)

l7 = Label(root, text="Select Payment",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l7.place(x=70,y=320)

# create a dropdown menu with the OptionMenu widget
cvar = StringVar()
cvar.set("Select course")
option = ("bni", "permata", "mandiri","other")
o = OptionMenu(root,cvar, *option)
o.config(font=("times",11),bd=3)
o.place(x=240,y=310,width=190)

l11 = Label(root, text="Additional Input 1",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l11.place(x=70,y=370)
iadd_input_1 = Entry(root,width=30,bd=2)
iadd_input_1.place(x=240,y=370)

l12 = Label(root, text="Additional Input 2",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l12.place(x=70,y=400)
iadd_input_2 = Entry(root,width=30,bd=2)
iadd_input_2.place(x=240,y=400)

l13 = Label(root, text="Additional Input 3",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l13.place(x=70,y=430)
iadd_input_3 = Entry(root,width=30,bd=2)
iadd_input_3.place(x=240,y=430)

# submit and cancel buttons
b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
b1.place(x=120,y=500)
b2 = Button(root, text='Resubmit Without Login',command=resubmit,width=25,bg='blue',fg='white',font=("times",12,"bold"))
b2.place(x=120,y=550)
b3 = Button(root, text='Resubmit & Login Again',command=relaunch,width=25,bg='red',fg='white',font=("times",12,"bold"))
b3.place(x=120,y=600)
# b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
# b2.place(x=320,y=440)

root.mainloop()