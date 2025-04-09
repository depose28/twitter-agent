from supabase import create_client
import os
from datetime import datetime

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_tweet(author, content):
    # Check if tweet already exists for that author + content
    existing = supabase.table("messages") \
        .select("id") \
        .eq("author", author) \
        .eq("content", content) \
        .execute()

    if existing.data:
        print(f"⏩ Skipped duplicate tweet from {author}")
        return

    # Otherwise, insert it
    data = {
        "author": author,
        "content": content,
        "timestamp": datetime.utcnow().isoformat()
    }

    supabase.table("messages").insert(data).execute()
    print(f"✅ Saved tweet from {author}")


