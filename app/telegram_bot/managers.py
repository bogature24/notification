# from django.contrib.auth import get_user_model
#
# from market.models import TransactionOffer
# from wallet.models import WalletAddress, Wallet
#
# User = get_user_model()
#
#
# def get_wallet(crypto_currency, user_id):
#     random_wallet_address = WalletAddress.objects.filter(currency__name=crypto_currency).order_by("?").first()
#     wallet = Wallet.objects.filter(user__chat_id=user_id, wallet_address__currency__name=crypto_currency)
#     if wallet:
#         wallet = wallet.first()
#     else:
#         wallet = Wallet.objects.create(
#             user=User.objects.get(chat_id=user_id),
#             wallet_address_id=random_wallet_address.id,
#             crypto_amount=0
#         )
#     return wallet
#
#
# def offer_create_transaction(user_id, user_data, amount):
#     user = User.objects.get(chat_id=user_id)
#
#     if user_data.get("type_meny") == "meny_market" and user_data.get("offer") is not None:
#         try:
#             transaction = TransactionOffer.objects.create(buyer=user,
#                                                           offer_id=user_data.get("offer"),
#                                                           crypto_amount=amount,
#                                                           fiat_amount=amount
#                                                           )
#             return transaction
#         except ValueError:
#             return False
#     return False
