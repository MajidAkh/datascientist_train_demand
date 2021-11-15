# train_demand

## Requirement
see the requirements.txt

## Local utilisation
You can create virtualenv
```
virtualenv -p python3 venv
```

Activate the virtualenv
```
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

launch from terminal
```
python ./pipeline/main.py
```


## In Docker
Build docker image
```
docker build -t datascientist .
```

Launch in docker
```
docker run -it datascientist
```

