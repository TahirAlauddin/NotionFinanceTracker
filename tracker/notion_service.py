from .models import FinancialRecord
import requests
from django.conf import settings

BASE_URL = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {settings.NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_financial_data():
    url = f"{BASE_URL}/databases/{settings.NOTION_DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")  # Log the error details
        return None
    
def save_financial_data(user, notion_data):
    for item in notion_data['results']:
        # Print the raw item for debugging
        print(item)

        # Extract properties
        properties = item['properties']
        notion_id = item['id']  # Unique ID for the page in Notion

        # Extract date, handling cases where the date property might not exist
        date = properties['Date']['date']['start'] if 'Date' in properties and properties['Date']['date'] else None

        # Extract amount, handling cases where the amount property might not exist
        amount = properties['Amount']['number'] if 'Amount' in properties and properties['Amount']['number'] is not None else 0

        # Extract category, handling cases where the category property might not exist
        category = properties['Category']['select']['name'] if 'Category' in properties and properties['Category']['select'] else "Uncategorized"

        # Extract description, handling cases where the description property might not exist
        description = properties['Description']['rich_text'][0]['text']['content'] if 'Description' in properties and properties['Description']['rich_text'] else ""

        # Check if the record already exists, if not, create a new one
        if not FinancialRecord.objects.filter(notion_id=notion_id).exists():
            FinancialRecord.objects.create(
                user=user,
                notion_id=notion_id,
                date=date,
                amount=amount,
                category=category,
                description=description
            )

