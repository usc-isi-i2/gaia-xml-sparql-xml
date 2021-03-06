import sys
sys.path.append('..')


from src.Question import Question
from src.Answer import Answer


def run(xml_query):
    with open(xml_query) as f:
        xml = f.read()

    ans = Answer(Question(xml)).ask()

    print(ans)

    from src.utils import write_file
    write_file(ans, xml_query.split('.')[0] + '_response.xml')

# example query provided by NIST
run('graph_query.xml')

# subgraph as query in our dataset
run('autogenerated_query_1.xml')
