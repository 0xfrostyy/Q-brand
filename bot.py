import asyncio
from playwright.async_api import async_playwright, TimeoutError

# Yahan apna answer set karein ("A", "B", "C", ya "D")
ANSWER = "A"

# Yahan apne accounts ki list daal dein
accounts = [

    

  {"username": "tatto-1", "wallet": "5TgSFA5zpTsVwPvwgz9YTjDTgKbm7jHg66aMeBcdgVQH"},
  {"username": "tatto-2", "wallet": "BsZ3AepHyRXofAXxA1RJPVaBnfFaq3ErdqbqKNnktt1r"},
  {"username": "tatto-3", "wallet": "4iPa3CrZkqdZAwdPkryfCmo8QpwbuXTHm2wEnYQdBqhJ"},
  {"username": "tatto-4", "wallet": "HZFX53P3o93TCLpHUkyLVqPAZwZXxzG8kZnZSo66UpnP"},
  {"username": "tatto-5", "wallet": "8UpMgyRFgECKyQz5rRXHVjwLb3Be5AtLGr9QEzvTY2ut"},
  {"username": "tatto-6", "wallet": "5ajhLsbgTbzUrcxmHraf5j4uKfaxr17a96qhayY8bGFP"},
  {"username": "tatto-7", "wallet": "6zuBrezJCcAx8czyTcq1kKkChLsbKigMLZdYhu4kMDwz"},
  {"username": "tatto-8", "wallet": "7BAEgkgfgEGHaaQd9TJYz2EeHzFDRHmmFFwinxrM8cXq"},
  {"username": "tatto-9", "wallet": "9yTdhnT6MAsdUNwamU8gbJmRDnkySjMWrnzRityGG6HE"},
  {"username": "tatto-10", "wallet": "D8svR9PqpLQoY6AiTEcqvUeanAxyYEP52vWLdC1wV1hZ"},

    # {"username": "apna_username_2", "wallet": "0xYourWalletAddressHere2"},
]

async def handle_modal(page):
    modal = page.locator("#scamMigrationWarningModal")
    try:
        if await modal.is_visible(timeout=5000):
            print("⚠️ Closing modal...")
            buttons = modal.locator("button")
            if await buttons.count() > 0:
                await buttons.first.click()
                await page.wait_for_timeout(1000)
    except:
        pass

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        for acc in accounts:
            context = await browser.new_context()
            page = await context.new_page()

            print("Running account:", acc["username"])

            try:
                await page.goto("https://theros.io/prelaunch", timeout=80000)
                await page.wait_for_load_state("networkidle", timeout=15000)
            except TimeoutError:
                print(f"Timeout for {acc['username']}. Skipping.")
                await context.close()
                continue

            await handle_modal(page)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("input", timeout=15000)

            inputs = await page.query_selector_all("input")
            if len(inputs) < 2:
                print(f"Not enough inputs for {acc['username']}, skipping")
                await context.close()
                continue

            await inputs[0].fill(acc["username"])
            await inputs[1].fill(acc["wallet"])

            if len(inputs) > 2:
                await inputs[2].fill("bot")

            await handle_modal(page)

            create_btn = page.locator("#registerBtn")
            try:
                await create_btn.click(timeout=9000)
            except TimeoutError:
                await create_btn.click(force=True)

            next_btn = page.locator("#nextQuestionBtn")
            try:
                await next_btn.wait_for(state="visible", timeout=8000)
                await next_btn.click()
            except:
                pass

            answer_selector = f"#answer{ANSWER.upper()}"
            try:
                await page.locator(answer_selector).click(timeout=20000)
                print("Answered:", ANSWER)
            except Exception as e:
                print(f"Failed to answer: {e}")

            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
