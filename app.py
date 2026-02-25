from monday_client import fetch_board_items
import os
from dotenv import load_dotenv

load_dotenv()

BOARD_1_ID = os.getenv("BOARD_1_ID")

data = fetch_board_items(BOARD_1_ID)

print(data)