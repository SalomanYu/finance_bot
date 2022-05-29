import spacy
import json

def nlp_removing_similiraty_requirements():
    all_requirements_data = json.load(open('req_in_group.json', 'r'))
    import spacy
    
    nlp = spacy.load('ru_core_news_lg')

    dublicate_list = []
    result_data = []
    stopwords = ['имеешь опыт работы в сфере','имеете опыт работы с', 'понимание и опыт работы с', 'имеешь опыт работы с', 'опыт работы с', 'опыт работы со',
                'навыки работы с',  'уверенное знание'  , 'уверенные знания', 'базовые знания' 'отличное знание',  'есть опыт написания', 'опыт разработки',
                'знание принципов', 'понимание принципов', 'понимаете принципы', 'знаете принципы', 'умеете работать', 'умение работать' 'приветствуется',
                 'навык работы с', 'имеете работы с', 'мышление', 'опыт работы/ знание']
    count = len(all_requirements_data)
    for group in all_requirements_data:
        count -= 1
        requirements = group['Общие требования']
        for req in range(len(requirements)-1):
            requirement = requirements[req]
            for taby in stopwords:
                if taby in requirement.lower():
                    requirement = requirement.lower().replace(taby, '').strip()
                    break

            doc1 = nlp(requirement)
            for req2 in range(req+1, len(requirements)):
                next_requirement = requirements[req2]
                for taby in stopwords:
                    if taby in next_requirement.lower():
                        next_requirement = next_requirement.lower().replace(taby, '').strip()


                doc2 = nlp(next_requirement)
                similary = doc1.similarity(doc2)
                if similary * 100 >= 90:
                    dublicate_list.append(requirements[req2])
                    print(f'{requirement} -- {next_requirement} -- {similary*100}')
        

        for item in dublicate_list:
            count = 0
            for item2 in requirements:
                if item == item2:
                    count += 1
            if count > 1 and item in requirements:
                requirements.remove(item)
        
        result_data.append({
            'Группа': group['Группа'],
            'Требования': requirements
        })
        print('Осталось ', count)
    with open('NO_DUBLICATE_REQ.json', 'w') as file:
        json.dump(result_data, file, ensure_ascii=False, indent=2)


nlp_removing_similiraty_requirements()