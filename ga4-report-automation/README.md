# Google Analytics 4 Automations Data for Performance Dashboard

### OFFICIAL References Links:
1. [API QUICKSTART](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries)
2. [Google Analytics Data API OVERVIEW](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/?apix=true)
3. [v1beta Google Analytics API Properties](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties)
4. [Google Analytics 4 Dimensions and Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)
5. [Google Cloud Client Libraries for google-analytics-data (Beta Analytics Data Client)](https://googleapis.dev/python/analyticsdata/latest/data_v1beta/beta_analytics_data.html#google.analytics.data_v1beta.services.beta_analytics_data.BetaAnalyticsDataClient)
6. [RunReportRequest()](https://googleapis.dev/python/analyticsdata/latest/data_v1beta/types.html#google.analytics.data_v1beta.types.RunReportRequest)
7. [Official Google API Repositories](https://github.com/googleapis/google-api-python-client)


### The overview of the process:
1. Get API keys: create a GCP project, authorize Google Analytics Data API, create a service account, create JSON keys for the account.
2. Add service account as a viewer to your GA4 property
    - Admin -> Account Access Management, 
    - Properties -> Property Access Management
3. Install google-analytics-data package.
4. Set os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'your_api_key.json'
5. Send request, get output. Done!

### Automations Project Directory Info
1. **assets** = some text documentations or screenshoots
2. **data** =  where the downloaded data from applications are saved on
3. **utilities** = the python class for Google Aplications automations
   - **__pycache__** = python execution caches, not to be really care
   - **base.py** = the credentials, GA4 property id, dimensions and metrics, google sheets credentials
   - **credentials.py** = the Google Cloud Platfrom service account private keys
   - **ga.py** = Google Analytics 4 API and Automations
   - **sheets.py** = Google Sheets API and Automations
6. **venv** = python virtual environment
7. **.gitignore** = git ignore documentations for python
8. **main.py** = main python file for executed
9. **README.md** = Projects documentations
10. **requirements.txt** = list of python libraries, package

### Managing Virtual Environment and Libraries
1. Installing python-pipenv
    ```
    pip install python-pipenv
    ```
2. Creating Virtual Enviroment
    ```
    pipenv shell
    ```
3. Downloading and Installing the Libraries from requirements.txt
    ```
    pipenv install -r ./requirements.txt
    ```
4. Creating and Saving some libraries (if updated, deleted, and et cetera) to requirements.txt
    ```
    pipenv lock -r > requirements.txt
    ```

### How to use

1. Open CMD
2. go to project directory
3. activate virtual environment with command
4. Look the left side of directory line if virtual environment already active (in this case will (venv))
5. If already activate just launch the applications with command python main.py


Features:
1. Update Performance - User Activity
   - Update directly from Google Analytics 4 to suggested Google Sheets
   - for unifiedScreenClass(Page Title and Screen Class), there is option whether suggested page or all recorded page
   - can customize the file name
   - the file type can be .csv or .xlsx as you needs

3. Download Data from Google Analytics
   - Get Google Analytics 4 data for Local consumption (Tableau, Power BI, etc)
   - if unifiedScreenClass are mentioned as one of dimensions, will get option like (1) point b.
   - can customize the file name
   - the file type can be .csv or .xlsx as you needs

5. Google Analytics - Dataframe in Terminal
   - Retrive Google Analytics 4 data and it can show as dataframe in terminal
   - if unifiedScreenClass are mentioned as one of dimensions, will get option like (1) point b.

7. Download Data from Google Sheets
   - Download entire suggested worksheet data from Performance spreadsheets
   - can customize the file name
   - the file type can be .csv or .xlsx as you needs

9. Performance Data Info
   - list of worksheet in Performance
   - last update data date

11. Exit
   exit from applications

### Dimensions and Metrics Template
```
req = ga.request(
    dimensions = ['date','unifiedScreenClass'],
    metrics = ['activeUsers'],
    date_range = ['2022-01-01','today']
)
```
