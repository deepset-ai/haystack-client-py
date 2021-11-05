#################################
# Simple Haystack client
#################################

from haystack_client import HaystackClient, HaystackHubClient

client = HaystackClient(host="http://localhost:8000")
# client = HaystackHubClient(user="some_user", password="some_pass")

# get docs
docs = client.get_documents()
# print results
for d in docs[:2]:
    print(d.content)

# trigger a query
answers = client.search(query="Who is the father of Arya Stark?", params={})
print(answers)

# Returns:
# {'answers': [{'answer': 'Ned',
#               'context': '\n'
#                          '====Season 1====\n'
#                          'Arya accompanies her father Ned and her sister Sansa '
#                          "to King's Landing. Before their departure, Arya's "
#                          'half-brother Jon Snow gifts A',
#               'document_id': '180c2a6b36369712b361a80842e79356',
#               'meta': {'name': '43_Arya_Stark.txt'},
#               'offsets_in_context': [{'end': 49, 'start': 46}],
#               'offsets_in_document': [{'end': 49, 'start': 46}],
#               'score': 0.9767240881919861,
#               'type': 'extractive'},
# ...

#client.upload_file()

# client.delete_file()