from exa_py import Exa

exa = Exa('2eaab939-9536-4647-81ea-be50a75fda94')

query = input('Search here: ')


response = exa.search(
    query,
    num_results=5,
    type='keyword',
    include_domains=['https://www.google.com'],
)

print(response)


for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
