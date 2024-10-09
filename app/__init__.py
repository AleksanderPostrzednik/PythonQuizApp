import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

quiz_questions = [
    {
        'question': 'Co oznacza skrót NLP w kontekście sztucznej inteligencji?',
        'options': [
            'Neuro Linguistic Programming',
            'Natural Language Processing',
            'New Learning Protocol',
            'None Language Processing'
        ],
        'answer': 'Natural Language Processing'
    },
    {
        'question': 'Która biblioteka Pythona jest popularna w przetwarzaniu języka naturalnego?',
        'options': [
            'NumPy',
            'NLTK',
            'Pandas',
            'Matplotlib'
        ],
        'answer': 'NLTK'
    },
    {
        'question': 'Co to jest wizja komputerowa?',
        'options': [
            'Dziedzina zajmująca się interakcją komputerów z ludźmi',
            'Dziedzina pozwalająca komputerom rozumieć i interpretować obrazy',
            'Technika kompresji danych',
            'Metoda optymalizacji algorytmów'
        ],
        'answer': 'Dziedzina pozwalająca komputerom rozumieć i interpretować obrazy'
    },
    {
        'question': 'Która biblioteka jest często używana w wizji komputerowej w Pythonie?',
        'options': [
            'Pillow',
            'OpenCV',
            'Requests',
            'Flask'
        ],
        'answer': 'OpenCV'
    },
    {
        'question': 'Co to jest TensorFlow?',
        'options': [
            'Biblioteka do przetwarzania języka naturalnego',
            'Framework do uczenia maszynowego i głębokiego uczenia',
            'Narzędzie do analizy danych geoprzestrzennych',
            'Biblioteka do tworzenia interfejsów graficznych'
        ],
        'answer': 'Framework do uczenia maszynowego i głębokiego uczenia'
    },
    {
        'question': 'Jakie jest główne zastosowanie LSTM (Long Short-Term Memory) w AI?',
        'options': [
            'Przetwarzanie sekwencji i danych czasowych',
            'Analiza obrazów',
            'Algorytmy sortowania',
            'Kompresja danych'
        ],
        'answer': 'Przetwarzanie sekwencji i danych czasowych'
    },
    {
        'question': 'Co oznacza termin "transfer learning" w uczeniu maszynowym?',
        'options': [
            'Proces kompresji modelu w celu jego przyspieszenia',
            'Wykorzystanie wcześniej wytrenowanego modelu do nowego, pokrewnego zadania',
            'Technika przesyłania danych między sieciami neuronowymi',
            'Metoda zwiększania dokładności modelu poprzez dodanie więcej warstw'
        ],
        'answer': 'Wykorzystanie wcześniej wytrenowanego modelu do nowego, pokrewnego zadania'
    },
    {
        'question': 'Który z poniższych jest frameworkiem do tworzenia aplikacji webowych w Pythonie?',
        'options': [
            'Django',
            'NumPy',
            'Matplotlib',
            'SciPy'
        ],
        'answer': 'Django'
    },
    {
        'question': 'Co to jest uczenie nadzorowane?',
        'options': [
            'Model uczy się na danych bez etykiet',
            'Model uczy się przez interakcję ze środowiskiem',
            'Model uczy się na danych z etykietami',
            'Model uczy się przez analizę danych statystycznych'
        ],
        'answer': 'Model uczy się na danych z etykietami'
    },
    {
        'question': 'Która z poniższych jest biblioteką do implementacji sieci neuronowych w Pythonie?',
        'options': [
            'Keras',
            'Pandas',
            'Requests',
            'BeautifulSoup'
        ],
        'answer': 'Keras'
    },
    {
        'question': 'W jakim celu używa się biblioteki Scikit-Learn?',
        'options': [
            'Do tworzenia aplikacji webowych',
            'Do analizy i wizualizacji danych',
            'Do uczenia maszynowego',
            'Do przetwarzania obrazów'
        ],
        'answer': 'Do uczenia maszynowego'
    },
    {
        'question': 'Co to jest model regresji liniowej?',
        'options': [
            'Model służący do klasyfikacji obrazów',
            'Model predykcyjny stosowany do przewidywania wartości ciągłych',
            'Algorytm klastrowania danych',
            'Metoda redukcji wymiarowości danych'
        ],
        'answer': 'Model predykcyjny stosowany do przewidywania wartości ciągłych'
    },
    {
        'question': 'Który algorytm jest często używany w analizie sentymentu w NLP?',
        'options': [
            'K-means',
            'Naive Bayes',
            'Apriori',
            'DBSCAN'
        ],
        'answer': 'Naive Bayes'
    },
    {
        'question': 'Co oznacza skrót API w kontekście programowania?',
        'options': [
            'Application Programming Interface',
            'Advanced Programming Integration',
            'Automated Process Implementation',
            'Artificial Python Intelligence'
        ],
        'answer': 'Application Programming Interface'
    },
    {
        'question': 'Która biblioteka pozwala na tworzenie interaktywnych wykresów w Pythonie?',
        'options': [
            'Matplotlib',
            'Bokeh',
            'NumPy',
            'Seaborn'
        ],
        'answer': 'Bokeh'
    }
]

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(24).hex()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app