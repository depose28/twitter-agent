
import asyncio
from playwright.async_api import async_playwright
from supabase_client import save_tweet

async def scrape_twitter():
    print("🚀 Scraper started...")  # <-- This is the debug line we're adding

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://x.com/0xfluid")
        await page.wait_for_selector('article div[lang]', timeout=15000)

        tweets = await page.eval_on_selector_all(
            'article div[lang]', 'elements => elements.map(e => e.innerText)'
        )
        await browser.close()

        for tweet in tweets:
            save_tweet("0xfluid", tweet)


