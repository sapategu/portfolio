#!/usr/bin/python3


class Google_API:
    
    # Google Cloud Service Account Private Key
    SERVICE_ACCOUNT = "YOUR GCP SERVICE ACCOUNT"
    
    # Google Analytics Property Instances
    GOOGLE_ANALYTICS_PROPERTY_ID = 'YOUR GA PROPERTY ID'

    DIMENSIONS_METRICS = {

        # DIMENSIONS
        'date': 'Date',
        'unifiedScreenClass': 'Page Title and Screen Class',
        'region': 'Region',
        'firstUserDefaultChannelGroup': 'First User Default Channel Group',
        'newVsReturning': 'New / Returning',
        'mobileDeviceMarketingName': 'Device',
        'deviceModel': 'Device Model',
        'firstUserMedium': 'First User Medium',
        'firstUserSource': 'First User Source',
        'firstUserSourceMedium': '% Source/Medium',
        'brandingInterest': 'Interest',
        'deviceCategory': 'Device Category',
        'userGender': 'Gender',
        'unifiedScreenName': 'Page Name',

        # METRICS
        'active1DayUsers': 'DAU',
        'active7DayUsers': 'WAU',
        'activeUsers': 'Active Users',
        'screenPageViews': 'Views',
        'bounceRate': 'Bounce Rate',
        'engagementRate': 'Engagement Rate',
        'newUsers': 'New Users',
        'crashFreeUsersRate': 'Crash Free-User Rate'
    }

    # roli Suggested User Activity
    USER_ACTIVITY = [
        'LockScreenBackgroundActivity',
        'WheelFortuneActivity',
        'SurveyAdvancedDetailActivity',
        'RewardDetailActivity',
        'DetailArtikelListWebActivity',
        'ProfileActivity',
        'CerpenActivity',
        'InviteFriendActivity',
        'ActivateLockscreenActivity',
        'SurveyDetailActivity',
        'ListArtikelActivity',
        'DetailCerpenActivity',
        'CerpenChapterActivity',
        'InterestsActivity',
    ]

    # Google Sheets Instances
    MAIN = 'https://docs.google.com/spreadsheets/d/'
    SHEET_ID = 'YOUR SHEET ID'
    SCOPE = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    # Google Sheets for Performance Dashboard Data
    WORKSHEET = {
        'Engagement': '/edit#gid=338496162',
        'Loss': '/edit#gid=700001040',
        'Content roli': '/edit#gid=1093174183',
        'Content Click': '/edit#gid=2144020646',
        'Broadcast Hit': '/edit#gid=161726572',
        'Wording Non Register': '/edit#gid=888538644',
        'User Activity': '/edit#gid=1365463268',
    }


    # Google Play Console Property Instances
    GPC_SERVICE_ACCOUNT = ''
    GOOGLE_PLAY_CONSOLE_APP_ID = ''
    API_KEY = ""
    CLIENT_ID = ""
    CLIENT_SECRET = ""
    
