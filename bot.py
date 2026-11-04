import asyncio
from playwright.async_api import async_playwright, TimeoutError

# Yahan apna answer set karein ("A", "B", "C", ya "D")
ANSWER = "A"

# Yahan apne accounts ki list daal dein
accounts = [

    

  {"username": "tatto-11", "wallet": "3cyAGaZKC4ytEL2vY6D11BKkka2L9fjkdWJY8zzb3ozt"},
  {"username": "tatto-12", "wallet": "DTm8sZPVeCVJgabpvUQs2EgpawnsEWv6D49PSf1uoxvZ"},
  {"username": "tatto-13", "wallet": "5oLTVyQAPc2L4dnXW1LfkZXZnfzdgKkcMpxeQyEc2hYG"},
  {"username": "tatto-14", "wallet": "Fw5DKTvSp5AiszNUT8qRax8U213jGGgXVRc3Q9o3LSRi"},
  {"username": "tatto-15", "wallet": "G9aXvZiUjeLSFgne487EKjKcYR9LhF186GuES8eMY26X"},
  {"username": "tatto-16", "wallet": "DfovEkChdGyyNyDEmFZb4THbyDnWoTey5TNXCkLFLFN9"},
  {"username": "tatto-17", "wallet": "H2RTncSE87W7qJvGJGVWHA31ZBjW21mptJze1WRN8dfA"},
  {"username": "tatto-18", "wallet": "Cp5demxHqAjzZ5s7RdgajCDqQhG8PaGYwwdCRbntia1H"},
  {"username": "tatto-19", "wallet": "g9sg8sqhZ1A6dC9RgioUDrR6HC2cuCAXhvy18TG7pCC"},
  {"username": "tatto-20", "wallet": "3maPTE93qnhCJqRRNTscoEud27WUAdE15VWPMob47ux4"},
  {"username": "tatto-21", "wallet": "6bRVgnC3dR8iR5PHudDHUgZHpCdtCw87BfehH6tjoNUf"},
  {"username": "tatto-22", "wallet": "2biE197FdrcNHjiiSrPxDaqxwRmeDGvPvQYNa6YELvMn"},
  {"username": "tatto-23", "wallet": "Hwxcpj8DAiH77i7iHcs7WgB4WcPP87p435FHdh5N8e5M"},
  {"username": "tatto-24", "wallet": "C3xcf2nc4XBG2m37V8x5fJkUvwhJS7QNzFkobZyL89c"},
  {"username": "tatto-25", "wallet": "Ubb2LrHYmKNd885JWyaYwqVVbeMNBg9L68HSjwYMogL"},
  {"username": "tatto-26", "wallet": "GwXS4FxgW3mMYBkxgj1CoCa6NTuESr77wNR2gDZUrPzW"},
  {"username": "tatto-27", "wallet": "CQDD6J5XevQGvFrQdAAnYxxxbyMCcjR9JL9sEt3WmeDE"},
  {"username": "tatto-28", "wallet": "HoXEnkJL9ycSas68GgTiiy9V873uEsBNLbHioTirii4z"},
  {"username": "tatto-29", "wallet": "Hn2oV8feqv2tPENMjHksXK3kSiTTi1JdYaicp1G5xzxB"},
  {"username": "tatto-30", "wallet": "GCMRZ3ECPsJG2dGa1xrbXtz55NuQYKz4a4iLPg4bRuZ7"},
  {"username": "tatto-31", "wallet": "BU8rTKG5nDYfAzsL91nk9Co9zJnq2SDcXsSYkMSH8NTy"},
  {"username": "tatto-32", "wallet": "9phmMNX4Lm5WmVtKopfMJHKCoDba9QZoCRNwMvxFksMQ"},
  {"username": "tatto-33", "wallet": "2WCbeuBQV56QFJVvVKYu52du54QJCM1sDsbJ52U1pFMD"},
  {"username": "tatto-34", "wallet": "6B5A412jL4b4rKFTn4HpUc18WeQqDgRMyDF7B9tLZnFS"},
  {"username": "tatto-35", "wallet": "2YMeigzhBTFEVKTeMVdYcyWcGH6932m32KRTQUinKacZ"},
  {"username": "tatto-36", "wallet": "Eo1uVXYzkASbAw7kSMt2hLBxFmAfapYGQCmoDTHaF4Yd"},
  {"username": "tatto-37", "wallet": "EcD4Hvr1QSBD7aBEwKPNN1Jsm9HuLQ1pxQNoERcdK8an"},
  {"username": "tatto-38", "wallet": "6yLyruGRJwAb2M7T4Dxr2cVKyhqVPudo3UDS7sZSNpFF"},
  {"username": "tatto-39", "wallet": "XzWbXKwCBCBnWwFYxdUskFqnrTp6WbaZYZVBnDCUWx6"},
  {"username": "tatto-40", "wallet": "sQwyicHRt49n4QJwjLM4qXLPrV9vbyhBujQ9vnyaxcd"},
  {"username": "tatto-41", "wallet": "wnaCc3MANYgNtNRf4qAj1X9j1EfyUk4pFT3udK7J4H1"},
  {"username": "tatto-42", "wallet": "889DUHrrK1uYdBD9ZutjViFSaf6GDfz7QS7KdTBhmx5H"},
  {"username": "tatto-43", "wallet": "6izuTnKpnG3s3DUkmTZhfs4gsMbWGpV9aLTh4bVcRX6v"},
  {"username": "tatto-44", "wallet": "8jnAT5VXZSkCmnDc1kJ7b5gSrhmevkM6jic88nbxA4tk"},
  {"username": "tatto-45", "wallet": "VexKMsCdqdjCKZ2mCwZBL9ZVWHdU6umo9dHc7g9nNSi"},
  {"username": "tatto-46", "wallet": "5d7i6y7N5SarqsxoHfcKcNCyUeB7bcM4YN8CSedQysHE"},
  {"username": "tatto-47", "wallet": "83z12UAuY4oAM1zZsvz1QHZf9qqrDvoHQcjQqy7DrNjt"},
  {"username": "tatto-48", "wallet": "D9GmHaEBF6ShzAoVjhdmfB4DcWiBKR1tLgKCCt5PFyp5"},
  {"username": "tatto-49", "wallet": "FDTmRrTr8eRTUskVJuUDTTSi58VonCjhZcce22KkFMpe"},
  {"username": "tatto-50", "wallet": "2JTFQpU9tQDxkrmiY8JSxgQvts5PfhSPDZZYbwQqCuvr"},
  {"username": "tatto-51", "wallet": "9WdAhDTrrHhuwq6EYhDxFUtuJkgdQS1KhjQrzo14uEc2"},
  {"username": "tatto-52", "wallet": "75cQ6EAUscJEFnYh6yqyGawTr5HTLCv7dueqQyRdnxWh"},
  {"username": "tatto-53", "wallet": "9qqPo4LXR4huEHXwkhamKjz3pMqza1CiuQVFHXojBCdv"},
  {"username": "tatto-54", "wallet": "J53qWZAgmwhvXYbbg45Tig6bTdWwwJkHbPeKovfTKv9h"},
  {"username": "tatto-55", "wallet": "CEz4HtW7aSJ9J54g5jTosEtcULLZCPL4qnmLMVBYCDrp"},
  {"username": "tatto-56", "wallet": "6NyYDxdhtLhETYujt4BW5ZnEZJ6TPLbuXqjj5xhqdAZz"},
  {"username": "tatto-57", "wallet": "6FgvujA9wFJVddgbJddABwhLLJUDpaKZakBKHTHNXND1"},
  {"username": "tatto-58", "wallet": "7Mmtk6avUtdmmHDmEkBfmhiBGs8xpycsS7nJKafbVf3P"},
  {"username": "tatto-59", "wallet": "cWmnxGk3uvsRsTK4AZY3Gm6cfrZGVdZAyVCSH2Zm5gN"},
  {"username": "tatto-60", "wallet": "3mA1CZsuY3HF2M7BNgbiawD9R8ogfaXfp259pRtfjbRf"},
  {"username": "tatto-61", "wallet": "4zo1tHCdrcXj9gE4E919RaHKt9roEg3cpiD23zNZ9NRg"},
  {"username": "tatto-62", "wallet": "61TNCbJdox6CsPpBXXQ78WEGbbeHCC5wnEMjQAMQdyKJ"},
  {"username": "tatto-63", "wallet": "GgCRvupQw4cpWdBWukoqdhuvRJXqKKBUkTKXNwsG9fid"},
  {"username": "tatto-64", "wallet": "8jbLwrQbdu3XH61VbTPP6DXRCgKFMahKMUKUMnAMTiP8"},
  {"username": "tatto-65", "wallet": "Dfvka4UiDw6AntCitHmoW1eVhS4whSqhzwmWS1EsoMub"},
  {"username": "tatto-66", "wallet": "6qMWwcP1wd9y47a8QKL5i6DGdu6GE8ZQW27EwkJFENQ3"},
  {"username": "tatto-67", "wallet": "GJL1pHzmN1JidGWNg3FrGChS66L16cM6ZWk7fSYB3vt7"},
  {"username": "tatto-68", "wallet": "5YvqFWPn22XdxN8L1oKnD9v8XvVpTaSiudatZvCDFapG"},
  {"username": "tatto-69", "wallet": "2dtUNh6tBrwdSh26ZuG3No5UeJ6bJxzvFPUrw3E6j8a9"},
  {"username": "tatto-70", "wallet": "8rsLucJeMB2gmA7h5tR91XgqmaKaARRt97KRseUB39HW"},
  {"username": "tatto-71", "wallet": "E9WrfNg63NBwZ9brQeZpysDZa5M69ug7bF3CXtErgqfL"},
  {"username": "tatto-72", "wallet": "EViAzn15Ejcq1ZkZ2MwAngtXYEuame7kxKFqbdKo4GjQ"},
  {"username": "tatto-73", "wallet": "24Ev17GHp114LRhhMUoptg5N33FWHqoBSmpobfu6RjR8"},
  {"username": "tatto-74", "wallet": "6FcYc6RRscvj3rV5hweXxQJDkxGYvTf3ioEQmCknqNrF"},
  {"username": "tatto-75", "wallet": "An8PZF1kCgAyAd7EnJ9JppZvhWHbABWmH1MV2i1JiPqz"},
  {"username": "tatto-76", "wallet": "DjGfr1MKtjrRqnZwu4m6ZPyAZpykvUtrv5h6JqZTgg7Y"},
  {"username": "tatto-77", "wallet": "2tx7xt7UyUpaUyYs21kVxGK5qmYDrfFrQYtmZBawx6ZH"},
  {"username": "tatto-78", "wallet": "8q5tFxgM4u4DG62cB9tyRu6fDwahxEsfs7XHHCVsJSmk"},
  {"username": "tatto-79", "wallet": "EAi1WC3bXa9Sws4DokeNip3FHtMk49RBwf3Er5QhyC6C"},
  {"username": "tatto-80", "wallet": "yr43pPJLcoRMY9BqSqD1whnHyz3B85CPRzSG8JqTXie"},
  {"username": "tatto-81", "wallet": "AkzoPJPKDR6FYhjo1SMt2k3aXd87sFLQhok613uVh54W"},
  {"username": "tatto-82", "wallet": "8NrZ2WRxtVLaii4ogEzDSAovEvjC6GiWPqBUZ51dnaT6"},
  {"username": "tatto-83", "wallet": "3r3WvsdJT98b8WMeR2zcPFAH7bV4nTG8UQri4y8E1tGr"},
  {"username": "tatto-84", "wallet": "GTrdYh6XzELP83cpwseJJk7x8guaxAWYFhChugnU8cnr"},
  {"username": "tatto-85", "wallet": "8rgf39vDyQkxH28HbMZKzry4w2GVRUypLnJGpf6PCjzW"},
  {"username": "tatto-86", "wallet": "4cwxj1w7FGPwnxdfSK6FKSfi2E4GECfnRkXG4tAhboLD"},
  {"username": "tatto-87", "wallet": "DhseP4drqPdYMZcfoFFkxKYdJJCzACkQj536a2JLhnht"},
  {"username": "tatto-88", "wallet": "FDjjdQ9TZx79kqvv5ab3dYunXwiNAM42UWy49FJUQqRY"},
  {"username": "tatto-89", "wallet": "Hknq1jEiuq8oiRrfNQT46EdXTxW6unebBqPgMmPAnwdy"},
  {"username": "tatto-90", "wallet": "EcpoaZcP9s9iB94UJmzpsjntiBjwQuiC7xNKuT8vLJuy"},
  {"username": "tatto-91", "wallet": "GwNXBidoNqtUVe7EFx3E7tsL15vuXiLnLEW5uABPfxEp"},
  {"username": "tatto-92", "wallet": "3mZqL8Y2kDJ5r9vG8BuTyw8eFhKuLdKa9KQVfL3bkX1Y"},
  {"username": "tatto-93", "wallet": "GJQoFbpaLoLbDDQKY1qgGScNEMukwz6gDcJppzE41Jyu"},
  {"username": "tatto-94", "wallet": "2fKuRkEFZyVdeRYrcNrXY6qVFNdMAYpb4FedLPUgfB6F"},
  {"username": "tatto-95", "wallet": "6ZS46DpYyb8NjzUXALqGHh89FzRKuyDzvaC2kmTHLoK5"},
  {"username": "tatto-96", "wallet": "9AN7TyaHVuSQnAfUCEgXsSkB7WKWPpKvC4Bvv8Gu1kr2"},
  {"username": "tatto-97", "wallet": "7x5WqmDwNnQgACB6BTpeJHLDSFjsmTSScX9aLxojVxMB"},
  {"username": "tatto-98", "wallet": "2e2Mxzrbb13kxsYRWyo9eSurPBnVnaANhcb863b49qzo"},
  {"username": "tatto-99", "wallet": "5gnL2iHiahSM37Rj8RL3Rx79khM14KD3556VJbVYuaF7"},
  {"username": "tatto-100", "wallet": "E6rJapuyuYihJQRcrTNXsojf9YnFMb6BZGjtDeG9bUuD"},#
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
