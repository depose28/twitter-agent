from sources.twitter import scrape_twitter
import asyncio

async def main():
    await scrape_twitter()

if __name__ == "__main__":
    asyncio.run(main())
