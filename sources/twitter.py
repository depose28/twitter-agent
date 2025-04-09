import asyncio
from playwright.async_api import async_playwright
from supabase_client import save_tweet

accounts = [
    ("0xfluid", "https://x.com/0xfluid"),
    ("DeFi_Made_Here", "https://x.com/DeFi_Made_Here")
]

async def scrape_twitter():
    print("🚀 Scraper started...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for name, url in accounts:
            print(f"🔍 Scraping {name} from {url}")
            await page.goto(url)
            await page.wait_for_selector('article div[lang]', timeout=15000)

            tweets = await page.eval_on_selector_all(
                'article div[lang]', 'elements => elements.map(e => e.innerText)'
            )

            for tweet in tweets:
                save_tweet(name, tweet)

        await browser.close()
