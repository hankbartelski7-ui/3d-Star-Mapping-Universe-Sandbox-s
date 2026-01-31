import requests

# Example: list of names from Wikipedia or other sources
names_to_check = [
    "GJ 581",
    "Gliese 581",
    "HIP 74995",
    "Kepler-404"
]

# Function to query NASA Exoplanet Archive
def check_nasa_name(name):
    # NASA Exoplanet Archive TAP API
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    query = f"""
    SELECT pl_name, hostname
    FROM ps
    WHERE pl_name LIKE '%{name}%' OR hostname LIKE '%{name}%'
    """
    params = {
        "query": query,
        "format": "json"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if len(data) > 0:
            # Return the official NASA names found
            return [d['pl_name'] for d in data]
        else:
            return None
    except Exception as e:
        return f"Error: {e}"

# Check each name
for name in names_to_check:
    result = check_nasa_name(name)
    if result:
        print(f"Input: {name} → NASA official: {result}")
    else:
        print(f"Input: {name} → Not found in NASA archive")
