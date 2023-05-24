try:
    import requests
    import json

    n = int(input('请输入要获取新闻条数：'))

    url = "https://www.toutiao.com/api/pc/feed/?category=news_hot"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    top_news = []
    for item in data['data']:
        if 'title' in item and 'abstract' in item and 'source' in item and 'chinese_tag' in item and '':
            news = {
                'title': item['title'],
                'abstract': item['abstract'],
                'source': item['source'],
                'chinese_tag': item['chinese_tag'],
            }
            top_news.append(news)
        if len(top_news) == n:
            break

    print("\n今日头条新闻热榜前", n, "：\n", sep='')
    nums = 1
    for news in top_news:
        print(nums, '.', news['title'], '\n详细信息：', news['abstract'], '\n来源：', news['source'], '\n标签：',
              news['chinese_tag'], sep='', end='\n\n')
        nums += 1

except Exception as e:
    print('抱歉，网络可能出错了，无法访问此地址！')
    print(e)
    input('Pass any button quit...')

