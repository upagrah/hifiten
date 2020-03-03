from django.http import HttpResponse,JsonResponse

def SuccessRes(data):
    response={}
    response['result']='success'
    response['data']=data
    return JsonResponse(response)
def ErrorRes(data):
    response={}
    response['result']='failure'
    response['error_code']=data['error_code']
    response['error_message']=data['error_message']
    response['error_data']=data['error_data']
    return JsonResponse(response,status=response['error_code'])
