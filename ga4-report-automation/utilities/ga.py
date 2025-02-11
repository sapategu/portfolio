#!/usr/bin/python3

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
    OrderBy)
from dataclasses import dataclass
from typing import List,Final
from pandas import DataFrame
import pandas as pd
import os

from .base import Google_API

# ----------------------------------------------------------------------------------

@dataclass
class Google_Analytics_Data:
    """Google Analytics 4 API and Automations"""

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Google_API.SERVICE_ACCOUNT
    property_id = Google_API.GOOGLE_ANALYTICS_PROPERTY_ID
    date_range = List[str]


    def __repr__(self) -> str:
        data_info = ""

    def _request(self, dimensions: List[str], metrics: List[str], date_range: List[str]) -> DataFrame | None:
        """The request part from Google Analytics 4
        """

        self.dimensions = dimensions; self.metrics = metrics; self.date_range = date_range

        dimension_list = [Dimension(name=dimension) for dimension in dimensions]
        metric_list = [Metric(name=metric) for metric in metrics]

        # Run the Request Instances
        request = RunReportRequest(
            property=f'properties/{self.property_id}',
            dimensions=dimension_list,
            metrics=metric_list,
            order_bys=[OrderBy(dimension={'dimension_name': 'date'})],
            date_ranges=[DateRange(start_date=f'{date_range[0]}', end_date=f'{date_range[1]}')],
            limit=100000,
        )

        # Instantiates the beta analytics data client.
        response = BetaAnalyticsDataClient().run_report(request)

        # retrieve header name
        dimension_name = [header.name for header in response.dimension_headers]
        metric_name = [header.name for header in response.metric_headers]

        # data store
        data = {}; dimension_values = []; metric_values = []

        # Store the all dimension values from response
        for i in range(len(dimension_name)):
            dimension_values.append(
                [row.dimension_values[i].value for row in response.rows]
            )

        # Changing the date type from <class 'str'> to suggested date format
        dimension_values[0] = pd.to_datetime(dimension_values[0], format='%Y%m%d').date

        # Store the all data values from response
        for i in range(len(metric_name)):
            metric_values.append([row.metric_values[i].value for row in response.rows])


        # Combining the all recorded data into DataFrame
        for i in range(len(dimension_name)): data[f'{dimension_name[i]}'] = dimension_values[i]
        for j in range(len(metric_name)): data[f'{metric_name[j]}'] = metric_values[j]

        # Change header name to proper way
        # Update keys from data with recorded dictionary values, and pop out the old keys
        for keys in Google_API.DIMENSIONS_METRICS:
            if keys in data:
                data[Google_API.DIMENSIONS_METRICS[keys]] = data.pop(keys)
        
        # return DataFrame
        return pd.DataFrame(data)

        # # return Google Analytics 4 request
        # return response

    def user_activity(self, data: DataFrame) -> DataFrame | None:
        """Filtering Page Title and Screen Class value with suggested Page Title and Screen Class"""

        user_activity = data['Page Title and Screen Class'].isin(Google_API.USER_ACTIVITY)
        data = data[user_activity]
        return data

    def download_sheets_csv(self, data: DataFrame, file_name: str) -> str | None:
        """Downloading recorded data to CSV format file"""

        file = pd.DataFrame(data)
        save = file.to_csv(f'data/{file_name}.csv', index = False)
        return f'File {file_name}.csv succesfully saved !'


    def download_sheets_xlsx(self, data: DataFrame, file_name: str) -> str | None:
        """Downloading recorded data to Excel format file"""

        file = pd.DataFrame(data)
        save = file.to_excel(f'data/{file_name}.xlsx', index = False)
        return f'File {file_name}.xlsx succesfully saved !'


        
