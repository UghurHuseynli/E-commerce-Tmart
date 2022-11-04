# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from requests import request
# from .models import CardItemModel, CardModel
# from User.models import UserModel

# @receiver(post_save, sender=CardItemModel)
# def create_card_if_not_exist(sender, instance, created, **kwargs):
    
#     print('+++++++++', instance.card.id)
#     # if created:
#     if not CardModel.objects.filter(id=sender.card.id):
#         print('+++++++++++')
#     #     CardModel.objects.create(at_but = False, user=request.user)