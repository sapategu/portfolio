#!/usr/bin/python3

# from __future__ import annotations
# import argparse

from utilities.ga import Google_Analytics_Data
from utilities.sheets import Google_Sheets_Config
from os import system, name
from colorama import (
    Fore, Back,
    init as colorama_init
)
# from tqdm import tgrange # Loading animation
from time import sleep
import time
from datetime import datetime, timedelta
import os

ANALYTICS = Google_Analytics_Data()
SHEETS = Google_Sheets_Config()

def cmd_clear():
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

def user_activity_update(request):
    
    if 'Page Title and Screen Class' not in request.columns.values.tolist():
        return 'Only Updating if Page Title and Screen Class are included.'
    
    return SHEETS.update_user_activity_from_analytics(request)

def user_activity_download(request) -> None:

    if 'Page Title and Screen Class' not in request.columns.values.tolist():
        file_name = input("The File Name: ")
        type = input("type of the sheets, a. xlsx or b. csv: ")
        
        if type == 'a': print(ANALYTICS.download_sheets_xlsx(request, file_name))
        if type == 'b': print(ANALYTICS.download_sheets_csv(request, file_name))
    
    else:
        choice = int(input("\nWant to: \n1. all recorded page\n2. suggested page\nYour choice: "))
        if choice == 1:
            file_name = input("The File Name: ")
            type = input("type of the sheets, a. xlsx or b. csv: ")
            
            if type == 'a': print(ANALYTICS.download_sheets_xlsx(request, file_name))
            if type == 'b': print(ANALYTICS.download_sheets_csv(request, file_name))

        elif choice == 2:
            user_activity = ANALYTICS.user_activity(request)
            file_name = input("The File Name: ")
            type = input("type of the sheets, a. xlsx or b. csv: ")
                
            if type == 'a': print(ANALYTICS.download_sheets_xlsx(user_activity, file_name))
            if type == 'b': print(ANALYTICS.download_sheets_csv(user_activity, file_name))


def main() -> None:
    
    cmd_clear()

    print("""\n\nWelcome to Google Analytics Automations for Performance""")
    choice = int(input("""
        Choose your action : 
        1. Update Performance - User Activity
        2. Download Data from Google Analytics
        3. Google Analytics - Dataframe in Terminal
        4. Download Data from Google Sheets
        5. Performance Data Info

        6. Exit
        
        Your Choice : """))

    match choice:
        case 1:
    
            start_time = time.time()
            dimensions_input = ['date','unifiedScreenClass']
            metrics_input = ['activeUsers','screenPageViews']
            # date_range = SHEETS.user_activity_last_date_data()
            date_range = []; today = datetime.today()
            for day in range(5):
                date = today - timedelta(days=day)
                date_range.append(date.strftime('%Y-%m-%d'))

            for date in range(0, len(date_range)):
                request = ANALYTICS.request(
                    dimensions = dimensions_input,
                    metrics = metrics_input,
                    date_range = [f'{date_range[date]}','today']
                )

            choice = int(input("\nWant to:\n1. all recorded page\n2. suggested page\nYour choice: "))
            if choice == 1: print(user_activity_update(request))
            elif choice  == 2:
                user_activity = ANALYTICS.user_activity(request)
                print(user_activity_update(user_activity))


            print("\n\nExecuted in ------- %s sec -------" % (time.time() - start_time))

            # Back to Main Menu
            decisions = input("back to main menu (Y/N) : ")
            return quit() if decisions.lower() == 'n' else main()


        case 2:
            start_time = time.time()
            print("\nThe Input in string format with comma separated. No Space needed\n")

            # Google Analytics 4 Dimensions and Metrics API -> https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema
            dimensions_input = list(map(str, input("Dimensions : ").split(',')))
            metrics_input = list(map(str, input("Metrics : ").split(',')))
            date_input = list(map(str, input("Date Range : ").split(',')))
            
            # run the request
            request = ANALYTICS.request(
                dimensions = dimensions_input,
                metrics = metrics_input,
                date_range = date_input
            ) 

            print(user_activity_download(request))
            print("\n\nExecuted in ------- %s sec -------" % (time.time() - start_time))
            
            # Back to Main Menu
            decisions = input("back to main menu (Y/N) : ")
            return quit() if decisions.lower() == 'n' else main()


        case 3:
            start_time = time.time()
            print("\nThe Input in string format with comma separated. No Space needed\n")

            # Google Analytics 4 Dimensions and Metrics API -> https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema
            dimensions_input = list(map(str, input("Dimensions: ").split(',')))
            metrics_input = list(map(str, input("Metrics: ").split(',')))
            date_input = list(map(str, input("Date Range: ").split(',')))

            request = ANALYTICS.request(
                dimensions = dimensions_input,
                metrics = metrics_input,
                date_range = date_input
            )

            choice = int(input("Want to: \n1. all recorded page or \n2. suggested page: "))
            if choice == 1: print(request)
            elif choice  == 2:
                user_activity = ANALYTICS.user_activity(request)
                print(roli_user_activity)

            print("\n\nExecuted in ------- %s sec -------" % (time.time() - start_time))

            # Back to Main Menu
            decisions = input("back to main menu (Y/N) : ")
            return quit() if decisions.lower() == 'n' else main()
        
        
        case 4:
            start_time = time.time()

            worksheet_name = input("\nWhich worksheet that you want to save : ")
            file_name = input("The File Name: ")
            type = input("type of the sheets, a. xlsx or b. csv: ")
            
            if type == 'a': print(SHEETS.download_sheets_xlsx(
                file_name = file_name,
                worksheet_name = worksheet_name))

            if type == 'b': print(SHEETS.download_sheets_csv(
                file_name = file_name,
                worksheet_name = worksheet_name))
            
            print("\n\nExecuted in ------- %s sec -------" % (time.time() - start_time))

            # Back to Main Menu
            decisions = input("back to main menu (Y/N) : ")
            return quit() if decisions.lower() == 'n' else main()


        case 5:
            start_time = time.time()
            print(f'{SHEETS.get_last_date_data()}\n\n{SHEETS.list_of_worksheets()}')

            print("\n\nExecuted in ------- %s sec -------" % (time.time() - start_time))


        case 6:
            decisions = input("are your really want to quit (Y/N) : ")
            return quit() if decisions.lower() == 'y' else main()
        

        case _:
            print("\nInput from 1 - 8. Back to Main Menu...")
            sleep(2)
            cmd_clear()
            main()
        


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    main()
    
