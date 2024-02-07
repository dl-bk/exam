from datetime import datetime

all_sites_dct = {}
class WebPage:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content
        self.publication_date = datetime.now().strftime('%Y-%m-%d')
    
    def view_page_info(self):
        print(f"Page title: {self.title}")
        print(f"Self content: {self.content}")
        print(f"Publication date: {self.publication_date}")

class WebSite:
    def __init__(self, name, url, web_page_dct: dict) -> None:
        self.name = name
        self.url = url
        self.web_page_dct = web_page_dct
    
    def add_web_page(self, title, content):
        new_page = WebPage(title, content)
        self.web_page_dct[title] = new_page
    
    def delete_web_page(self, title):
        for key, value in self.web_page_dct.items():
            if key == title:
                self.web_page_dct.pop(key)
                return True
        return False

    def view_site_info(self):
        print(f"Site name: {self.name}")
        print(f"Site URL: {self.url}")
        choice = input("""
                          1.Show all pages details
                          2.Show only pages titles
                          ---> """)
        for title, page in self.web_page_dct.items():
            if choice == '1':
                page.view_page_info()
            elif choice == '2':
                print(title)
            else:
                print("incorrent action")

while True:
    action = input(f"""
    1. Create Website
    2. Add page to Website
    3. Delete page from website
    4. Show page info
    5. Show site info
    0. exit
    """)

    if action == '0':
        break
    elif action == '1':
        site_name = input("Website name: ")
        site_url = input("Website url: ")
        try:
            website = WebSite(site_name, site_url, {})
            all_sites_dct[site_url] = website
            print(f"Website {site_name} created")
        except Exception as e:
            print(f"ERROR: {str(e)}")
    elif action == '2':
        try:
            site_url = input("Website url: ")
            website = all_sites_dct[site_url]
            page_title = input("Enter page title: ")
            page_content = input("Enter page content: ")

            website.add_web_page(page_title, page_content)
            print(f"page with title {page_title} created")
        except Exception as e:
            print(f"ERROR: {str(e)}")
    elif action == '3':
        try:
            site_url = input("Website url: ")
            page_title = input("Page title to delete:")
            website = all_sites_dct[site_url]
            res = website.delete_web_page(page_title)
            if res:
                print(f"page with title {page_title} deleted")
            else:
                print("Something went wrong. Page is not deleted")
        except Exception as e:
            print(f"ERROR: {str(e)}")
    elif action == '4':
        try:
            site_url = input("Website url: ")
            page_title = input("Page title:")
            website = all_sites_dct[site_url]
            page = website.web_page_dct[page_title]
            page.view_page_info()
        except Exception as e:
            print(f"ERROR: {str(e)}")
    elif action == '5':
        try:
            site_url = input("Website url: ")
            website = all_sites_dct[site_url]
            website.view_site_info()
        except Exception as e:
            print(f"ERROR: {str(e)}")