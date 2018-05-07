# Mission to Mars

[Instructions](https://github.com/RutgersCodingBootcamp/RUTSOM201801DATA5-Class-Repository-DATA)

## Setup

1. Install MongoDB: https://docs.mongodb.com/manual/installation/
2. Install chromedriver:  http://chromedriver.chromium.org/
3. Install Python modules 
```bash
  pip install -r requirements.txt
  ```

## File List

* [README.md](README.md)
* [requirements.txt](requirements.txt)
* [mission_to_mars.ipynb](mission_to_mars.ipynb)
* [app.py](app.py)
* [mars_scrapper.py](mars_scrapper.py)
* templates/
  * [index.html](templates/index.html)
* static/
  * css/
    * [style.css](static/css/style.css)

## Execution 

```bash
python app.py
```

### Some Tricks

In debugging Flask app, it is useful to let server restart when files are changes to avoid manual reload. 
Change to app.py are tracked automatically but not for other files. So added following:

```python```
    app.run(
        debug=True,
        extra_files=[
           './static/css/style.css',
           './templates/index.html',
           './mars_scrapper.py'
        ]
```buildoutcfg

```
## Copyright

Coding Boot Camp © 2017. All Rights Reserved.
