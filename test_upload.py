from playwright.sync_api import Page, expect

HTML_FORM = """
<!DOCTYPE html>
<html>
<body>
  <form>
    <label for="formFile">Upload demo</label>
    <input type="file" id="formFile" />
    <input type="submit" value="Upload" id="file-submit" />
  </form>
</body>
</html>
"""


# Способ 1: через set_input_files()
def test_upload_set_input_files(page: Page) -> None:
    page.set_content(HTML_FORM)
    page.locator("#formFile").set_input_files("hello.txt")
    expect(page.locator("#formFile")).to_have_value(r"C:\fakepath\hello.txt")


# Способ 2: через слушатель события filechooser
def test_upload_event_listener(page: Page) -> None:
    page.set_content(HTML_FORM)
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
    page.locator("#formFile").click()
    expect(page.locator("#formFile")).to_have_value(r"C:\fakepath\hello.txt")


# Способ 3: через контекстный менеджер expect_file_chooser()
def test_upload_expect_file_chooser(page: Page) -> None:
    page.set_content(HTML_FORM)
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("hello.txt")
    expect(page.locator("#formFile")).to_have_value(r"C:\fakepath\hello.txt")

