from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from Core.models import BlockedIp

class BlockIpMiddleware(MiddlewareMixin):
    def process_request(self, request):
        blocked_ip = [ip.ip_addr for ip in BlockedIp.objects.all() ]
        if request.META['REMOTE_ADDR'] in blocked_ip:
            return HttpResponseForbidden()