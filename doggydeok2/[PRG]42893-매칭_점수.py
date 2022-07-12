import re


def solution(word, pages):
    find_word = word.lower()
    page_info = []
    for page in pages:
        page = page.lower()
        info = {
            'URL': '',
            'href': [],
            'word_cnt': 0,
        }
        info['URL'] = re.search(r'(<meta property.+content=")(https:\/\/\S*)"\/>', page).group(2)
        for anchor in re.findall(r'<a href="https:\/\/\S*">', page):
            info['href'].append(re.search(r'(https:\/\/\S*)(">)', anchor).group(1))
        for body_word in re.findall(r'[a-z]+', page):
             if body_word == find_word:
                info['word_cnt'] += 1

        page_info.append(info)

    score = [0] * len(pages)
    for i in range(len(pages)):
        score[i] += page_info[i]['word_cnt']
        for j in range(len(pages)):
            if page_info[i]['URL'] in page_info[j]['href']:
                score[i] += page_info[j]['word_cnt'] / len(page_info[j]['href'])

    max_idx, max_val = -1, -1
    for idx, val in enumerate(score):
        if val > max_val:
            max_idx = idx
            max_val = val

    return max_idx