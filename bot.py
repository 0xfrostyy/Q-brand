import asyncio
from playwright.async_api import async_playwright, TimeoutError

# Yahan apna answer set karein ("A", "B", "C", ya "D")
ANSWER = "B"

# Yahan apne accounts ki list daal dein
accounts = [

    
{"username":"S2G-1","wallet":"BNJBfYbbZq1C68AsAWp9tyDqCDCgj5zfBZgzjRSYihLZ"},
{"username":"S2G-2","wallet":"EB2gsr2pwK9DJUeQX2YxCSKUNcaJckHu6p77Ay8RD8DJ"},
{"username":"S2G-3","wallet":"6WqbmefJXk6S5MH834vGH1J3L3iFHXSra9qC9puTaGdR"},
{"username":"S2G-4","wallet":"9vLnecBFin7sTvh76qaUvWAykSgsSp7p6juNaXAuxdhT"},
{"username":"S2G-5","wallet":"3uB6z5fNa3G9Uox6TE2ma46f8XCLEvRs7D5vpbjMUNdM"},
{"username":"S2G-6","wallet":"6NwUNyBDhHABy6VFtF3i9PVSqpQQHf6sQDvxTP68kLHT"},
{"username":"S2G-7","wallet":"HLjxcNt81Z5kuTg4gD1n8P7y3k1fCqekKRNrs3YaqeUZ"},
{"username":"S2G-8","wallet":"ANeWth8fiMHNgDXtKXTsFCMYDQXyQJembQ4RMcUSFEZf"},
{"username":"S2G-9","wallet":"B1mvqBcKseHEwZQVQLVE6TwnwTFionmzsrKDa7qZpXpf"},
{"username":"S2G-10","wallet":"AdCWDFLZRguRwdjwp3b2LN71VFAWpay5Djry7xhymX2o"},
{"username":"S2G-11","wallet":"DZku8S52eUceDY47nsN1C7GXWRuB3HmH9EKUBgHpPk96"},
{"username":"S2G-12","wallet":"AsspK1sq68nnKd5ZQzh4z8pRhjJofNzYC2zijGoru2j5"},
{"username":"S2G-13","wallet":"5JhEMRiXLYzX4CH8QWUuS5JJvTKmZ1LmDWnJupanrvpc"},
{"username":"S2G-14","wallet":"H5J65M7ZYxMS1oeAJ9Dy6NEnK8mGSohKiY7YhMsi7rn3"},
{"username":"S2G-15","wallet":"2GNq7nH3RdzaZHHdbyyTMo6sRwk4JjVURXKv314DzRXA"},
{"username":"S2G-16","wallet":"CoiTx7D7XHZn9UugMmCpBsWnDMHVCB6QnDRi7pnMv3zn"},
{"username":"S2G-17","wallet":"2tcNJf8kZXyiRLWJQGZwoCtgiZjP67pRpJpX4Xqo5EFn"},
{"username":"S2G-18","wallet":"CoxJPCoakr9zeiCpXMn994ukEx1wT9EzM2uhQisbhXJd"},
{"username":"S2G-19","wallet":"67ixBib7JMA114sudy9wJkJE819TtPYHve8tCNAzGz9B"},
{"username":"S2G-20","wallet":"GLyBSCLFqHVq6ng3bULfnHnG5me9giVuGQ4AJ7z14HAJ"},
{"username":"S2G-21","wallet":"BcjTPCE41mxVyXv5ebxDJdsQPHiWXDkmteP7SZgQCrQG"},
{"username":"S2G-22","wallet":"9wzAjPPfmJRDFfYbmQJYAN1bjcfXjWXE3ZjFQFGTKqUh"},
{"username":"S2G-23","wallet":"4B9LHfD2RsQBkMd3b3YCFpe2kNMJu4J5xw7ipYbQesAd"},
{"username":"S2G-24","wallet":"Cy9WofMnJHSZ7y4yvWtqiFWhsBZNLQzcD48BnJFKGk5a"},
{"username":"S2G-25","wallet":"AcPmMR354AEShi5qYHn1hmtjH3yEFCRb5xpUgXcfnLei"},
{"username":"S2G-26","wallet":"w7Dk9vpmFrR5bVoUiySCHNvq6k3dVyWaVThvTDaDYdR"},
{"username":"S2G-27","wallet":"CD2tytwTunZn6uijftsa5b1m1iWiW8X71cEFbwwpWBw4"},
{"username":"S2G-28","wallet":"5pGJJti9MtbY9C74D1qSaQoEkuWfcxptVBbpctGWJjY4"},
{"username":"S2G-29","wallet":"2q8EPvMZgTxjMctwNdex9G9fEM7FMxTeodSXm1SjgEN2"},
{"username":"S2G-30","wallet":"EXpvUzqpjjjMWmvH5Cjz1ag6W8KikAAE9LAzUU8yXwwF"},
{"username":"S2G-31","wallet":"6RUu5hUnWJtZCwibz8LApTxPZNncFXktP7LeHEusPY6X"},
{"username":"S2G-32","wallet":"2ajA8771TZNpdVAN9YS99LoeKAQVGcqD7Hev3Wi1z7Qk"},
{"username":"S2G-33","wallet":"2gnR4ZArkneYZ7sSHFdizucn6RSDReWphgyNZgaYMKvD"},
{"username":"S2G-34","wallet":"AKiSkBB6FKAUqzNTSdE9udTgQPKMpMpL7v8keEciC4FR"},
{"username":"S2G-35","wallet":"DpsVURqGz9pkADzi5earV4jfPvk29CJzTtCNdxbL3oNE"},
{"username":"S2G-36","wallet":"HTU8EGc3JTrWZVTRAu84M5mzbkXUFLGecbmgf8msfaJy"},
{"username":"S2G-37","wallet":"3BC6CTEdKseWxKaWhsWrFQVr1zKxe3JZ5EJs4AJLfBkS"},
{"username":"S2G-38","wallet":"FNaeXxgpTbb99kU7HDHhFaSa4bELJw1KnvVeLggKFD1C"},
{"username":"S2G-39","wallet":"99coSGfaziW5YgRpNrAzrTKhQ9iCCnxR77fbx9qHaAYZ"},
{"username":"S2G-40","wallet":"2T3ydERfY5BeJ8r8EtWaAdLv9e33KrSxizo4dTehTR4r"},
{"username":"S2G-41","wallet":"8ruAsneAUEjWyvDT89HteWQYJuwMAfKzHZF9ht3sgF1G"},
{"username":"S2G-42","wallet":"7of3ViX9BVaBhjXLPgTZczqcxovi7zNA7RhqZvWhNr3m"},
{"username":"S2G-43","wallet":"73HVSctyTj4iXQLa8LLMLCBYm1gYPtRayRQrSchq1nba"},
{"username":"S2G-44","wallet":"6s3hNjxViYQ77HdJLXytUVoxaVUhf8gWTBXbyH9W8RnN"},
{"username":"S2G-45","wallet":"4MsV2f9ArbsZaqptf9U3D33Exjp7UKTTYp7pajS4zHk3"},
{"username":"S2G-46","wallet":"A7LpS2nGPdYe34snrMiRjwAzRtwBHYk2FMe5CWz1mcUR"},
{"username":"S2G-47","wallet":"4mZHYw42kme4zRZ9g5CHy5i32JwPnqDasR3cgBKL76pn"},
{"username":"S2G-48","wallet":"ALmgUvmCTu5Eo3wkB7S1NEMvwR6vZTadMDq4t39PU5ap"},
{"username":"S2G-49","wallet":"2pgzzSM2UZ7edCPN5266MAZ7sTD7aDA6soMqUCitxdcz"},
{"username":"S2G-50","wallet":"27RhKkE59KUyMBqQvnhVwoTCgzBsAthmYvguVrW58uzg"},
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
