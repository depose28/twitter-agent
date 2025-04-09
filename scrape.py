import asyncio
from sources.twitter import scrape_twitter

async def main():
    await scrape_twitter()
    # Later: add other sources like Discord or Dune here

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


