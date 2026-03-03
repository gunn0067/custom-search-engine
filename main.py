from exa_py import Exa

exa = Exa('YOUR_EXA_API_KEY')

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

