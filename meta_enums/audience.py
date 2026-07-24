"""
Meta Marketing API - Audience Enums
"""

# Gender
GENDERS = {
    "All": [],
    "Male": [1],
    "Female": [2],
}

# Age
AGE_MIN = list(range(13, 66))
AGE_MAX = list(range(13, 66))

# Languages
LANGUAGES = {
    "All": "",
    "English": 1000,
    "Indonesian": 6,
}

# Geo Location Type
LOCATION_TYPES = {
    "Home": "home",
    "Recent": "recent",
    "Travel In": "travel_in",
}

# Radius Unit
RADIUS_UNITS = {
    "Kilometer": "kilometer",
    "Mile": "mile",
}

# Device Platform
DEVICE_PLATFORMS = {
    "All": [],
    "Mobile": ["mobile"],
    "Desktop": ["desktop"],
}

# Operating System
OPERATING_SYSTEMS = {
    "All": [],
    "Android": ["Android"],
    "iOS": ["iOS"],
}

# Connection
CONNECTION_TYPES = {
    "All": "",
    "WiFi": "wifi",
    "Cellular": "cell",
}

# Audience Type
AUDIENCE_TYPES = {
    "Saved Audience": "saved",
    "Custom Audience": "custom",
    "Lookalike Audience": "lookalike",
}

# Lookalike Country Limit
LOOKALIKE_SIZE = {
    "1%": 0.01,
    "2%": 0.02,
    "3%": 0.03,
    "5%": 0.05,
    "10%": 0.10,
}
