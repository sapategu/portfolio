#!/usr/bin/python3

from oauth2client.service_account import ServiceAccountCredentials
import gspread as Spreadsheet
from dataclasses import dataclass
from typing import List
from datetime import datetime, time, timedelta
import pandas as pd

from .base import Google_API

# -----------------------------------------------------------------------------------

@dataclass
class Google_Sheets_Config:
    """Google Sheets API and Automations"""

    # Set up the Service Accounts with Credentials Keys
    CREDS = ServiceAccountCredentials.from_json_keyfile_name(
        Google_API.SERVICE_ACCOUNT,  
        Google_API.SCOPE
    )
    CLIENT = Spreadsheet.authorize(CREDS)
    SPREADSHEET = CLIENT.open_by_key(Google_API.SHEET_ID)

    # Some variables
    selected_worksheet = ''
    isUpdate = False
    date_range = str
    last_data_date = str

    def get_worksheet_access(self, sheet_name: str) -> None:
        """Getting sheets informations with suggested sheet name"""
        return pd.DataFrame(self.SPREADSHEET.worksheet(sheet_name).get_all_values())

    def creating_sheets(self, sheet_name: str, rows: int = 1000, cols: int = 10) -> str | None:
        """Creating worksheets with existing sheet"""

        new_worksheet = self.SPREADSHEET.add_worksheet(title = sheet_name, 
                                                        rows = rows,
                                                        cols = cols)
        self.selected_worksheet = new_worksheet
        return f'{sheet_name} is sucessfully created !!'

    def user_activity_last_date_data(self, sheet_name: str = 'User Activity') -> str | None:
        """Getting Last recorded date of data from suggested sheet"""

        sheet = pd.DataFrame(self.SPREADSHEET.worksheet(sheet_name).get_all_values())
        sheet_last_day = sheet[0].tail(250)
        return list(set(sheet_last_day))

    def check_existing_data(self, sheet_name: str) -> str | None:
        pass


    def update_user_activity_from_analytics(self, request_data) -> str | None:
        """Updating User Activity worksheets from Google Analytics 4 requested data"""

        info = ''

        if request_data['Date'].all():
            request_data['Date'] = request_data['Date'].astype(str)

        sheet = self.SPREADSHEET.worksheet('Automations')
        rows = sheet.row_count; cols = len(request_data.values.tolist())
        if rows < cols: sheet.add_rows(cols)
        try:
            sheet.update(
                f'A{1}:D{cols}',
                [data for data in request_data.values.tolist()]
            )
            info += 'Updated!!'
        except Exception as e:
            info += 'Cannot Update. Fix the Logic!'

        return info

    def format_data(self, worksheet_name: str) -> str | None:
        """Formatting last 3-4 days from sugested sheet with custom format"""

        # get last 3 days of date data -> Unwork yet
        for date in self.get_last_date_data(worksheet_name):
            print(date)

        worksheets = self.SPREADSHEET.worksheet(worksheet_name)
        worksheets.formatworksheet.format(
            "A2:B2",
            {
                "backgroundColor": { "red": 0.0,"green": 0.0,"blue": 0.0 },
                "horizontalAlignment": "CENTER",
                "textFormat": {
                    "foregroundColor": {
                        "red": 1.0,
                        "green": 1.0,
                        "blue": 1.0
                    },
                    "fontSize": 12,
                    "bold": True
                }
            })

        return "Updated!!"
 
    
    def list_of_worksheets(self) -> List[str] | None:
        """Listing the all worksheeets from existing sheet"""

        worksheets = self.SPREADSHEET.worksheets()
        for worksheet in worksheets: print(worksheet)

    
    def download_sheets_csv(self, file_name: str, worksheet_name: str) -> str | None:
        """Downloading recorded data to CSV format file"""

        save = self.get_worksheet_access(worksheet_name).to_csv(
            f'data/{file_name}.csv', 
            index = False
        )
        return f'File {file_name}.csv succesfully saved !'


    def download_sheets_xlsx(self, file_name: str, worksheet_name: str) -> str | None:
        """Downloading recorded data to Excel format file"""

        save = self.get_worksheet_access(worksheet_name).to_excel(
            f'data/{file_name}.xlsx', 
            index = False,
        )
        return f'File {file_name}.xlsx succesfully saved !'
