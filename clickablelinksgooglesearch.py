'''
Author : Priyam Modi
Title : AutoBrowseEngine 

'''
from googlesearch import search
import webbrowser
import time
def auto_google_search(query,max_results=10):
    print(f"\nSearching for: '{query}'\n")
    try:
        res=list(search(query,num_results=max_results))
        for url in res:
            print(url)
            webbrowser.open_new_tab(url)
            time.sleep(1)  # slight delay to avoid browser overload
    except Exception as e:
        print("Error:", e)
if __name__=="__main__":
    query=input("Enter your search query: ").strip()
    if query:
        try:
            max_results=int(input("Enter number of results to open (default 10): ").strip())
            if max_results<=0:
                print("Using default of 10 results.")
                max_results=10
        except ValueError:
            print("Invalid input, using default of 10 results.")
            max_results=10
        auto_google_search(query,max_results)
    else:
        print("Please enter a valid query.")
