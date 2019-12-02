def search_first(str):
    from algoliasearch import algoliasearch
    client  = algoliasearch.Client("XXXXXXXXXX","XXXXXXXXXXXXX")
    index = client.init_index("book_search")
    # settings = index.get_settings()
    # print(json.dumps(settings,indent = 2))
    # index.set_settings({"searchableAttributes":['title']})
    result = index.search(str)
    first = [{'title':result["hits"][0]['title'],'image_url':result["hits"][0]['image_url'],'author':result["hits"][0]['authors']}]
    # print(len(result["hits"]))
    # for hit in result["hits"]:
    #     print(json.dumps(hit,indent = 2))
    return first
