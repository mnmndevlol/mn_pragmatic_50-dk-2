FROM python:3.9.0
WORKDIR /home/
RUN echo "testing1"
# RUN git clone https://github.com/mnmndevlol/mn_pragmatic_50.git
COPY . /home/pragmatic_50-dk-2/
WORKDIR /home/pragmatic_50-dk-2/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN echo "SECRET_KEY=django-insecure-(#w^3bt47w6848f%7)go1x6qh8u76l3lm*!7&4v2qqu65*0wwd" > .env
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

