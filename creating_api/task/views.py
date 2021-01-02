from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class task_one(APIView):

	def get(self, request, string, number):
		if number == 0:
			return Response({ 'Output' : string })

		elif number >= len(string):
			return Response({ 'Output' : string })

		elif number <= len(string):
			string = string[::-1]
			new_string = ''
			for i in range(0, len(string), number):
				new_string+=string[i : i+number] + ' '
			new_string = new_string[::-1]
			new_string = new_string[1:]
		return Response({ 'Output' : new_string })

class task_two(APIView):
	def get(self, request, string):
		new_string = string.split(',')
		count_dict = {}
		for i in new_string:
			if i in count_dict:
				count_dict[i] += 1
			else:
				count_dict[i] = 1
		return Response(count_dict)
