from django.http import HttpResponse,JsonResponse
# Create your views here.
# def index(request):
#     return HttpResponse("hello there")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskserializer
from .models import task

@api_view(['GET'])
def overview(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    t = task.objects.all()
    ser = taskserializer(t, many=True)
    return Response(ser.data)

@api_view(['GET'])
def taskdetail(request,pk):
    t = task.objects.get(id=pk)
    ser = taskserializer(t, many=False)
    return Response(ser.data)

@api_view(['POST'])
def taskcreate(request):

	ser = taskserializer(data=request.data)
	call(ser)
	return Response(ser.data)


def call(ser):
	if ser.is_valid():
		ser.save()

@api_view(['POST'])
def taskupdate(request, pk):
	t = task.objects.get(id=pk)
	ser = taskserializer(instance=t,data=request.data)
	call(ser)
	return Response(ser.data)


@api_view(['DELETE'])
def taskdelete(request, pk):
	t = task.objects.get(id=pk)
	t.delete()
	return Response("well done!")