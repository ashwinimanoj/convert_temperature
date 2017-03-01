from django.http import HttpResponse, Http404
import json


def f_to_c(val):
	return (val - 32) / 1.8


def f_to_k(val):
	return (val + 459.67) * 5/9


def f_to_r(val):
	return val + 459.67


def c_to_f(val):
	return (val - 32) * 0.5556

def k_to_f(val):
	return val * 9/5 - 459.67

def r_to_f(val):
	return val - 459.67

def display_root(request):
	html = "Send temperature value in the form of " \
		+ "http://website.com/convert/fahrenheit/212/"
	return HttpResponse(html)

def convert_fahrenheit(request, offset):
	res = {}
	try:
		fahrenheit = int(offset)
	except ValueError:
		raise Http404()
	res["celsius"] = f_to_c(fahrenheit)
	res["kelvin"] = f_to_k(fahrenheit)
	res["rankine"] = f_to_r(fahrenheit)
	return HttpResponse(json.dumps(res), content_type = \
		"application/json")


def convert_celsius(request, offset):
	res = {}
	try:
		celsius = int(offset)
	except ValueError:
		raise Http404()
	res["fahrenheit"] =  c_to_f(celsius)
	res["kelvin"] = f_to_k(res["fahrenheit"])
	res["rankine"] = f_to_r(res["fahrenheit"])
	return HttpResponse(json.dumps(res), content_type = "application/json")


def convert_kelvin(request, offset):
	res = {}
	try:
		kelvin = int(offset)
	except ValueError:
		raise Http404()
	res["fahrenheit"] =  k_to_f(kelvin)
	res["celsius"] = f_to_c(res["fahrenheit"])
	res["rankine"] = f_to_r(res["fahrenheit"])
	return HttpResponse(json.dumps(res), content_type = "application/json")


def convert_rankine(request, offset):
	res = {}
	try:
		rankine = int(offset)
	except ValueError:
		raise Http404()
	res["fahrenheit"] =  r_to_f(rankine)
	res["celsius"] = f_to_c(res["fahrenheit"])
	res["kelvin"] = f_to_k(res["fahrenheit"])
	return HttpResponse(json.dumps(res), content_type = "application/json")


