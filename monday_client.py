import requests
import os
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")

def fetch_board_items(board_id):
    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            id
            name
            column_values {{
              column {{
                title
              }}
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        "https://api.monday.com/v2",
        json={"query": query},
        headers={"Authorization": MONDAY_API_KEY}
    )

    return response.json()