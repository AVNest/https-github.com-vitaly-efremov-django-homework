# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Alex',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.3,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Student:
    pass


class Statistics:
    # student_id, [Subjects]
    pass

class Subject:
    pass

class Score:
    # Subject,
    pass
