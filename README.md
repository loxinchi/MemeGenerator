# MemeGenerator

[Overview](#Overview)  
[Installation](#Installation)  
[Run the application](#Run-the-application)  
[Project Scaffolding](#Project-Scaffolding)  
[Dependencies](#Dependencies)

## <a name="Overview"></a>Overview
A multimedia application to dynamically generate memes, including an image with an overlaid quote.
User can make meme by providing image url and quote, author text.

- Interact with a variety of complex filetypes.
- Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Load, manipulate, and save images.
- Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack develope

- Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don’t repeat yourself) principles of class and method design.

## <a name="Installation"></a>Installation
`pip install -r requirements.txt`

## <a name="Run-the-application"></a>Run the app
```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```
  
## <a name="DEMO"></a>DEMO
![demo1](https://user-images.githubusercontent.com/76967954/146972454-9511e7c9-1509-4527-a2c0-e4942869ee1a.gif)  

![demo2](https://user-images.githubusercontent.com/76967954/146972463-05d2a55f-245b-4e3c-912d-55dd211dafa1.gif)


## <a name="Project-Scaffolding"></a>Project Scaffolding
```
├── MemeEngine.py
├── QuoteEngine              <- Pasrse different types of quote data into QuoteModel 
│   ├── CSVIngestor.py
│   ├── DOCXIngestor.py
│   ├── Ingestor.py
│   ├── IngestorInterface.py
│   ├── PDFIngestor.py
│   ├── QuoteModel.py        <- QuoteModel Object
│   ├── TXTIngestor.py       
│   └── exceptions.py        <- Customized exception
├── _data                    <- Resource files of quotes, images, font
│   ├── DogQuotes
│   ├── font
│   ├── SimpleLines
│   └── photos
├── app.py                   <- Load resources and randomly choose one image and QuoteModel and render to html.
├── meme.py                  <- This file generates the final image path.
├── requirements.txt         <- List of project dependencies.
├── templates                <- HTML layout.
├── test                     <- Scripts to run the unittest.
```

## <a name="Dependencies"></a>Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [pandas](https://pandas.pydata.org/)
- [docx](https://python-docx.readthedocs.io/)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [Pillow](https://pillow.readthedocs.io/)


[Follow PEP8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
