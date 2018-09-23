import newspaper
from newspaper import Article

x = []
y = []
z = {}

def select_news():
    global source 
    source = 'http://cnn.com'
    
def print_articles():
    global cnn_paper
    cnn_paper = newspaper.build(source, memoize_articles=False)

def get_popular():
    global pop
    pop = newspaper.popular_urls()
    
def make_lists(a_list):
    global cnn_paper
    for i in cnn_paper.articles:
        a_list.append(i.url)
    
def create_num_list(length_list):
    global y
    y = list(range(len(length_list)))
    
def create_dictionary():
    global x, y, z
    z = dict(zip(y,x))
    
def select_article():
    global z
    url = z[int(input('Which news article would you like to read? '))]    
    article = Article(url)
    article.download()
    article.parse()
    print(article.text)
    
    
select_news()
print_articles()
get_popular()
make_lists(x)
create_num_list(x)
create_dictionary()
print(x)
print(y)
for i,j in z.items():
    print(str(i)+":"+str(j))
select_article()
    

#print(pop)