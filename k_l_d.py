import requests

def kld(name):
    param = {
        "key": "E4776CB9C2E87197641785F629EA749A",
        "req_type": "json",
        "q": name
    }
    res = (requests.get("https://stdict.korean.go.kr/api/search.do", params = param).json())
    try:
        dfn = res["channel"]["item"]
        i = []
        for j in range(0, len(dfn)):
            i.append(dfn[j]["sense"]["definition"])
    except:
        i = ["검색 결과 없음"]
    
    return(i)

print(kld(input()))
