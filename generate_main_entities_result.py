import json
import textrank


def generate_by_textrank(input_dir, output_dir):
    article_id_start, article_id_end = 51158, 51218
    for cur_article_id in range(article_id_start, article_id_end+1):
        input_file_path = input_dir + '/%s'%(cur_article_id)
        input_file_json_dict = json.load(open(input_file_path))
        text = input_file_json_dict['text'].encode('utf8')
        key_phrases_with_scores = textrank.extract_key_phrases(text)
        within_doc_entities = [[{'start':None, 'end':None, 'id':None, 'article': cur_article_id,'text':_[0]}] for _ in key_phrases_with_scores] 
        entity_scores = [_[1] for _ in key_phrases_with_scores]
        result = {
                'id': input_file_json_dict['id'],
                'date': input_file_json_dict['date'],
                'source': input_file_json_dict['source'],
                'text': input_file_json_dict['text'],
                'title': input_file_json_dict['title'],
                'within_doc_entities': within_doc_entities,
                'entity_scores': entity_scores
                }
        json.dump(result, open(output_dir+'/%s.output'%(cur_article_id), 'w'))

if __name__ == '__main__':
    generate_by_textrank('/home/jlu229/entity-event-extraction/models/ArticleData/2017-10-01', '/home/jlu229/entity-event-extraction/models/Entity-Event-Extraction-Baselines/data/text_rank')
        
