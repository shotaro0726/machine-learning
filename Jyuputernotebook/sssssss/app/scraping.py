import requests
from bs4 import BeautifulSoup

from app.assets.database import db_session
from app.assets.models import Data

import datetime


def get_info():
    url = 'https://scraping-for-beginner.herokuapp.com/udemy'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.select('.card-title')[0].string

    student = soup.select('.subscribers')[0].string
    student = int(student.split('：')[1])

    review = soup.select('.reviews')[0].string
    review = int(review.split('：')[1])

    results = {
        'name': name,
        'student': student,
        'review': review
    }
    return results


def write_data():

    _result = get_info()

    date = datetime.date.today()
    student = _result['student']
    review = _result['review']

    row = Data(date=date, subscribers=student, reviews=review)
    db_session.add(row)
    db_session.commit()


if __name__ == '__main__':
    write_data()
