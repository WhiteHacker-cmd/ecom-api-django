from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

import braintree

# Create your views here.


gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='2ww4qgmg8wmxm6zy',
    public_key='79tvj5t5fxjyd5rh',
    private_key='809c787fa8cf2a565594b3f11dbb01c1'
  )
)


def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token_view(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Invalid session, Please login again!"})
    return JsonResponse({"clientToken": gateway.client_token.generate(), "success": True})



@csrf_exempt
def process_payment_view(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Invalid session, Please login again!"})
    
    nonce_from_the_client = request.POST("paymentMethodNonce")
    amount_from_the_client = request.POST("amount")


    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        return JsonResponse({
            "success": result.is_success,
            "transaction": result.transaction.id,
            "amount": result.transaction.amount
        })
    
    else:
        return JsonResponse({
            "error": True,
            "success": False,
        })