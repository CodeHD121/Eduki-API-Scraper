def load_and_save(file, save_as_xlsx):
    import json
    import pandas as pd

    with open(str(file)) as js:
        data_raw = js.read()

    data = json.loads(data_raw)
    items = data['results']['items']
    results = []
    for item in items:
        name = item['title']
        price = item['price']
        desc = item['description']
        p_id = item['id']
        p_date = item['createdAt']
        s_name = item['author']['details']['publicName']
        s_id = item['author']['id']
        s_follower = item['author']['followersNumber']
        item_dict = {'Artikel': name, 'Preis': price, 'Beschreibung': desc, 'Artikel-ID': p_id, 'Erstellt am': p_date,
                     'Autor': s_name, 'Autor-ID': s_id, 'Autor Follower': s_follower}
        results.append(item_dict)

    df = pd.DataFrame(results)
    df = df.sort_values(by=['Autor Follower', 'Autor', 'Erstellt am'], ascending=False)
    df.to_excel(f'{save_as_xlsx}.xlsx', index=False)


load_and_save('Mathe_9999_2023-03-13.json', 'test')