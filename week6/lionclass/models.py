from django.db import models


class LionClass(models.Model):
    # 장고의 디비에 있는 모델을 쓰겠다.(상속받겠다.)

    status_1 = (1, '모집')
    status_2 = (2, '마감')
    status_choices = (status_1, status_2)
    # 썸네일 이미지 파일 thumbnail image
    thumbnail_image = models.CharField(max_length=255, blank=True)
    # 상태(모집, 마감, …) status
    status = models.CharField(max_length=2, choices=status_choices)
    # 제목 title
    title = models.CharField(max_length=100)
    # 요약 설명 title_description
    title_description = models.CharField(max_length=100)
    # 금액 price
    price = models.IntegerField()
    # 클래스 소개 description
    description = models.TextField()

    # python manage.py makemigrations => 파일 생성
    # python manage.py migrate => 생성된 파일로 디비설계됨
    # 커리큘럼 curriculum
    # - 주차 week
    #   - 강의 주제 lecture
    # FAQ faq
    # - 질문 questions
    # - 답변 answer
