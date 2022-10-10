from selenium import webdriver
from bs4 import BeautifulSoup



def get_page_count(keyword):
    options=webdriver.ChromeOptions() 
    options.add_experimental_option('excludeSwitches',['enable-logging']) 

    browser = webdriver.Chrome("C:\\chromedriver.exe")
    base_url = "https://kr.indeed.com/jobs?q="
    end_url = "&limit=50"
    browser.get(f"{base_url}{keyword}{end_url}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="ecydgvn0") 
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        options=webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches',['enable-logging']) 
        browser = webdriver.Chrome("C:\\chromedriver.exe")
        base_url = "https://kr.indeed.com/jobs?q="
        end_url = "&limit=50"
        page_url = "&start="
        final_url = f"{base_url}{keyword}{page_url}{page*10}{end_url}"
        print("Requesting", final_url)
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)
        

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link':f"https://kr.indeed.com{link}",
                    'company':company.string,
                    'location':location.string,
                    'position':title[:-10]
                }
                results.append(job_data)        
    return results