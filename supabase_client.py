import os
from supabase import create_client, Client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_tweet(author: str, content: str):
    data = {
    "author": author,
    "content": content,
    "company": "Twitter"  # 🧩 Added to fix the NOT NULL error
}

    supabase.table("messages").insert(data).execute()

