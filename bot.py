import asyncio
from playwright.async_api import async_playwright, TimeoutError

ANSWER = "B"

accounts = [


{"username":"HC-1","wallet":"Eb9jymzeWjX8MsH4F698k8EetswHcUiPEY5vEFjtx74k"},
{"username":"HC-2","wallet":"6JsyAAsVyKWQaDHMDZK5ZVZ9Xi294cGfMDCvWj8tfa8u"},
{"username":"HC-3","wallet":"Awbg9VZ6FgT5L3X8CLuRY17AcpfkqMW1vnUKgmiSw3gm"},
{"username":"HC-4","wallet":"GtjzWWZMb7AnajH7ChE67oeaeK9RrQpEEaahKq2iHKkT"},
{"username":"HC-5","wallet":"HPqQVKWYZxFB5sKu2UuThhpZ4VJz2U2g7WMuwuSZj34D"},
{"username":"HC-6","wallet":"7Ka6GnteXcFpHQmcPNsp8WAcfSadMBgEsPmjCkbVwN5z"},
{"username":"HC-7","wallet":"GPzftdABFvfUaLDM2cefz4gPeCAo99ESCf1wUWZU4an5"},
{"username":"HC-8","wallet":"8wCb8PaP3gcdiwSAHzSx33o3Snq6RnmDrJwzcBN1d5gZ"},
{"username":"HC-9","wallet":"D3LmyLrJwyzk9okzbhttN22YdFRkDVs7ouuNjZuBVRfo"},
{"username":"HC-10","wallet":"6cW6nBzSmaRJ78uuQp9eQo4GsFv2RqcuqZQGYd8V7cbF"},
{"username":"HC-11","wallet":"FMqFFgQ8pENMmLAtiThwU3pmqGDjni2zDyPTKfN9opsw"},
{"username":"HC-12","wallet":"3fU2XjdzipcNeG4tRArZaJvAunmYsDWzjaVR3VV1APuq"},
{"username":"HC-13","wallet":"HjBubpPxF9aSJ3crBXH2HoQVo3ypmsnTH61fpqYuKHHc"},
{"username":"HC-14","wallet":"2E8iyPdL7bSRfX7JryVBjaEMmjbLdf4nQymopTbWyUqB"},
{"username":"HC-15","wallet":"Ge6h9zQSWgcE1gSAcnZirPiU2KZwNrfiYstTmC4T5naR"},
{"username":"HC-16","wallet":"3fsfUYhcwoc7CuHJ7Pg6RVcgooera15bCw7BqmhW7GDv"},
{"username":"HC-17","wallet":"4G6EY6xaMhQQqDopFJ8BkFJm5EeWfexkypoWYhrtSkke"},
{"username":"HC-18","wallet":"8ENWkfPEnX5SyJV5g7zuXDTccCb1DTTLDSvTykjv47ig"},
{"username":"HC-19","wallet":"67LhjfjMdjGu65QqQdu6rMudmTver99BJixHVUR7AnEn"},
{"username":"HC-20","wallet":"8GJwoxY5X54Qdo7MKyzeE1nYogaaQ7mLi3FS2TSzRv4h"},
{"username":"HC-21","wallet":"4fpFY9jSxoyPVHLssY9fg55h8AQPzB413Px45HDPKhus"},
{"username":"HC-22","wallet":"ETsPEAwF6h238YnNrrsQPjyNc1NDGVTJAuLi6V2gfEJ"},
{"username":"HC-23","wallet":"8LrmFZLcN6QYPeUSBxftaDAUfyswjEaCLwDPsLWDYvtu"},
{"username":"HC-24","wallet":"2LF6tW7xqQNcVZrbwKeSz2rjHeR8pzPN2sGE1MtS7WmY"},
{"username":"HC-25","wallet":"FYhAvP84CpCuy4Fst1EGhnNdGuwEsy6LWGCMiimBK1gR"},
{"username":"HC-26","wallet":"G4Frt4jE7wTN5L1kZfgJzvdop4XecqZtzQKh4vYYEKaG"},
{"username":"HC-27","wallet":"6BFBow38XZ7a7vnMdCXgKPgQc4pEwcQ5VEE7Vn8TNJAE"},
{"username":"HC-28","wallet":"DtjTgZuYdCxVE3xhu416kGGCsUcpC4WExkwtmnuiR9F"},
{"username":"HC-29","wallet":"Fy9usJF5vsTKY8Ar53fmFgCYwHrkndfgbGjicuuGP7P"},
{"username":"HC-30","wallet":"HKfV39d3KEy1HhDc9vgJ7fv5aEXESGbft6LpPLME1yyU"},
{"username":"HC-31","wallet":"BvsQ5mCdaw7sff32u47RqDjvXvkKL4epH5oML4VNUdo5"},
{"username":"HC-32","wallet":"Gd8PkP9MbKz6ogvXECZjA565V8ieTmQvsnKMRzQEbrFv"},
{"username":"HC-33","wallet":"J3px8A6fNgcGe2HmP3y5HiroSPSY7xdWmVHkfaiinpfd"},
{"username":"HC-34","wallet":"3vxaDSquFcpzs8phKFqXJwHYzq13aaGpDPZG7kzwuJrG"},
{"username":"HC-35","wallet":"6dEh5u8BsEmH8yaUoTDLRVSWDq1SEojnCvkazAe1uFqn"},
{"username":"HC-36","wallet":"Hh9Ni8pfuFPJAGXF4M7HW9SbyJ6pPG3NYhS7xamUkBXs"},
{"username":"HC-37","wallet":"4NXfW9Sg361W8vq3pdsotUP8qrgonj2TgaayKekLSSZd"},
{"username":"HC-38","wallet":"2F2hi74TezqwhjfpXB8yyQzXWLzfvpA6jbW5botq29XJ"},
{"username":"HC-39","wallet":"FhdEUm4kjzg3qLKN9Awxhx8Pzpbsn2vzLLPcyQ1Ztg9Y"},
{"username":"HC-40","wallet":"4dWg23TPYnc3tjqEvkVEAPwz3ERogU3dBRxFWyjghJx5"},
{"username":"HC-41","wallet":"Ee6aW5K4wpZp1NhAALxEJLoGqy96hNhc7uph6rEPgh5"},
{"username":"HC-42","wallet":"73YZM94As6QgQJJ6LqBZYT5VBVD6HAcMiZKatC8EAuS6"},
{"username":"HC-43","wallet":"2pmHDuDPQAi3EHvTuaZ7488rq9DoxjsH7go9jHHsNHGi"},
{"username":"HC-44","wallet":"9efqJdRien5iugwpsJfkaWP6xGhpqHYSEt9t8CJSjrhf"},
{"username":"HC-45","wallet":"6XCZRiW4AzqVxbzuRaFcDfrx1yvtpom5KZXjXgRGjoow"},
{"username":"HC-46","wallet":"7LTfVsH9PkHaoDrnz7S2wgdGohGaSmbtXMs72RA6r8xi"},
{"username":"HC-47","wallet":"Ez8qPmDDrU9JQ2x9zn4NNxztZXb4wupKpkSVQu179SeY"},
{"username":"HC-48","wallet":"2rwrBS9b7EVB3UBsjAqDjqgPAyXEFfXVb9JWynab2UN2"},
{"username":"HC-49","wallet":"99M6wop4EZwwvo6XZSJbZPk98VuAwZZAsKWVwanKWFac"},
{"username":"HC-50","wallet":"3f7s2bCVm4cRQtNDfAiMLjGVebVHSdNfcakb6xvcducs"},
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

            await page.wait_for_timeout(1000)
            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
